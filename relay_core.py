"""Deterministic, synthetic fault workflow shared by the Streamlit UI and tests."""
import csv
import io
import math
from datetime import datetime, timedelta, timezone

CLOCK = "2026-10-08T23:00:00.000Z"
STATUSES = ["Submitted", "Assigned", "In progress", "Awaiting confirmation", "Closed"]
UNITS = ["Riverbend", "Northbank", "Lakeside"]
CATEGORIES = ["Device", "Access", "Application", "Network"]
TECHNICIANS = ["Alex T.", "Morgan T.", "Sam T."]
ROLES = ["Requester", "Coordinator", "Technician", "Manager"]
TARGET_HOURS = {"P1": 4, "P2": 24, "P3": 72}


def parse_date(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def iso(value):
    return value.astimezone(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def check(condition, message):
    if not condition:
        raise ValueError(message)


def required_text(value, minimum, maximum, label):
    check(isinstance(value, str), f"{label} is required.")
    value = value.strip()
    check(minimum <= len(value) <= maximum, f"{label} must contain {minimum}–{maximum} characters.")
    return value


def priority(impact, urgency):
    check(impact in ("High", "Standard") and urgency in ("High", "Standard"),
          "Choose a valid impact and urgency.")
    return "P1" if impact == urgency == "High" else "P2" if "High" in (impact, urgency) else "P3"


def event(now, role, action, status, note=""):
    return dict(at=now, role=role, action=action, status=status, note=note)


def create_request(state, data, role):
    check(role in ("Requester", "Coordinator"), "Only a requester or coordinator can submit a request.")
    title = required_text(data.get("title"), 5, 120, "Title")
    description = required_text(data.get("description"), 10, 1000, "Description")
    check(data.get("unit") in UNITS, "Choose a valid unit.")
    check(data.get("category") in CATEGORIES, "Choose a valid category.")
    p = priority(data.get("impact"), data.get("urgency"))
    number = max([1000] + [int(r["id"][3:]) for r in state["records"]]) + 1
    record = dict(
        id=f"RF-{number}", title=title, description=description, unit=data["unit"],
        category=data["category"], impact=data["impact"], urgency=data["urgency"],
        priority=p, status="Submitted", owner="Unassigned", createdAt=state["now"],
        dueAt=iso(parse_date(state["now"]) + timedelta(hours=TARGET_HOURS[p])),
        resolution="", closedAt=None,
        events=[event(state["now"], role, "Request submitted", "Submitted",
                      "Assisted intake" if role == "Coordinator" else "Self-service intake")],
    )
    state["records"].insert(0, record)
    return record


def act(state, request_id, action, role, data=None):
    data = data or {}
    record = next((r for r in state["records"] if r["id"] == request_id), None)
    check(record is not None, "Request not found.")
    rules = {
        "assign": ("Coordinator", "Submitted", "Assigned", "Technician assigned"),
        "start": ("Technician", "Assigned", "In progress", "Work started"),
        "resolve": ("Technician", "In progress", "Awaiting confirmation", "Resolution proposed"),
        "confirm": ("Requester", "Awaiting confirmation", "Closed", "Requester confirmed service restored"),
        "reject": ("Requester", "Awaiting confirmation", "In progress", "Requester rejected resolution"),
    }
    check(action in rules, "Unsupported action.")
    required_role, required_status, next_status, label = rules[action]
    check(role == required_role, f"This action requires the {required_role} demo role.")
    check(record["status"] == required_status, f"This action requires status {required_status}.")
    note = ""
    if action == "assign":
        check(data.get("owner") in TECHNICIANS, "Select a technician.")
        note = data["owner"]
    elif action in ("resolve", "reject"):
        note = required_text(data.get("note"), 10, 1000,
                             "Resolution" if action == "resolve" else "Rejection reason")
    # Validate everything before mutating a record or its history.
    if action == "assign":
        record["owner"] = note
    if action == "resolve":
        record["resolution"] = note
    record["status"] = next_status
    record["closedAt"] = state["now"] if next_status == "Closed" else None
    record["events"].append(event(state["now"], role, label, next_status, note))
    return record


def stats(state):
    records = state["records"]
    return {
        "Open": sum(r["status"] != "Closed" for r in records),
        "Overdue": sum(r["status"] != "Closed" and parse_date(r["dueAt"]) < parse_date(state["now"]) for r in records),
        "Awaiting confirmation": sum(r["status"] == "Awaiting confirmation" for r in records),
        "Closed": sum(r["status"] == "Closed" for r in records),
    }


def filter_records(state, query="", status="All"):
    query = query.strip().casefold()
    return [r for r in state["records"] if (status == "All" or r["status"] == status)
            and any(query in r[key].casefold() for key in ("id", "title", "unit", "owner"))]


def csv_cell(value):
    value = "" if value is None else str(value)
    if value.lstrip().startswith(("=", "+", "-", "@")) or value.startswith(("\t", "\r")):
        value = "'" + value
    return value


def to_csv(records):
    fields = ["id", "title", "unit", "category", "priority", "status", "owner", "createdAt", "dueAt", "resolution", "closedAt"]
    output = io.StringIO(newline="")
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow(fields)
    writer.writerows([[csv_cell(r.get(f)) for f in fields] for r in records])
    return output.getvalue()


def advance_clock(state, hours):
    check(isinstance(hours, (float, int)) and not isinstance(hours, bool)
          and math.isfinite(hours) and 0 < hours <= 168, "Advance by 1–168 hours.")
    state["now"] = iso(parse_date(state["now"]) + timedelta(hours=hours))


def seed():
    state = dict(schema=1, now=CLOCK, records=[])
    rows = [
        ("Shared printer unavailable", "Riverbend", "Device", "High", "Standard", 26, "Submitted", None),
        ("Counter workstations offline", "Northbank", "Network", "High", "High", 2, "Assigned", "Alex T."),
        ("Scanner connection intermittent", "Lakeside", "Device", "Standard", "Standard", 24, "In progress", "Morgan T."),
        ("Training application access restored", "Riverbend", "Access", "Standard", "High", 6, "Awaiting confirmation", "Sam T."),
        ("Spare monitor installed", "Northbank", "Device", "Standard", "Standard", 60, "Closed", "Alex T."),
        ("Team dashboard will not load", "Riverbend", "Application", "High", "Standard", 30, "In progress", "Morgan T."),
        ("Desk headset replaced", "Lakeside", "Device", "Standard", "Standard", 48, "Closed", "Sam T."),
        ("Meeting room screen flickers", "Riverbend", "Device", "Standard", "Standard", 1, "Submitted", None),
    ]
    for index, (title, unit, category, impact, urgency, age, status, owner) in enumerate(rows):
        state["now"] = iso(parse_date(CLOCK) - timedelta(hours=age))
        r = create_request(state, dict(title=title, unit=unit, category=category, impact=impact,
                                      urgency=urgency, description="Synthetic demonstration fault. Staff require support to restore normal service."), "Requester")
        if status != "Submitted":
            act(state, r["id"], "assign", "Coordinator", dict(owner=owner))
        if status in ("In progress", "Awaiting confirmation", "Closed"):
            act(state, r["id"], "start", "Technician")
        if status in ("Awaiting confirmation", "Closed"):
            act(state, r["id"], "resolve", "Technician", dict(note="Service restored using a tested configuration. Requester verification is required."))
        if status == "Closed":
            state["now"] = iso(parse_date(CLOCK) - timedelta(hours=2 if index == 4 else 6))
            act(state, r["id"], "confirm", "Requester")
    state["now"] = CLOCK
    return state
