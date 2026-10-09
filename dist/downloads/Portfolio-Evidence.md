# Relay business analysis portfolio

Version 1.0 | 9 October 2026 | Fictional independent exercise


## Stakeholders and problem analysis

Problem statement: fragmented fault intake and unconfirmed closure create avoidable administration and uncertain service restoration. The proposed service gives staff one visible request, a named owner and a confirmed outcome.
Scope: routine device, access, application and network faults in three fictional licensing support units. Exclusions: weapons licensing decisions, applicant records, exhibits, emergency response, security incident handling, live integrations, procurement and real staff data. Security or safety incidents must use authorised agency channels rather than this proposed routine workflow.
All seven stakeholder groups, six findings and the 50-fault baseline are simulated. In a real engagement, obtain informed participation, validate notes, invite dissent and triangulate interviews with observation and service data before baselining requirements.
Stakeholder map and engagement plan
ID
Stakeholder
Influence and impact
Needs
Engagement
Validation role
ST01
Frontline requesters
High impact / medium influence
Quick reporting; status visibility; assisted channel
Two 30-minute interviews and mobile task test
Validate required fields and confirmation wording
ST02
Service coordinator
High impact / high influence
One queue; fewer follow-ups; clear priorities
Process walkthrough and weekly design playback
Own triage rules and daily aged queue review
ST03
ICT technicians
High impact / high influence
Useful diagnosis; accountable hand-offs
Resolution workshop and exception testing
Validate routing, evidence and reopen rules
ST04
Unit manager and sponsor
High influence / medium impact
Operational continuity; defensible investment
Fortnightly decision brief and gate review
Approve scope, resources and residual risks
ST05
Privacy, security and records advisers
High influence / medium impact
Safe data handling; access; record lifecycle
Early assessment workshop and release review
Confirm applicable controls and evidence
ST06
Platform owner and external support provider
Medium influence / high impact
Reuse approved tools; support boundaries
Integration discovery and hand-off workshop
Confirm tenancy, licensing, contracts and support
ST07
Accessibility and staff representatives
Medium influence / high impact
Accessible reporting; fair workload; safe feedback
Keyboard task test and inclusive change sessions
Challenge barriers and review training options
Interview questions
Walk me through your most recent fault, from detection to confirmation of recovery.
Where do you wait, repeat information or ask another person for an update?
What would make a fault urgent, and what workaround is available?
Who owns each hand-off, and how do you know it has been accepted?
What evidence is needed before closing or reopening a fault?
What information is essential, restricted or unnecessary for this process?
Which accessibility, shift, location or confidence barriers affect reporting?
Which policy, integration and supplier constraints must we validate?
What measure would convince you the new process is better?
Simulated interview findings
ID
Perspective
Fictional observation
Design implication
Evidence status
F01
Requester
I send another email because I cannot see whether anyone owns it.
Status visibility and an immediate reference
Simulated interview, not an actual quotation
F02
Coordinator
We re-enter the same fault into a spreadsheet, then ask for the missing location.
Structured intake and one queue
Simulated interview
F03
Technician
Urgent means something different to every person.
Agreed impact and urgency matrix
Simulated workshop
F04
Requester
The ticket was closed, but the printer still did not work.
Resolution evidence and explicit confirmation
Simulated interview
F05
Records adviser
A spreadsheet does not explain who changed a status and why.
Event history and controlled records export
Simulated workshop
F06
Staff representative
A web form cannot be the only way to get help.
Assisted intake and accessible task testing
Simulated interview
Success measures
The baseline below is an invented four-week sample of 50 faults, separate from the eight seeded prototype records. Targets are hypotheses to validate in a comparable four-week pilot. No operational benefits have been measured.
ID
Measure
Synthetic baseline
Proposed target
Measurement and owner
M01
Administrative handling time
12 minutes per fault
≤ 6 minutes
Observed active minutes / completed faults; same definition before and after; coordinator; 4-week pilot
M02
Submission completeness
36 / 50 = 72%
≥ 95%
Submissions accepted without clarification / all submissions; coordinator; weekly; assisted intake included
M03
Status-chasing contacts
22 / 50 = 44%
≤ 20%
Faults with at least one status-only follow-up / all faults; coordinator; weekly
M04
Confirmed closure
30 / 50 = 60%
100%
Closed faults with explicit requester confirmation / all closed faults; process owner; weekly
M05
Operational guardrail
Not established
No service or accessibility deterioration
Track priority breaches, reopen rate and assisted-channel completion; establish baseline before pilot; sponsor
Assumptions and validation backlog
A01: 50 routine faults per month and 12 minutes active handling per fault. Validate through a time-and-motion baseline; do not include technician repair time.
A02: staff have an approved device and platform access. Confirm with the platform owner and include an assisted channel.
A03: a business owner can define priorities and organise requester confirmation. Validate with all shifts and the coordinator.
A04: existing approved service tooling may meet the need. Assess before building or procuring another platform.
A05: policies, retention rules, real data classification and supplier arrangements are unknown. Obtain authoritative agency decisions before a pilot.


## Current and future process analysis

These simplified swimlanes show responsibilities and hand-offs; they are not asserted to be BPMN 2.0 compliant or to describe actual QPS processes. Open the SVG for a larger view, or edit the diagrams.net source.
Current state
Open current-state SVG
Edit current-state draw.io
Proposed future state
Open future-state SVG
Edit future-state draw.io
Gap analysis
Gap
Current state
Problem or risk
Proposed improvement
Findings
Requirements
Measures
G01
Email, phone and spreadsheet intake
Incomplete information and duplicate entry
Structured form plus assisted intake in the same queue
F02, F06
R01, R10
M01, M02
G02
Unowned spreadsheet rows
Faults wait between teams
Named technician and visible state transitions
F01
R02, R03
M03
G03
Priority is self-selected
Unequal treatment and hidden operational risk
Impact and urgency matrix with visible due time
F03
R04
M05
G04
Closure by technician alone
Unresolved faults disappear from the backlog
Resolution evidence; requester confirms or rejects
F04
R05, R06
M04
G05
Overwritten spreadsheet cells
Weak accountability and unreliable reporting
Append event history; controlled export in target solution
F05
R07, R08
M05
G06
Review based on anecdotes
Repeated faults and benefits not evidenced
Queue measures and scheduled trend review
F01, F02
R09
M01, M03
G07
Unvalidated platform controls
Privacy, access and retention risks
Agency assessments and release gates before production
F05
R11, R12
M05
Priority definitions and timing are proposed business rules. High impact means multiple staff blocked; High urgency means no practical workaround. P1 = both High (4 elapsed hours); P2 = either High (24 hours); P3 = neither High (72 hours). The timer does not pause for confirmation. Capacity and escalation arrangements need sponsor validation.


## Business requirements and traceability

BRD purpose: define a testable service workflow for the fictional problem. Baseline version 1.0 is ready for portfolio review; business approval is not claimed. Must for pilot controls remain mandatory gates even though this prototype does not implement them.
Business outcomes and solution boundary
Reduce handling and chasing, improve submission quality and verify restoration. The working prototype is static HTML, CSS and JavaScript with a browser-local dataset. It demonstrates service behaviour, not production identity, protected audit, cross-device persistence or a deployed Microsoft 365 solution.
R01 · Must · Functional
As a requester, I want to submit a structured fault so that the coordinator has enough information to act.
Acceptance criteria:
 Given a new request, when title (5–120 characters), unit, category, impact, urgency and description (10–1000 characters) are valid, create a unique sequential reference and Submitted event. Reject blank or out-of-range values without saving.
Implemented in demo · Gap G01 · Tests T01, T02, T03
R02 · Must · Functional
As a coordinator, I want to assign a technician so that each accepted fault has an accountable owner.
Acceptance criteria:
 Given a Submitted fault and the Coordinator demo role, assigning a named technician moves it to Assigned and appends an event. Reject an empty technician or another role. Reassignment after submission is outside this prototype.
Implemented in demo · Gap G02 · Tests T04, T05
R03 · Must · Functional
As a technician, I want controlled state changes so that progress is meaningful and consistent.
Acceptance criteria:
 Only Assigned → In progress and In progress → Awaiting confirmation are permitted for the Technician demo role. Skip transitions are rejected without mutation.
Implemented in demo · Gap G02 · Tests T06, T07
R04 · Must · Business rule
As a coordinator, I want consistent priority rules so that faults are treated fairly.
Acceptance criteria:
 High impact and High urgency gives P1 with 4 elapsed hours; either High gives P2 with 24 hours; otherwise P3 with 72 hours. Due time is created time plus the target and never pauses while awaiting confirmation. These are proposed targets, not QPS SLAs.
Implemented in demo · Gap G03 · Tests T08
R05 · Must · Functional
As a technician, I want to record what restored service so that the requester can verify the result.
Acceptance criteria:
 Resolution requires 10–1000 characters and an In progress fault. Saving moves it to Awaiting confirmation with an event; a shorter note is rejected.
Implemented in demo · Gap G04 · Tests T09
R06 · Must · Functional
As a requester, I want to confirm or reject a resolution so that a fault closes only when service works.
Acceptance criteria:
 Only the Requester demo role can act on Awaiting confirmation. Confirming closes the fault and records closedAt. Rejecting with a reason of 10–1000 characters returns it to In progress, preserves prior events and clears closedAt. No automatic closure.
Implemented in demo; identity enforcement deferred · Gap G04 · Tests T10, T11
R07 · Must · Control
As a reviewer, I want a time-stamped event history so that hand-offs are explainable.
Acceptance criteria:
 Every successful creation and transition appends actor role, event, state and timestamp. Failed actions append nothing. The demo history is locally mutable; a production release needs server-managed identity and tamper-resistant records.
Demo history implemented; production assurance deferred · Gap G05 · Tests T12
R08 · Should · Functional
As a coordinator, I want a filtered CSV export so that I can review the same queue outside the app.
Acceptance criteria:
 Export exactly the filtered records with headers; quote commas, quotes and line breaks; prefix formula-like cells to prevent spreadsheet execution. Display fictional-data and local-storage notices.
Implemented in demo · Gap G05 · Tests T13
R09 · Should · Functional
As a manager, I want workload and completion measures so that I can identify pressure and trends.
Acceptance criteria:
 Display all-record counts for open, overdue, awaiting confirmation and closed faults. Open means every state except Closed; overdue is open and dueAt < demo clock. Search covers reference, title, unit and owner; status filters combine with search.
Implemented in demo · Gap G06 · Tests T14, T15
R10 · Must · Quality
As a staff member, I want a usable and inclusive service so that reporting does not depend on device or digital confidence.
Acceptance criteria:
 Provide labelled fields, keyboard-operable dialogs, visible focus, text status labels, a narrow-screen layout and an assisted-intake SOP. Conduct representative assistive-technology and user testing before release; full WCAG conformance is not claimed.
Basic UI checks executed; user validation deferred · Gap G01 · Tests T16, U01
R11 · Must for pilot · Security and privacy
As a security and privacy adviser, I want enforced access and assessed data handling so that operational information is protected.
Acceptance criteria:
 Before pilot, approve classification, privacy assessment, data location and supplier review; enforce SSO and server-side least privilege including ownership; test cross-user denial, logs and breach response. Role switching is only a demo convenience.
Production release gate; not implemented · Gap G07 · Tests U02
R12 · Must for pilot · Records and operations
As a records and platform owner, I want approved lifecycle and support controls so that records remain usable and service is recoverable.
Acceptance criteria:
 Before pilot, approve the applicable retention schedule without inventing a period; test restore, record export, support ownership, incident runbook and controlled deployment rollback. Keep requirements, decisions and releases versioned.
Production release gate; not implemented · Gap G07 · Tests U03
Data dictionary
Field
Type
Definition and validation
id
System-generated text
RF-1001 onwards; unique within the local demo dataset
title / description
Required text
5–120 / 10–1000 characters; synthetic details only
unit
Controlled list
Riverbend, Northbank or Lakeside; all fictional
category
Controlled list
Device, Access, Application or Network; no credentials
impact / urgency
Controlled lists
High or Standard; High impact = multiple staff blocked; High urgency = no practical workaround
priority / dueAt
Derived fields
P1/P2/P3 and UTC ISO timestamp; displayed as Australia/Brisbane
status / owner
Controlled state / alias
Submitted, Assigned, In progress, Awaiting confirmation, Closed; technician alias
resolution / closedAt
Text / optional timestamp
Resolution evidence retained across rejection; closure timestamp only on confirmation
events
Ordered event collection
Actor role, action, status, note and UTC time; local demonstration, not immutable audit
Requirements traceability matrix
Requirement
Gap
Priority
Test coverage
Delivery status
R01
G01
Must
T01, T02, T03
Implemented in demo
R02
G02
Must
T04, T05
Implemented in demo
R03
G02
Must
T06, T07
Implemented in demo
R04
G03
Must
T08
Implemented in demo
R05
G04
Must
T09
Implemented in demo
R06
G04
Must
T10, T11
Implemented in demo; identity enforcement deferred
R07
G05
Must
T12
Demo history implemented; production assurance deferred
R08
G05
Should
T13
Implemented in demo
R09
G06
Should
T14, T15
Implemented in demo
R10
G01
Must
T16, U01
Basic UI checks executed; user validation deferred
R11
G07
Must for pilot
U02
Production release gate; not implemented
R12
G07
Must for pilot
U03
Production release gate; not implemented
Download traceability CSV
Microsoft 365 implementation blueprint
First assess the approved service management platform. If it cannot meet the need, test a low-code alternative in an approved tenant: Power Apps for intake, SharePoint or Microsoft Lists for the request register, a separate event list for state history, Power Automate for controlled notifications and escalation, and Power BI for trends. No tenant configuration or licensing has been performed in this portfolio.
Design Request and RequestEvent lists with stable IDs, controlled choice columns, UTC timestamps and indexed filter fields; confirm delegation and realistic list volumes.
Use agency SSO and group-based permissions; implement requester and assigned-technician restrictions in the data/service layer. Hiding controls in Power Apps is insufficient.
Make state transitions server-validated and protect the event repository from end-user modification; use concurrency checks and idempotent flows to prevent duplicate events.
Configure retention and record capture with the records owner; do not assume a SharePoint version history is sufficient. Validate tenant location, connector paths and supplier terms.
Test notification failures, flow retries, backup/restore, operational support and licensing before pilot. The web demo does not send email or run automatic escalation.


## Governance risk and compliance

This is a control mapping and validation plan, not a compliance certification or legal interpretation. The current public sources were reviewed on 9 October 2026. Agency owners must confirm applicability and internal policy requirements.
Framework
Application to this project
Required evidence
Requirements
Sources
QGEA
Use the current Queensland architecture policy catalogue to assess platform reuse and applicable policies. Confirm applicability with the agency architecture owner.
Architecture decision record; approved platform and integration assessment
R11, R12
S01
IS18 current June 2026
The current Information and cyber security policy uses lifecycle risk management and an ISO 27001 based ISMS. Map this project into agency assurance; this demo does not establish compliance.
Classification, access-control test, security assessment and accepted residual risks
R11
S02
Information Privacy Act 2009 and QPPs
Use current Queensland Privacy Principles. Minimise personal data and assess collection, use, disclosure and transfers. Complete a privacy assessment before introducing actual staff or applicant data.
Privacy impact assessment, collection notice and breach response decision
R11
S03, S04
Public Records Act 2023
Create and manage appropriate records. Validate the applicable Queensland State Archives and agency retention and disposal requirements; no arbitrary retention period is proposed.
Records mapping, authorised retention decision and recoverable export
R07, R12
S05
Customer experience and accessibility
QPS references the Queensland Digital Service Standard. Use needs research, clear status, assisted service and accessibility validation as design inputs.
Task observations, inclusive research, U01 and pilot feedback
R10
S06
QPS ICT policies and practices
Internal policies were not supplied. Obtain the current authorised security, documentation, release and version-control requirements from accountable owners before implementation.
Agency-specific compliance checklist and release approvals
R11, R12
Role document
Risk register
Likelihood and impact use 1–5 scales. Score = likelihood × impact; Low 1–4, Medium 5–9, High 10–25. Ratings are scenario estimates, not agency assessments. Residual High risks K02 and K07 remain unacceptable for production and are explicit release gates.
ID
Risk
Inherent score
Mitigation
Owner
Residual score
Acceptance or gate
K01
Operational or personal data entered into public demo
3 × 5 = 15 High
Synthetic-only warning; no attachments; no network submission; reset local data
Project author
1 × 5 = 5 Medium
Restrict the production intake and assess privacy before pilot
K02
Demo role switch mistaken for access control
4 × 5 = 20 High
Explicit role simulation label; R11 and cross-user denial test as pilot gate
Security lead
2 × 5 = 10 High
Unaccepted for production; SSO and server enforcement required
K03
Staff keep using separate email queues
4 × 3 = 12 High
Champions, assisted intake, clear service channel and daily reconciliation
Process owner
2 × 3 = 6 Medium
Pilot adoption must reach 80% before expansion
K04
Wrong priority or unrealistic target
3 × 4 = 12 High
Agree impact definitions; calibrate capacity; review breached high-priority faults daily
Coordinator
2 × 3 = 6 Medium
Sponsor validates targets before pilot
K05
Fault marked resolved while service is still unavailable
3 × 4 = 12 High
Evidence plus requester confirmation; rejection returns to active work
ICT lead
1 × 4 = 4 Low
Test T09–T11 and monitor reopen rate
K06
Inaccessible interface or exclusion of shift staff
3 × 4 = 12 High
Keyboard checks, assisted intake, recorded training plus captioned materials
Change lead
2 × 3 = 6 Medium
Representative users must pass U01
K07
Loss or alteration of records in browser storage
4 × 4 = 16 High
State openly that demo storage is disposable; production repository and restore tests
Platform owner
3 × 4 = 12 High
Unaccepted for production until U03 passes
K08
Unsupported tenant, connector cost or data location
3 × 4 = 12 High
Confirm approved platform, licensing, residency, supplier terms and support model
Platform owner
2 × 4 = 8 Medium
No procurement or live tenant assumed
K09
Misleading benefit or compliance claims
3 × 4 = 12 High
Label invented baseline, proposed targets, executed checks and outstanding gates
Project author
1 × 4 = 4 Low
Do not present prototype checks as stakeholder sign-off
Document control
Version
Date
Change
Status
0.1
9 Oct 2026
Scenario, findings and process baseline drafted
Superseded draft
0.9
9 Oct 2026
Prototype, requirements and governance mapped
Superseded draft
1.0
9 Oct 2026
Executed prototype tests and packaged portfolio evidence
Portfolio review baseline; no agency approval
Approver role
Decision required
Status
Project author
Portfolio baseline and disclosure accuracy
Prepared for review
Business sponsor
Scope, success measures, funding and residual risks
Not sought; fictional project
Security / privacy / records owners
Applicable controls and assessment evidence
Not sought; no agency implementation
Business UAT lead
Pilot acceptance and rollout readiness
Not executed
Version and change practice
Keep requirements, maps, decisions, source and test evidence in version control. A change request records problem, affected requirement IDs, benefit, risk, owner and acceptance impact. Assess it with the process owner, update traceability and tests, then baseline a reviewed release. Operational records require their own approved records repository; source control is not a substitute.
Decision log
ID
Decision
Reason
Status
D01
Use routine ICT faults in a fictional licensing unit
Align to system operationalisation while excluding operational licensing decisions
Project author; 9 Oct 2026
D02
Demonstrate local browser state only
Provide a complete low-friction interview workflow with synthetic data; no agency integration
Project author; 9 Oct 2026
D03
Require confirmation and allow rejection
Address false closure risk; no automatic closure timeout
Project author; 9 Oct 2026
D04
Prefer approved platform reuse
Limit bespoke support cost; conditional M365 pilot if existing platform is unsuitable
Proposed; sponsor validation pending
D05
Use fixed demo clock initially
Keep seed queue measures reproducible; advance the clock explicitly in the demo
Project author; 9 Oct 2026


## Testing implementation and review

Test plan: run a fresh synthetic dataset through submission, assignment, repair, rejection and closure. Check invalid inputs, role restrictions, event preservation, target calculations and export. Prototype results below were executed by the project author, not independent business users. They do not constitute organisational UAT.
Entry criteria: agreed requirements, versioned build and reproducible seed data. Pilot exit criteria: all Must and Must for pilot requirements passed in the target environment, zero Severity 1 (service/security failure) or Severity 2 (critical task blocked) defects, accessibility issues resolved and documented sponsor acceptance. Lesser defects need an owner and due date.
Executed prototype checks
Test
Scenario and expected behaviour
Requirements
Result
Execution method
T01
Valid fault creates a Submitted request and initial event
R01
Pass
Automated domain check
T02
Invalid and whitespace input rejected without saving
R01
Pass
Automated domain check
T03
Unique references and assisted intake
R01, R10
Pass
Automated domain check
T04
Coordinator assignment records owner and event
R02
Pass
Automated domain check
T05
Empty owner and wrong-role assignment fail atomically
R02
Pass
Automated domain check
T06
Assigned fault can start only with Technician role
R03
Pass
Automated domain check
T07
Skipped or unknown transitions leave data unchanged
R03
Pass
Automated domain check
T08
All four priority combinations and target intervals
R04
Pass
Automated domain check
T09
Resolution requires adequate evidence and proper role
R05
Pass
Automated domain check
T10
Requester confirmation closes once and stamps closure
R06
Pass
Automated domain check
T11
Rejection requires reason, preserves history and returns to work
R06
Pass
Automated domain check
T12
Successful events retain roles, states and timestamps
R07
Pass
Automated domain check
T13
CSV quotes special characters and neutralises formula cells
R08
Pass
Automated domain check
T14
Snapshot queue counts and clock-driven overdue changes
R09
Pass
Automated domain check
T15
Search and status filters combine, with empty result
R09
Pass
Automated domain check
T16
Browser workflow, form labels and responsive review
R01–R10
Pass
Verified submit → assign → start → resolution → reject → second resolution → confirmed closure; short resolution rejected; browser reset and reload preserved eight records; 390 px layout had no page overflow; all form fields labelled; Tab and Escape operated intake dialog. Not full WCAG or screen-reader validation.
Download test cases with steps and expected results
 · 
Download machine-readable results
Business UAT and production gates
Test
Participants
Scenario
Expected result
Status
Requirements
U01
Representative requesters including an assistive-technology user
Complete submit, follow status and confirm or reject across mobile, keyboard and screen reader; assisted request enters same queue
No critical task barrier; feedback resolved
Not executed; representative users required
R10
U02
Security and privacy advisers
Verify SSO; requester A cannot view or alter requester B records; technician access matches assignment; evaluate collection, logs and breach response
No unauthorised access; signed assessment and residual-risk decision
Not executable on browser-only demo
R11
U03
Records and platform owners
Apply approved retention rules; export records; restore backup; deploy and roll back; verify incident hand-off
Evidence meets approved records, recovery and support criteria
Not executable until target platform exists
R12
U04
Process owner and nominated business testers
Repeat T01–T16 in the target platform and exercise interruption, duplicate reports and supplier hand-off
All Must requirements pass; no open Severity 1 or 2 defects
Planned; no business acceptance claimed
R01–R10
Change communications and rollout
Stage
Accountable owner
Activity
Gate
Discover / week 1
Process owner and BA
Validate baseline and workflow with all shifts; include accessibility and supplier voices
Research notes agreed; scope and outcome definitions approved
Design / week 2
BA, platform owner and advisers
Playback requirements; challenge priority rules; assess approved platform reuse
Requirements baseline and privacy, security, records assessments completed
Validate / week 3
ICT and representative users
Complete UAT including exceptions, permission denial and restore; train champions
All Must for pilot requirements passed and residual risks accepted
Pilot / weeks 4–7
Process owner and change lead
Small volunteer unit; 20-minute role-based sessions; captioned guide; assisted channel; daily triage
80% channel adoption; no critical service, privacy or accessibility issue
Review / week 8
Sponsor and BA
Compare like-for-like baseline; inspect incidents and feedback; decide expand, revise or stop
Written review and sponsor decision; no automatic expansion
Audience
Message
Channel and timing
Feedback
All shifts
Why the change matters; how to report; assisted help remains available
Sponsor announcement before pilot; team briefing and captioned quick guide
Short task observation and anonymous issue channel
Coordinators and technicians
Priority definitions, ownership, rejection and exception handling
Role-based workshop before pilot; daily 10-minute triage during week 1
Record process issues and triage conflicts
Manager and advisers
Performance, incidents, adoption and control readiness
Weekly pilot note and gate review
Explicit accept, revise or stop decision
Training and support
Use a 20-minute hands-on session for each role: requesters submit and confirm; coordinators triage and assist; technicians record evidence and handle rejection. Provide a one-page illustrated guide, captioned recording, shift-friendly repeats and named champions. Publish safe escalation channels and support hours agreed with the platform owner.
Cutover and rollback
Before cutover, reconcile open faults to unique references, assign owners, test access and restore, publish support details and stop dual entry. Keep the prior approved register available read-only. If access failures block critical work, a serious privacy/security event occurs or records cannot be recovered, the process owner pauses intake, returns to the approved fallback channel, reconciles changes and seeks sponsor authority before restarting. Never roll back by deleting operational records.
Post implementation review plan
No operational implementation or PIR has occurred. At the end of the proposed four-week pilot, compare M01–M05 with an agreed like-for-like baseline, segment by priority and assisted intake, inspect outliers and reopen causes, and report adoption and unresolved control issues. The sponsor decides expand, refine or stop at week 8. A 30/60/90-day benefits review follows only if rollout proceeds.
Continuous improvement and working agreement
Maintain an improvement backlog linking feedback to gaps and requirements. Hold a weekly retrospective, rotate demonstrations, invite respectful challenge and record decisions without blame. Include all shifts and accessibility needs, share documentation, manage workload fairly and use safe channels for sensitive concerns. These are proposed team practices, not claims of previous employment performance.


## Advice to management

To: fictional Unit Manager. From: portfolio project author. Date: 9 October 2026. Decision sought: approve a short discovery and controlled pilot design, subject to platform, privacy, security and records assurance. This is a simulated briefing, not a real funding request.
Recommendation
Assess the existing approved service platform first. Configure it if it meets the requirements. If it does not, design a limited Microsoft 365 pilot in an approved tenant after R11 and R12 pass. Use the current web application only to validate workflow and requirements; it is not a production deployment recommendation.
Issue and evidence
The fictional unit handles faults across emails and spreadsheets, with duplicated handling, unclear ownership and closure without requester confirmation. Six simulated findings and a synthetic sample of 50 faults support the design exercise. Actual service data and stakeholder validation are required before investment decisions.
Options appraisal
Option
Approach
Advantages
Risks and dependencies
Assessment
A
Improve the spreadsheet
Low effort; immediate template and ownership rules
Still fragmented; weak automation, permissions and records evidence
Interim fallback only
B
Configure an existing approved service platform
Reuse identity, support, record lifecycle and reporting capabilities
Availability, licensing, configuration and integration must be established
Preferred after discovery confirms fit
C
Microsoft 365 low-code pilot
Microsoft Lists or SharePoint, Power Apps and controlled Power Automate flows
Item permissions, delegation, connector licensing, audit and records design need validation
Conditional pilot if option B cannot meet needs
D
Commission a custom production application
Maximum workflow flexibility
Highest delivery, assurance and ongoing support burden
Do not recommend at this stage
Benefits and indicative effort
At 50 faults per month, reducing active administrative handling from 12 to 6 minutes would release 50 × 6 / 60 = 5 staff hours per month. At an assumed loaded rate of A$65 per hour, this represents A$325 per month or A$3,900 per year in potential capacity value, not cash savings. At 25–100 faults per month, the same assumption gives 2.5–10 hours per month. The synthetic baseline does not establish demand or a return on investment.
Allow an indicative 8–12 person-days for discovery, configuration, assessment, testing and training, before licensing, integration or remediation. At the same assumed rate and 7.6-hour day this is A$3,952–A$5,928 in effort. This is an estimate for comparison, not a quote; benefit alone does not yet justify custom development.
Risks conditions and next decision
Primary risks are improper access, uncontrolled records, adoption failure and misleading priorities. Confirm platform fit, classification, privacy, retention, support and access denial before any live pilot. Residual High risks for demo access and storage remain unaccepted for production. Measure completeness, handling, chasing, confirmation and service guardrails during the pilot. Expand only after a documented sponsor review; stop or revise if safety, security, accessibility or service quality deteriorates.
Download the two-page management briefing


## Recruiter walkthrough and capability mapping

A five-minute walkthrough
Time
Show
Explain
0:00–0:45
One-page summary
Fictional problem, scenario boundaries and the proposed outcomes
0:45–1:30
Current/future maps and one gap
Follow G04 through R05/R06 to T09–T11
1:30–3:30
Prototype lifecycle
Submit, assign, resolve, reject, then confirm; inspect the history
3:30–4:15
Governance and tests
Distinguish demonstrated behaviour from outstanding production gates
4:15–5:00
Management briefing
Recommend reuse; explain the conditional benefit model and pilot decision
All nine role capabilities
#
Role requirement
Portfolio evidence
Interview emphasis
1
Coordinate and improve IT systems and BA
F01–F06; G01–G07; R01–R12; working prototype
Translate fragmented work into a controlled service workflow
2
Develop and support change management
Change plan; training guide; pilot and rollback criteria
Include shift staff, champions, assisted reporting and support ownership
3
Determine requirements within legislative, IT and customer frameworks
BRD; acceptance criteria; data dictionary; governance mapping
Identify policy constraints and validate internal rules with owners
4
Adhere to IT policies, security, documentation and version control
R11–R12; risk register; decision log; document control
Make unimplemented assurance controls explicit release gates
5
Advise management on improvement, innovation and risk
Two-page briefing; options appraisal; benefit model
Recommend reuse before custom build and avoid overstated savings
6
Analyse, document, develop, test, deliver, implement and review
Process maps; traceability; demo; executed tests; rollout and PIR plan
Separate completed prototype work from proposed organisational rollout
7
Engage operational and business stakeholders
Stakeholder map; questions; engagement plan; validation backlog
Explain the engagement approach; interviews in this project are simulated
8
Identify improvements and current/future gaps
Editable swimlanes; gap analysis; linked measures
Trace each change to a bottleneck, requirement and test
9
Contribute to an ethical, inclusive and improving team
Working agreement; accessible service; feedback and learning loop
Invite challenge, share knowledge and avoid inventing actual leadership experience
STAR answer for this portfolio exercise
Situation: “For an independent portfolio exercise, I modelled a fictional licensing support unit where IT faults were handled across email and a spreadsheet.” Task: “I set out to demonstrate an end-to-end BA approach to reducing administrative effort and improving confirmed restoration.” Action: “I created simulated stakeholder findings, mapped the hand-offs, traced gaps into testable requirements, built the workflow and documented the assurance and change gates.” Result: “I delivered a working prototype and executed domain checks. The benefit targets remain hypotheses; a real pilot would validate them.”
Team leader behaviour without invented experience
The supplied role identifies the Team leader stream. Use the decision log to explain how you would lead a project without direct reports: agree outcomes, invite challenge, communicate trade-offs, support learning, manage risks and hold decision owners accountable. Pair this exercise with truthful examples from your own work when addressing previous performance.
Application context
The supplied role description is Business Analyst AO5, Weapons Licensing Group, Legal Division, Brisbane, QLD/702780/26. It lists Tuesday 13 October 2026 as the closing date and seeks strong change management, process mapping and Microsoft Suite experience. The role document and applicant guide request a statement of no more than two A4 pages and a current CV. Treat the portfolio as supporting evidence; the written statement needs genuine previous-performance examples. These application details are taken from the supplied documents and have not been reverified against a live advertisement.


## Sources assumptions and downloads

Public framework references were checked on 9 October 2026. The attached recruitment documents were used as source material for role alignment, not as instructions to carry out application actions. No application, email or stakeholder communication has been submitted.
S01 · 
QGEA policy catalogue
Official framework catalogue; confirm applicability at design gate
S02 · 
Information and cyber security policy IS18
Current v10.0.0; effective June 2026; checked 9 October 2026
S03 · 
OIC privacy reform information
QPP reforms commenced 1 July 2025; checked 9 October 2026
S04 · 
OIC privacy impact assessments
Current privacy assessment guidance; checked 9 October 2026
S05 · 
Public Records Act 2023
Official Queensland legislation; current version checked 9 October 2026
S06 · 
QPS Digital Service Standard
Official QPS customer experience context; checked 9 October 2026
Supplied role documents
702780-26-Role Description.docx and 702780-26-Applicant Guide non-Police.docx, supplied by the applicant. Original files and contact details are not copied into the hosted portfolio.
Download and reuse
Portfolio pack: summary, discovery, maps, requirements, controls, testing, change, management advice and interview material.
Editable draw.io maps and SVG exports; CSV traceability, risk, gap and UAT registers; Markdown evidence source and prototype source.
All names, units, operational scenarios, interview findings and baseline figures are fictional. No QPS logo, approval or affiliation is claimed.
Portfolio PDF pack
One-page summary
Editable evidence and source ZIP