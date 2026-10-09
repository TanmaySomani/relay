"""Workflow regression checks and actual Streamlit widget integration checks.

Run: python -m unittest discover -s tests -p 'test_*.py' -v
These are automated prototype checks, not stakeholder UAT.
"""
import copy
import csv
import io
from pathlib import Path
import unittest

from streamlit.testing.v1 import AppTest
from relay_core import (act, advance_clock, create_request, filter_records,
                        parse_date, priority, seed, stats, to_csv)

ROOT = Path(__file__).resolve().parents[1]


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.state = seed()
        self.data = dict(title="Fictional display fault", description="Synthetic screen fails to show the training application.",
                         unit="Riverbend", category="Device", impact="High", urgency="High")

    def test_seed_and_aging(self):
        self.assertEqual(stats(self.state), {"Open": 6, "Overdue": 2, "Awaiting confirmation": 1, "Closed": 2})
        advance_clock(self.state, 24)
        self.assertEqual(stats(self.state)["Overdue"], 4)
        self.assertEqual(stats(self.state)["Open"], 6)

    def test_priority_matrix_and_deadlines(self):
        for impact, urgency, expected, hours in [("High", "High", "P1", 4), ("High", "Standard", "P2", 24), ("Standard", "High", "P2", 24), ("Standard", "Standard", "P3", 72)]:
            with self.subTest(impact=impact, urgency=urgency):
                self.assertEqual(priority(impact, urgency), expected)
                r = create_request(self.state, dict(self.data, impact=impact, urgency=urgency), "Requester")
                self.assertEqual((parse_date(r["dueAt"]) - parse_date(r["createdAt"])).total_seconds(), hours * 3600)

    def test_lifecycle_with_rejection(self):
        r = create_request(self.state, self.data, "Requester")
        self.assertEqual(r["id"], "RF-1009")
        act(self.state, r["id"], "assign", "Coordinator", dict(owner="Alex T."))
        act(self.state, r["id"], "start", "Technician")
        act(self.state, r["id"], "resolve", "Technician", dict(note="Synthetic driver updated and display checked."))
        act(self.state, r["id"], "reject", "Requester", dict(note="Display still fails after a restart."))
        self.assertEqual(r["status"], "In progress")
        self.assertIsNone(r["closedAt"])
        act(self.state, r["id"], "resolve", "Technician", dict(note="Synthetic cable replaced and test repeated."))
        act(self.state, r["id"], "confirm", "Requester")
        self.assertEqual(r["status"], "Closed")
        self.assertEqual(r["closedAt"], self.state["now"])
        self.assertEqual(len(r["events"]), 7)

    def test_invalid_transitions_are_atomic(self):
        for action, role, data in [("confirm", "Requester", {}), ("start", "Technician", {}), ("assign", "Requester", {"owner": "Alex T."}), ("assign", "Coordinator", {"owner": "Unknown"}), ("delete", "Manager", {})]:
            before = copy.deepcopy(self.state)
            with self.assertRaises(ValueError):
                act(self.state, "RF-1001", action, role, data)
            self.assertEqual(self.state, before)

    def test_invalid_intake_does_not_create_records(self):
        for change in [dict(title="tiny"), dict(description="short"), dict(unit="Unknown"), dict(category="Unknown"), dict(impact="Critical"), dict(title="x" * 121)]:
            before = copy.deepcopy(self.state)
            with self.assertRaises(ValueError):
                create_request(self.state, dict(self.data, **change), "Requester")
            self.assertEqual(self.state, before)
        with self.assertRaises(ValueError):
            create_request(self.state, self.data, "Technician")

    def test_resolution_and_rejection_need_evidence(self):
        for request_id, action, role in [("RF-1003", "resolve", "Technician"), ("RF-1004", "reject", "Requester")]:
            before = copy.deepcopy(self.state)
            with self.assertRaises(ValueError):
                act(self.state, request_id, action, role, dict(note="short"))
            self.assertEqual(self.state, before)

    def test_search_and_status_filter(self):
        self.assertEqual(len(filter_records(self.state, " RIVERBEND ", "Submitted")), 2)
        self.assertEqual(len(filter_records(self.state, "Alex T.")), 2)
        self.assertEqual(len(filter_records(self.state, "RF-1004")), 1)
        self.assertEqual(filter_records(self.state, "no-match"), [])

    def test_csv_roundtrip_and_formula_defence(self):
        r = create_request(self.state, dict(self.data, title='=SUM(1,2) "synthetic"', description="Synthetic detail"), "Requester")
        r["resolution"] = 'Line one, with comma\nLine two "quoted"'
        rows = list(csv.DictReader(io.StringIO(to_csv([r]))))
        self.assertEqual(rows[0]["title"], "'" + r["title"])
        self.assertEqual(rows[0]["resolution"], r["resolution"])
        self.assertEqual(rows[0]["closedAt"], "")

    def test_invalid_clock_advance(self):
        for hours in [0, -1, 169, float("inf"), float("nan"), True, "24"]:
            before = self.state["now"]
            with self.assertRaises(ValueError):
                advance_clock(self.state, hours)
            self.assertEqual(self.state["now"], before)


class StreamlitIntegrationTests(unittest.TestCase):
    def app(self, page="Overview"):
        app = AppTest.from_file(str(ROOT / "streamlit_app.py"), default_timeout=20).run()
        if page != "Overview":
            app.sidebar.radio(key="page").set_value(page).run()
        self.assertEqual(len(app.exception), 0, str(app.exception))
        return app

    def assert_clean(self, app):
        self.assertEqual(len(app.exception), 0, str(app.exception))

    def test_all_pages_and_evidence_sections(self):
        app = self.app()
        for page in ["Working demo", "Evidence library", "Downloads", "Overview"]:
            app.sidebar.radio(key="page").set_value(page).run()
            self.assert_clean(app)
            if page == "Evidence library":
                for section in app.selectbox(key="evidence_section").options:
                    app.selectbox(key="evidence_section").select(section).run()
                    self.assert_clean(app)

    def test_submit_validation_and_create(self):
        app = self.app("Working demo")
        app.button(key="FormSubmitter:intake-Submit request").click().run()
        self.assertTrue(app.error)
        self.assertEqual(len(app.session_state.workflow["records"]), 8)
        app.text_input(key="new_title").input("Fictional counter display issue")
        app.text_area(key="new_description").input("Synthetic display fails during staff training.")
        app.button(key="FormSubmitter:intake-Submit request").click().run()
        self.assert_clean(app)
        self.assertEqual(app.session_state.workflow["records"][0]["id"], "RF-1009")
        self.assertEqual(app.selectbox(key="request_id").value, "RF-1009")

    def test_widgets_complete_rejection_and_closure(self):
        app = self.app("Working demo")
        app.selectbox(key="request_id").select("RF-1001").run()
        app.selectbox(key="demo_role").select("Coordinator").run()
        app.button(key="FormSubmitter:assign_RF-1001-Assign request").click().run()
        app.selectbox(key="demo_role").select("Technician").run()
        app.button(key="start_RF-1001").click().run()
        app.text_area(key="resolution_RF-1001").input("Synthetic printer configuration updated and checked.")
        app.button(key="FormSubmitter:resolve_RF-1001-Propose resolution").click().run()
        app.selectbox(key="demo_role").select("Requester").run()
        app.text_area(key="rejection_RF-1001").input("Synthetic printer still produces blank pages.")
        app.button(key="FormSubmitter:reject_RF-1001-Return to technician").click().run()
        app.selectbox(key="demo_role").select("Technician").run()
        app.text_area(key="resolution_RF-1001").input("Synthetic printer cartridge replaced and output verified.")
        app.button(key="FormSubmitter:resolve_RF-1001-Propose resolution").click().run()
        app.selectbox(key="demo_role").select("Requester").run()
        app.button(key="confirm_RF-1001").click().run()
        self.assert_clean(app)
        record = next(r for r in app.session_state.workflow["records"] if r["id"] == "RF-1001")
        self.assertEqual(record["status"], "Closed")
        self.assertEqual(len(record["events"]), 7)

    def test_filters_clock_reset_and_session_isolation(self):
        app = self.app("Working demo")
        app.button(key="advance").click().run()
        self.assertEqual(stats(app.session_state.workflow)["Overdue"], 4)
        other = self.app("Working demo")
        self.assertEqual(stats(other.session_state.workflow)["Overdue"], 2)
        app.text_input(key="query").input("no-match").run()
        self.assertTrue(any("No requests" in item.value for item in app.info))
        app.button(key="reset").click().run()
        self.assert_clean(app)
        self.assertEqual(stats(app.session_state.workflow)["Overdue"], 2)
        self.assertEqual(app.text_input(key="query").value, "")


if __name__ == "__main__":
    unittest.main()
