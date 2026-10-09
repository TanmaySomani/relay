"""Relay: a recruiter-ready business analysis case study and synthetic demo."""
import json
from datetime import timedelta, timezone
from pathlib import Path

import streamlit as st

from relay_core import (CATEGORIES, ROLES, STATUSES, TECHNICIANS, UNITS, act,
                        advance_clock, create_request, filter_records, parse_date,
                        seed, stats, to_csv)

ROOT = Path(__file__).resolve().parent
DOWNLOADS = ROOT / "dist" / "downloads"
st.set_page_config(page_title="Relay | BA portfolio", page_icon="↗", layout="wide")
st.markdown("""<style>
 .block-container {max-width:1180px;padding-top:2.3rem;padding-bottom:3rem}
 h1 {font-size:3.7rem!important;letter-spacing:-.06em;line-height:1.07!important}
 h2,h3 {letter-spacing:-.025em}
 [data-testid="stMetric"] {border-top:2px solid #157566;padding-top:1rem}
 [data-testid="stSidebar"] {border-right:1px solid #d9ded4}
 .eyebrow {font-size:.76rem;letter-spacing:.16em;font-weight:700;color:#157566}
 .intro {font-size:1.18rem;line-height:1.65;max-width:760px;color:#41594e}
 </style>""", unsafe_allow_html=True)


def read_json(path):
    return json.loads((ROOT / path).read_text())


def date_label(value):
    return parse_date(value).astimezone(timezone(timedelta(hours=10))).strftime("%d %b %Y, %H:%M AEST")


def download(filename, label, key):
    path = DOWNLOADS / filename
    mime = "application/pdf" if path.suffix == ".pdf" else "application/zip"
    st.download_button(label, path.read_bytes(), file_name=filename, mime=mime, key=key)


def overview():
    st.markdown('<p class="eyebrow">INDEPENDENT BUSINESS ANALYSIS CASE STUDY · 2026</p>', unsafe_allow_html=True)
    st.title("Less chasing. Clearer ownership.")
    st.markdown('<p class="intro">Relay improves how a fictional public-sector licensing support unit reports, tracks and closes routine IT faults. Explore the analysis, then test the proposed workflow.</p>', unsafe_allow_html=True)
    st.caption("Prepared by Tanmay Somani · Fictional scenario and synthetic data · No QPS affiliation or endorsement")
    cols = st.columns(3)
    with cols[0]:
        download("Relay-One-Page-Summary.pdf", "↓ One-page summary", "summary_top")
    with cols[1]:
        download("Relay-Management-Brief.pdf", "↓ Management briefing", "brief_top")
    with cols[2]:
        download("Relay-Portfolio-Pack.pdf", "↓ Full evidence pack", "pack_top")
    st.divider()
    left, right = st.columns([1.15, 1], gap="large")
    with left:
        st.subheader("The problem")
        st.write("Email requests and a manually maintained spreadsheet create incomplete intake, duplicate handling and uncertain ownership. Staff cannot reliably see progress, and faults can close before service is restored.")
        st.subheader("The approach")
        st.write("Map the current process, test assumptions with simulated stakeholder discovery, trace gaps into requirements and design a controlled request-to-confirmation workflow. Assess existing approved service tools before selecting a platform.")
    with right:
        st.subheader("The proposed outcome")
        st.write("One queue, agreed priorities, accountable hand-offs and requester confirmation before closure. A small conditional pilot would test operational value and compliance.")
        st.info("Modelled opportunity: 12 → 6 minutes of handling per fault. At an assumed 50 faults per month, that is 5 hours of capacity. These are synthetic assumptions and targets; benefits have not been achieved.")
    st.subheader("Evidence across the delivery lifecycle")
    for col, (title, description) in zip(st.columns(3), [
        ("01 / Understand", "Stakeholder map, engagement plan, interview questions, findings and success measures."),
        ("02 / Design", "Current and future swimlanes, gap analysis, requirements, acceptance criteria and traceability."),
        ("03 / Deliver & review", "Prototype, tests, risk register, change plan, implementation gates and management advice."),
    ]):
        with col:
            st.markdown(f"**{title}**")
            st.write(description)
    st.caption("Tools: Python / Streamlit · HTML / CSS / JavaScript · draw.io · CSV registers · PDF evidence pack · Git version control")
    with st.expander("Five-minute recruiter walkthrough", expanded=False):
        st.markdown("1. **Frame the problem** and distinguish assumed measures from validated findings.\n2. **Trace G04 → R05/R06 → T09/T10/T11** in the evidence library.\n3. **Run the demo:** submit → assign → start → propose resolution → reject → resolve again → confirm.\n4. **Discuss the recommendation:** reuse approved tools first, then conduct a gated pilot.\n5. **Explain production controls** and what business UAT still needs to prove.")
    st.caption("This portfolio supports an interview discussion. Present your genuine prior-work examples separately from this independent exercise.")


def demo():
    st.markdown('<p class="eyebrow">WORKING PROTOTYPE / SYNTHETIC DATA ONLY</p>', unsafe_allow_html=True)
    st.title("The fault queue")
    st.write("Follow a request from intake to confirmed restoration. Change the demo role to explore each hand-off.")
    st.warning("Demo roles simulate responsibilities and do not authenticate people or enforce request ownership. Enter fictional details only. Session data is processed by the Streamlit host; there is no persistent shared database or protected audit store.")
    if "workflow" not in st.session_state:
        st.session_state.workflow = seed()
    state = st.session_state.workflow
    role = st.selectbox("Demo role", ROLES, key="demo_role")
    for col, (label, value) in zip(st.columns(4), stats(state).items()):
        col.metric(label, value)
    st.caption(f"Simulation clock: {date_label(state['now'])}. Targets use elapsed hours: P1 = 4, P2 = 24, P3 = 72. No timer pause or automatic closure. These are proposed demo rules, not agency SLAs.")
    with st.expander("Demo controls"):
        cols = st.columns(2)
        if cols[0].button("Advance clock 24 hours", key="advance"):
            advance_clock(state, 24)
            st.rerun()
        if cols[1].button("Reset synthetic demo", key="reset"):
            for key in list(st.session_state):
                if key != "page":
                    del st.session_state[key]
            st.rerun()
        st.caption("Reset affects this session only. Session data may be lost on disconnect or restart. Use CSV to keep a copy of fictional results.")
    if role in ("Requester", "Coordinator"):
        with st.expander("Submit a fault", expanded=False):
            with st.form("intake", clear_on_submit=True):
                title = st.text_input("Title", max_chars=120, key="new_title")
                description = st.text_area("Description", max_chars=1000, key="new_description", help="Describe the fictional impact and symptoms; no personal, operational or sensitive data.")
                cols = st.columns(2)
                unit = cols[0].selectbox("Unit", UNITS, key="new_unit")
                category = cols[1].selectbox("Category", CATEGORIES, key="new_category")
                impact = cols[0].selectbox("Impact", ["Standard", "High"], key="new_impact", help="High: multiple staff or a key service affected.")
                urgency = cols[1].selectbox("Urgency", ["Standard", "High"], key="new_urgency", help="High: restoration needed promptly; confirm thresholds in discovery.")
                if st.form_submit_button("Submit request"):
                    try:
                        record = create_request(state, dict(title=title, description=description, unit=unit, category=category, impact=impact, urgency=urgency), role)
                        st.session_state.flash = f"{record['id']} submitted. Priority {record['priority']}."
                        st.session_state.request_id = record["id"]
                        st.rerun()
                    except ValueError as error:
                        st.error(str(error))
    if "flash" in st.session_state:
        st.success(st.session_state.pop("flash"))
    cols = st.columns([2, 1])
    query = cols[0].text_input("Search ID, title, unit or owner", key="query")
    status = cols[1].selectbox("Status filter", ["All"] + STATUSES, key="status_filter")
    records = filter_records(state, query, status)
    st.caption(f"{len(records)} of {len(state['records'])} requests")
    if not records:
        st.info("No requests match these filters. Clear the search or choose another status.")
        return
    st.dataframe([{"ID": r["id"], "Title": r["title"], "Unit": r["unit"], "Priority": r["priority"], "Status": r["status"], "Owner": r["owner"], "Target (AEST)": date_label(r["dueAt"])} for r in records], hide_index=True, width="stretch")
    st.download_button("Export filtered queue (CSV)", to_csv(records), "relay-synthetic-faults.csv", "text/csv", key="queue_csv")
    ids = [r["id"] for r in records]
    if st.session_state.get("request_id") not in ids:
        st.session_state.request_id = ids[0]
    selected = st.selectbox("Open request", ids, key="request_id")
    record = next(r for r in records if r["id"] == selected)
    st.subheader(f"{record['id']} · {record['title']}")
    st.write(f"**{record['status']}** · {record['priority']} · {record['unit']} · {record['category']} · Owner: {record['owner']}")
    st.write(record["description"])
    if record["resolution"]:
        st.markdown("**Latest proposed resolution**")
        st.write(record["resolution"])
    if record["closedAt"]:
        st.success(f"Requester confirmed restoration at {date_label(record['closedAt'])}.")
    actions(record, state, role)
    with st.expander("Request history", expanded=True):
        st.caption("Illustrative session history. A production implementation needs a protected, authorised records store.")
        for item in reversed(record["events"]):
            st.markdown(f"**{item['action']}** · {item['role']} · {date_label(item['at'])}")
            if item["note"]:
                st.write(item["note"])


def perform(state, record, action, role, data=None):
    try:
        result = act(state, record["id"], action, role, data)
        st.session_state.flash = f"{result['id']} → {result['status']}"
        st.rerun()
    except ValueError as error:
        st.error(str(error))


def actions(record, state, role):
    status = record["status"]
    if role == "Coordinator" and status == "Submitted":
        with st.form(f"assign_{record['id']}"):
            owner = st.selectbox("Assign technician", TECHNICIANS, key=f"owner_{record['id']}")
            if st.form_submit_button("Assign request"):
                perform(state, record, "assign", role, dict(owner=owner))
    elif role == "Technician" and status == "Assigned":
        if st.button("Start work", key=f"start_{record['id']}"):
            perform(state, record, "start", role)
    elif role == "Technician" and status == "In progress":
        with st.form(f"resolve_{record['id']}"):
            note = st.text_area("Resolution evidence", max_chars=1000, key=f"resolution_{record['id']}", help="10–1000 characters; explain the fix and how it was checked.")
            if st.form_submit_button("Propose resolution"):
                perform(state, record, "resolve", role, dict(note=note))
    elif role == "Requester" and status == "Awaiting confirmation":
        if st.button("Confirm service restored", key=f"confirm_{record['id']}"):
            perform(state, record, "confirm", role)
        with st.form(f"reject_{record['id']}"):
            note = st.text_area("Why is the fault unresolved?", max_chars=1000, key=f"rejection_{record['id']}")
            if st.form_submit_button("Return to technician"):
                perform(state, record, "reject", role, dict(note=note))
    elif status != "Closed":
        expected = {"Submitted": "Coordinator", "Assigned": "Technician", "In progress": "Technician", "Awaiting confirmation": "Requester"}[status]
        st.info(f"Next step is with the {expected}. Select that demo role to continue.")


def evidence():
    st.markdown('<p class="eyebrow">ANALYSIS / DECISIONS / TRACEABILITY</p>', unsafe_allow_html=True)
    st.title("The evidence library")
    st.caption("Evidence baseline 1.0 · 9 October 2026 · Interviews, measures, approvals and implementation plans are simulated or proposed. Business UAT remains planned.")
    sections = read_json("evidence/sections.json")
    choice = st.selectbox("Evidence section", [row[1] for row in sections], key="evidence_section")
    selected = next(row for row in sections if row[1] == choice)
    # Generated project HTML is trusted local content, never interpolated user input.
    # Inline local map images; the isolated component cannot resolve static-relative paths.
    import base64
    html = selected[2]
    for filename in ("current-state.svg", "future-state.svg"):
        data = base64.b64encode((DOWNLOADS / filename).read_bytes()).decode()
        html = html.replace(f'downloads/{filename}', f'data:image/svg+xml;base64,{data}')
    html = html.replace('href="downloads/', 'target="_blank" rel="noopener" href="https://raw.githubusercontent.com/TanmaySomani/relay/main/dist/downloads/')
    st.iframe("""<!doctype html><html lang="en"><head><meta charset="utf-8"><style>
    body{font:16px/1.6 system-ui,sans-serif;color:#17342e;background:#f8f7f3;margin:0 12px 16px 0}
    h2,h3{line-height:1.25}table{border-collapse:collapse;width:100%;font-size:14px;margin:20px 0}
    th,td{border:1px solid #cbd5cb;padding:10px;text-align:left;vertical-align:top}th{background:#e5ece4}
    a{color:#076452}img{max-width:100%;height:auto}.table-wrap{overflow:auto}
    .note,aside{background:#e9eee6;padding:14px;border-left:3px solid #157566}code{overflow-wrap:anywhere}
    </style></head><body>""" + html + "</body></html>", height="content", alt=choice)
    st.caption("For printable evidence, editable maps and CSV registers, open Downloads. Evidence links open source files from this project's GitHub repository.")


def downloads():
    st.markdown('<p class="eyebrow">RECRUITER PACK / EDITABLE EVIDENCE</p>', unsafe_allow_html=True)
    st.title("Take the evidence with you.")
    st.write("Start with the one-page summary. Use the briefing for the management recommendation and the full pack for supporting detail.")
    for filename, label in [
        ("Relay-One-Page-Summary.pdf", "Download one-page summary (PDF)"),
        ("Relay-Management-Brief.pdf", "Download two-page management briefing (PDF)"),
        ("Relay-Portfolio-Pack.pdf", "Download full portfolio evidence pack (PDF)"),
    ]:
        download(filename, label, filename)
    download("Relay-Evidence-and-Source.zip", "Download evidence and source (ZIP)", "source_zip")
    st.subheader("Editable maps and registers")
    files = ["current-state.drawio", "future-state.drawio", "current-state.svg", "future-state.svg", "requirements-traceability.csv", "gap-analysis.csv", "risk-register.csv", "uat-test-cases.csv", "Portfolio-Evidence.md"]
    filename = st.selectbox("Evidence file", files)
    st.download_button("Download selected evidence", (DOWNLOADS / filename).read_bytes(), filename, "application/octet-stream", key="evidence_file")
    st.link_button("View source on GitHub ↗", "https://github.com/TanmaySomani/relay")
    st.subheader("Validation and implementation status")
    st.write("The original browser prototype has 15 automated domain checks and a recorded browser review. The Streamlit port has its own Python and AppTest suite in this repository. Neither represents stakeholder UAT or production sign-off.")
    st.write("A real pilot requires approved hosting, identity and permissions, privacy and classification assessment, protected records, retention, backups, accessibility review, support ownership and rollback evidence.")


with st.sidebar:
    st.markdown("## ↗ Relay")
    st.caption("BUSINESS ANALYSIS PORTFOLIO")
    page = st.radio("Explore", ["Overview", "Working demo", "Evidence library", "Downloads"], key="page")
    st.divider()
    st.markdown("**Tanmay Somani**")
    st.caption("Fictional public-sector process improvement. Synthetic data only.")
    st.link_button("GitHub source ↗", "https://github.com/TanmaySomani/relay")

{"Overview": overview, "Working demo": demo, "Evidence library": evidence, "Downloads": downloads}[page]()
