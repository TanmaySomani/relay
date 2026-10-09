# Relay business analysis portfolio

A complete independent BA case study for routine ICT fault handling in a **fictional licensing support unit**. Prepared for the capability profile in QLD/702780/26, QPS Business Analyst AO5. No QPS affiliation, endorsement or access is claimed.

## Run the Streamlit app

Python 3.12 is recommended. The app needs no API key, credentials or external database.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run streamlit_app.py
```

The Streamlit app includes the overview, a native interactive fault workflow, the full evidence library and downloadable PDFs, maps and registers. Cloud entry point: `streamlit_app.py`; branch: `main`; dependency file: `requirements.txt`.

The Streamlit workflow uses **per-session, in-memory state** on the server. Data can disappear on disconnect, reload or server restart. It does not provide a persistent shared queue, identity, ownership enforcement or protected audit records. Enter synthetic details only. The original static prototype described below uses browser local storage; these are separate demos with the same workflow rules.

## Run the original static portfolio

Start with `dist/index.html`, or serve `dist/` locally and open the printed address. The JavaScript module prototype needs HTTP rather than a `file:` URL.

```sh
python3 -m http.server 4173 --bind 127.0.0.1 --directory dist
```

Open `http://127.0.0.1:4173/`. The site is buildless HTML/CSS/JavaScript. It can also be hosted on GitHub Pages or another static host; publish the contents of `dist` as the site root.

## Recruiter presentation

1. Send `dist/downloads/Relay-One-Page-Summary.pdf` as the introduction.
2. Demonstrate the prototype in `app.html` using the role selector.
3. Follow gap G04 → requirements R05/R06 → tests T09/T10/T11.
4. Use the management briefing to discuss trade-offs and the conditional pilot.
5. Use the complete pack for detailed questions. It is an evidence appendix, not the two-page application statement.

The supplied role documents request genuine previous-performance examples. This independent exercise must not be described as prior QPS work, real stakeholder consultation, production delivery or realised business benefits. Add truthful examples from your own experience to your application statement.

## Contents

- Portfolio page with a skimmable one-page narrative.
- Static evidence library covering stakeholders, simulated interview findings, measures, current/future swimlanes, gaps, BRD, acceptance criteria, data dictionary, traceability, controls, risks, change, UAT, review and management advice.
- Working prototype: structured intake; impact/urgency priority; controlled assignment and transitions; resolution evidence; requester confirmation/rejection; history; search; status filter; CSV; clock advancement; local persistence and reset.
- One-page PDF summary, two-page PDF management briefing and full PDF evidence pack.
- Editable `.drawio` maps, SVG exports and CSV registers.
- Machine-readable test results and runnable domain checks.
- Interview walkthrough, STAR example and nine-capability mapping.

## Evidence status

All people, units, fault data, interview observations and baseline measures are synthetic. Baseline measures use an invented 50-fault sample; the app uses a separate eight-record seed dataset. The starting clock is 9 October 2026 at 09:00 Australia/Brisbane (UTC+10). Targets count elapsed hours and do not pause while awaiting confirmation. This is not an agency SLA.

15 automated domain checks and a browser integration review passed on 9 October 2026. Business UAT and production controls U01–U04 are planned and have not been signed off. The browser review included the rejection loop, validation feedback, reset/reload, labelled inputs, basic keyboard operation and a 390px viewport. Full accessibility conformance is not claimed.

## Security and production boundary

The role selector is a simulation. It does not authenticate an individual or enforce request ownership. Data and event history are editable in local browser storage, can be lost, and do not synchronise across browsers or devices. There is no protected audit store, email, automated escalation, attachment upload, agency integration or operational backend.

Only enter fictional details. A real pilot needs an approved platform, server-enforced identity and permissions, privacy and classification assessment, protected records, authorised retention, backup/restore, support and rollback evidence. The recommended implementation assesses existing service tooling first; the Microsoft 365 blueprint is conditional and has not been deployed.

## Reproduce evidence

Node 18+ is sufficient for the zero-dependency domain suite:

```sh
node tests/model.test.mjs
```

Run the Streamlit port's nine Python workflow checks and four AppTest integration checks:

```sh
python -m unittest discover -s tests -p 'test_*.py' -v
```

The Streamlit checks cover all four screens and eight evidence sections, input validation, a complete assignment/rejection/confirmation lifecycle, filtering, clock advancement, reset and isolation between two sessions. See `evidence/streamlit-validation.json` for the executed result. These checks do not replace stakeholder UAT, accessibility conformance or production acceptance.

The suite writes `evidence/project-data.json` from the authoring data and `evidence/test-results.json`. Browser observations are separately recorded in `evidence/ui-results.json`.

Authoring scripts require Python with `lxml`, `reportlab`, `pypdf` and `Pillow`:

```sh
python3 scripts/build_evidence.py
python3 scripts/build_pdfs.py
python3 scripts/check_site.py
python3 scripts/package_source.py
```

`build_evidence.py` generates the static evidence library, editable diagrams and CSVs. `build_pdfs.py` generates the three PDFs. `render_pdf_qa.py` is an environment-specific QA helper using the bundled Poppler renderer and is not needed to run the site. Site files are tracked directly; no npm installation or web build is required.

## Version and release

Evidence baseline: 1.0, 9 October 2026. Streamlit port: 1.1. Requirements, maps, test evidence, decisions and source are versioned together. The repository and ZIP exclude hosting identity, original recruitment files, credentials, temporary QA images and Git metadata. The original PDF baseline describes the static prototype; Streamlit-specific storage and checks are recorded here and in `evidence/streamlit-validation.json`.

Public framework references and checks are in the evidence library. Internal QPS ICT policies were not supplied and must be obtained from authorised owners before implementation. Review framework currency again before any real project.
