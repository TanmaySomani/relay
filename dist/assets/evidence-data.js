window.RELAY_EVIDENCE = {
  version:'1.0', date:'9 October 2026',
  stakeholders:[
    ['ST01','Frontline requesters','High impact / medium influence','Quick reporting; status visibility; assisted channel','Two 30-minute interviews and mobile task test','Validate required fields and confirmation wording'],
    ['ST02','Service coordinator','High impact / high influence','One queue; fewer follow-ups; clear priorities','Process walkthrough and weekly design playback','Own triage rules and daily aged queue review'],
    ['ST03','ICT technicians','High impact / high influence','Useful diagnosis; accountable hand-offs','Resolution workshop and exception testing','Validate routing, evidence and reopen rules'],
    ['ST04','Unit manager and sponsor','High influence / medium impact','Operational continuity; defensible investment','Fortnightly decision brief and gate review','Approve scope, resources and residual risks'],
    ['ST05','Privacy, security and records advisers','High influence / medium impact','Safe data handling; access; record lifecycle','Early assessment workshop and release review','Confirm applicable controls and evidence'],
    ['ST06','Platform owner and external support provider','Medium influence / high impact','Reuse approved tools; support boundaries','Integration discovery and hand-off workshop','Confirm tenancy, licensing, contracts and support'],
    ['ST07','Accessibility and staff representatives','Medium influence / high impact','Accessible reporting; fair workload; safe feedback','Keyboard task test and inclusive change sessions','Challenge barriers and review training options']
  ],
  findings:[
    ['F01','Requester','I send another email because I cannot see whether anyone owns it.','Status visibility and an immediate reference','Simulated interview, not an actual quotation'],
    ['F02','Coordinator','We re-enter the same fault into a spreadsheet, then ask for the missing location.','Structured intake and one queue','Simulated interview'],
    ['F03','Technician','Urgent means something different to every person.','Agreed impact and urgency matrix','Simulated workshop'],
    ['F04','Requester','The ticket was closed, but the printer still did not work.','Resolution evidence and explicit confirmation','Simulated interview'],
    ['F05','Records adviser','A spreadsheet does not explain who changed a status and why.','Event history and controlled records export','Simulated workshop'],
    ['F06','Staff representative','A web form cannot be the only way to get help.','Assisted intake and accessible task testing','Simulated interview']
  ],
  questions:[
    'Walk me through your most recent fault, from detection to confirmation of recovery.',
    'Where do you wait, repeat information or ask another person for an update?',
    'What would make a fault urgent, and what workaround is available?',
    'Who owns each hand-off, and how do you know it has been accepted?',
    'What evidence is needed before closing or reopening a fault?',
    'What information is essential, restricted or unnecessary for this process?',
    'Which accessibility, shift, location or confidence barriers affect reporting?',
    'Which policy, integration and supplier constraints must we validate?',
    'What measure would convince you the new process is better?'
  ],
  metrics:[
    ['M01','Administrative handling time','12 minutes per fault','≤ 6 minutes','Observed active minutes / completed faults; same definition before and after; coordinator; 4-week pilot'],
    ['M02','Submission completeness','36 / 50 = 72%','≥ 95%','Submissions accepted without clarification / all submissions; coordinator; weekly; assisted intake included'],
    ['M03','Status-chasing contacts','22 / 50 = 44%','≤ 20%','Faults with at least one status-only follow-up / all faults; coordinator; weekly'],
    ['M04','Confirmed closure','30 / 50 = 60%','100%','Closed faults with explicit requester confirmation / all closed faults; process owner; weekly'],
    ['M05','Operational guardrail','Not established','No service or accessibility deterioration','Track priority breaches, reopen rate and assisted-channel completion; establish baseline before pilot; sponsor']
  ],
  gaps:[
    ['G01','Email, phone and spreadsheet intake','Incomplete information and duplicate entry','Structured form plus assisted intake in the same queue','F02, F06','R01, R10','M01, M02'],
    ['G02','Unowned spreadsheet rows','Faults wait between teams','Named technician and visible state transitions','F01','R02, R03','M03'],
    ['G03','Priority is self-selected','Unequal treatment and hidden operational risk','Impact and urgency matrix with visible due time','F03','R04','M05'],
    ['G04','Closure by technician alone','Unresolved faults disappear from the backlog','Resolution evidence; requester confirms or rejects','F04','R05, R06','M04'],
    ['G05','Overwritten spreadsheet cells','Weak accountability and unreliable reporting','Append event history; controlled export in target solution','F05','R07, R08','M05'],
    ['G06','Review based on anecdotes','Repeated faults and benefits not evidenced','Queue measures and scheduled trend review','F01, F02','R09','M01, M03'],
    ['G07','Unvalidated platform controls','Privacy, access and retention risks','Agency assessments and release gates before production','F05','R11, R12','M05']
  ],
  requirements:[
    {id:'R01',type:'Functional',priority:'Must',story:'As a requester, I want to submit a structured fault so that the coordinator has enough information to act.',ac:'Given a new request, when title (5–120 characters), unit, category, impact, urgency and description (10–1000 characters) are valid, create a unique sequential reference and Submitted event. Reject blank or out-of-range values without saving.',gap:'G01',tests:'T01, T02, T03',delivery:'Implemented in demo'},
    {id:'R02',type:'Functional',priority:'Must',story:'As a coordinator, I want to assign a technician so that each accepted fault has an accountable owner.',ac:'Given a Submitted fault and the Coordinator demo role, assigning a named technician moves it to Assigned and appends an event. Reject an empty technician or another role. Reassignment after submission is outside this prototype.',gap:'G02',tests:'T04, T05',delivery:'Implemented in demo'},
    {id:'R03',type:'Functional',priority:'Must',story:'As a technician, I want controlled state changes so that progress is meaningful and consistent.',ac:'Only Assigned → In progress and In progress → Awaiting confirmation are permitted for the Technician demo role. Skip transitions are rejected without mutation.',gap:'G02',tests:'T06, T07',delivery:'Implemented in demo'},
    {id:'R04',type:'Business rule',priority:'Must',story:'As a coordinator, I want consistent priority rules so that faults are treated fairly.',ac:'High impact and High urgency gives P1 with 4 elapsed hours; either High gives P2 with 24 hours; otherwise P3 with 72 hours. Due time is created time plus the target and never pauses while awaiting confirmation. These are proposed targets, not QPS SLAs.',gap:'G03',tests:'T08',delivery:'Implemented in demo'},
    {id:'R05',type:'Functional',priority:'Must',story:'As a technician, I want to record what restored service so that the requester can verify the result.',ac:'Resolution requires 10–1000 characters and an In progress fault. Saving moves it to Awaiting confirmation with an event; a shorter note is rejected.',gap:'G04',tests:'T09',delivery:'Implemented in demo'},
    {id:'R06',type:'Functional',priority:'Must',story:'As a requester, I want to confirm or reject a resolution so that a fault closes only when service works.',ac:'Only the Requester demo role can act on Awaiting confirmation. Confirming closes the fault and records closedAt. Rejecting with a reason of 10–1000 characters returns it to In progress, preserves prior events and clears closedAt. No automatic closure.',gap:'G04',tests:'T10, T11',delivery:'Implemented in demo; identity enforcement deferred'},
    {id:'R07',type:'Control',priority:'Must',story:'As a reviewer, I want a time-stamped event history so that hand-offs are explainable.',ac:'Every successful creation and transition appends actor role, event, state and timestamp. Failed actions append nothing. The demo history is locally mutable; a production release needs server-managed identity and tamper-resistant records.',gap:'G05',tests:'T12',delivery:'Demo history implemented; production assurance deferred'},
    {id:'R08',type:'Functional',priority:'Should',story:'As a coordinator, I want a filtered CSV export so that I can review the same queue outside the app.',ac:'Export exactly the filtered records with headers; quote commas, quotes and line breaks; prefix formula-like cells to prevent spreadsheet execution. Display fictional-data and local-storage notices.',gap:'G05',tests:'T13',delivery:'Implemented in demo'},
    {id:'R09',type:'Functional',priority:'Should',story:'As a manager, I want workload and completion measures so that I can identify pressure and trends.',ac:'Display all-record counts for open, overdue, awaiting confirmation and closed faults. Open means every state except Closed; overdue is open and dueAt < demo clock. Search covers reference, title, unit and owner; status filters combine with search.',gap:'G06',tests:'T14, T15',delivery:'Implemented in demo'},
    {id:'R10',type:'Quality',priority:'Must',story:'As a staff member, I want a usable and inclusive service so that reporting does not depend on device or digital confidence.',ac:'Provide labelled fields, keyboard-operable dialogs, visible focus, text status labels, a narrow-screen layout and an assisted-intake SOP. Conduct representative assistive-technology and user testing before release; full WCAG conformance is not claimed.',gap:'G01',tests:'T16, U01',delivery:'Basic UI checks executed; user validation deferred'},
    {id:'R11',type:'Security and privacy',priority:'Must for pilot',story:'As a security and privacy adviser, I want enforced access and assessed data handling so that operational information is protected.',ac:'Before pilot, approve classification, privacy assessment, data location and supplier review; enforce SSO and server-side least privilege including ownership; test cross-user denial, logs and breach response. Role switching is only a demo convenience.',gap:'G07',tests:'U02',delivery:'Production release gate; not implemented'},
    {id:'R12',type:'Records and operations',priority:'Must for pilot',story:'As a records and platform owner, I want approved lifecycle and support controls so that records remain usable and service is recoverable.',ac:'Before pilot, approve the applicable retention schedule without inventing a period; test restore, record export, support ownership, incident runbook and controlled deployment rollback. Keep requirements, decisions and releases versioned.',gap:'G07',tests:'U03',delivery:'Production release gate; not implemented'}
  ],
  dictionary:[
    ['id','System-generated text','RF-1001 onwards; unique within the local demo dataset'],
    ['title / description','Required text','5–120 / 10–1000 characters; synthetic details only'],
    ['unit','Controlled list','Riverbend, Northbank or Lakeside; all fictional'],
    ['category','Controlled list','Device, Access, Application or Network; no credentials'],
    ['impact / urgency','Controlled lists','High or Standard; High impact = multiple staff blocked; High urgency = no practical workaround'],
    ['priority / dueAt','Derived fields','P1/P2/P3 and UTC ISO timestamp; displayed as Australia/Brisbane'],
    ['status / owner','Controlled state / alias','Submitted, Assigned, In progress, Awaiting confirmation, Closed; technician alias'],
    ['resolution / closedAt','Text / optional timestamp','Resolution evidence retained across rejection; closure timestamp only on confirmation'],
    ['events','Ordered event collection','Actor role, action, status, note and UTC time; local demonstration, not immutable audit']
  ],
  risks:[
    ['K01','Operational or personal data entered into public demo','3 × 5 = 15 High','Synthetic-only warning; no attachments; no network submission; reset local data','Project author','1 × 5 = 5 Medium','Restrict the production intake and assess privacy before pilot'],
    ['K02','Demo role switch mistaken for access control','4 × 5 = 20 High','Explicit role simulation label; R11 and cross-user denial test as pilot gate','Security lead','2 × 5 = 10 High','Unaccepted for production; SSO and server enforcement required'],
    ['K03','Staff keep using separate email queues','4 × 3 = 12 High','Champions, assisted intake, clear service channel and daily reconciliation','Process owner','2 × 3 = 6 Medium','Pilot adoption must reach 80% before expansion'],
    ['K04','Wrong priority or unrealistic target','3 × 4 = 12 High','Agree impact definitions; calibrate capacity; review breached high-priority faults daily','Coordinator','2 × 3 = 6 Medium','Sponsor validates targets before pilot'],
    ['K05','Fault marked resolved while service is still unavailable','3 × 4 = 12 High','Evidence plus requester confirmation; rejection returns to active work','ICT lead','1 × 4 = 4 Low','Test T09–T11 and monitor reopen rate'],
    ['K06','Inaccessible interface or exclusion of shift staff','3 × 4 = 12 High','Keyboard checks, assisted intake, recorded training plus captioned materials','Change lead','2 × 3 = 6 Medium','Representative users must pass U01'],
    ['K07','Loss or alteration of records in browser storage','4 × 4 = 16 High','State openly that demo storage is disposable; production repository and restore tests','Platform owner','3 × 4 = 12 High','Unaccepted for production until U03 passes'],
    ['K08','Unsupported tenant, connector cost or data location','3 × 4 = 12 High','Confirm approved platform, licensing, residency, supplier terms and support model','Platform owner','2 × 4 = 8 Medium','No procurement or live tenant assumed'],
    ['K09','Misleading benefit or compliance claims','3 × 4 = 12 High','Label invented baseline, proposed targets, executed checks and outstanding gates','Project author','1 × 4 = 4 Low','Do not present prototype checks as stakeholder sign-off']
  ],
  controls:[
    ['QGEA','Use the current Queensland architecture policy catalogue to assess platform reuse and applicable policies. Confirm applicability with the agency architecture owner.','Architecture decision record; approved platform and integration assessment','R11, R12','S01'],
    ['IS18 current June 2026','The current Information and cyber security policy uses lifecycle risk management and an ISO 27001 based ISMS. Map this project into agency assurance; this demo does not establish compliance.','Classification, access-control test, security assessment and accepted residual risks','R11','S02'],
    ['Information Privacy Act 2009 and QPPs','Use current Queensland Privacy Principles. Minimise personal data and assess collection, use, disclosure and transfers. Complete a privacy assessment before introducing actual staff or applicant data.','Privacy impact assessment, collection notice and breach response decision','R11','S03, S04'],
    ['Public Records Act 2023','Create and manage appropriate records. Validate the applicable Queensland State Archives and agency retention and disposal requirements; no arbitrary retention period is proposed.','Records mapping, authorised retention decision and recoverable export','R07, R12','S05'],
    ['Customer experience and accessibility','QPS references the Queensland Digital Service Standard. Use needs research, clear status, assisted service and accessibility validation as design inputs.','Task observations, inclusive research, U01 and pilot feedback','R10','S06'],
    ['QPS ICT policies and practices','Internal policies were not supplied. Obtain the current authorised security, documentation, release and version-control requirements from accountable owners before implementation.','Agency-specific compliance checklist and release approvals','R11, R12','Role document']
  ],
  options:[
    ['A','Improve the spreadsheet','Low effort; immediate template and ownership rules','Still fragmented; weak automation, permissions and records evidence','Interim fallback only'],
    ['B','Configure an existing approved service platform','Reuse identity, support, record lifecycle and reporting capabilities','Availability, licensing, configuration and integration must be established','Preferred after discovery confirms fit'],
    ['C','Microsoft 365 low-code pilot','Microsoft Lists or SharePoint, Power Apps and controlled Power Automate flows','Item permissions, delegation, connector licensing, audit and records design need validation','Conditional pilot if option B cannot meet needs'],
    ['D','Commission a custom production application','Maximum workflow flexibility','Highest delivery, assurance and ongoing support burden','Do not recommend at this stage']
  ],
  change:[
    ['Discover / week 1','Process owner and BA','Validate baseline and workflow with all shifts; include accessibility and supplier voices','Research notes agreed; scope and outcome definitions approved'],
    ['Design / week 2','BA, platform owner and advisers','Playback requirements; challenge priority rules; assess approved platform reuse','Requirements baseline and privacy, security, records assessments completed'],
    ['Validate / week 3','ICT and representative users','Complete UAT including exceptions, permission denial and restore; train champions','All Must for pilot requirements passed and residual risks accepted'],
    ['Pilot / weeks 4–7','Process owner and change lead','Small volunteer unit; 20-minute role-based sessions; captioned guide; assisted channel; daily triage','80% channel adoption; no critical service, privacy or accessibility issue'],
    ['Review / week 8','Sponsor and BA','Compare like-for-like baseline; inspect incidents and feedback; decide expand, revise or stop','Written review and sponsor decision; no automatic expansion']
  ],
  uat:[
    ['U01','Representative requesters including an assistive-technology user','Complete submit, follow status and confirm or reject across mobile, keyboard and screen reader; assisted request enters same queue','No critical task barrier; feedback resolved','Not executed; representative users required','R10'],
    ['U02','Security and privacy advisers','Verify SSO; requester A cannot view or alter requester B records; technician access matches assignment; evaluate collection, logs and breach response','No unauthorised access; signed assessment and residual-risk decision','Not executable on browser-only demo','R11'],
    ['U03','Records and platform owners','Apply approved retention rules; export records; restore backup; deploy and roll back; verify incident hand-off','Evidence meets approved records, recovery and support criteria','Not executable until target platform exists','R12'],
    ['U04','Process owner and nominated business testers','Repeat T01–T16 in the target platform and exercise interruption, duplicate reports and supplier hand-off','All Must requirements pass; no open Severity 1 or 2 defects','Planned; no business acceptance claimed','R01–R10']
  ],
  capabilities:[
    ['1','Coordinate and improve IT systems and BA','F01–F06; G01–G07; R01–R12; working prototype','Translate fragmented work into a controlled service workflow'],
    ['2','Develop and support change management','Change plan; training guide; pilot and rollback criteria','Include shift staff, champions, assisted reporting and support ownership'],
    ['3','Determine requirements within legislative, IT and customer frameworks','BRD; acceptance criteria; data dictionary; governance mapping','Identify policy constraints and validate internal rules with owners'],
    ['4','Adhere to IT policies, security, documentation and version control','R11–R12; risk register; decision log; document control','Make unimplemented assurance controls explicit release gates'],
    ['5','Advise management on improvement, innovation and risk','Two-page briefing; options appraisal; benefit model','Recommend reuse before custom build and avoid overstated savings'],
    ['6','Analyse, document, develop, test, deliver, implement and review','Process maps; traceability; demo; executed tests; rollout and PIR plan','Separate completed prototype work from proposed organisational rollout'],
    ['7','Engage operational and business stakeholders','Stakeholder map; questions; engagement plan; validation backlog','Explain the engagement approach; interviews in this project are simulated'],
    ['8','Identify improvements and current/future gaps','Editable swimlanes; gap analysis; linked measures','Trace each change to a bottleneck, requirement and test'],
    ['9','Contribute to an ethical, inclusive and improving team','Working agreement; accessible service; feedback and learning loop','Invite challenge, share knowledge and avoid inventing actual leadership experience']
  ],
  decisions:[
    ['D01','Use routine ICT faults in a fictional licensing unit','Align to system operationalisation while excluding operational licensing decisions','Project author; 9 Oct 2026'],
    ['D02','Demonstrate local browser state only','Provide a complete low-friction interview workflow with synthetic data; no agency integration','Project author; 9 Oct 2026'],
    ['D03','Require confirmation and allow rejection','Address false closure risk; no automatic closure timeout','Project author; 9 Oct 2026'],
    ['D04','Prefer approved platform reuse','Limit bespoke support cost; conditional M365 pilot if existing platform is unsuitable','Proposed; sponsor validation pending'],
    ['D05','Use fixed demo clock initially','Keep seed queue measures reproducible; advance the clock explicitly in the demo','Project author; 9 Oct 2026']
  ],
  sources:[
    ['S01','QGEA policy catalogue','https://www.forgov.qld.gov.au/information-technology/queensland-government-enterprise-architecture-qgea/qgea-directions-and-guidance/qgea-policies-standards-and-guidelines','Official framework catalogue; confirm applicability at design gate'],
    ['S02','Information and cyber security policy IS18','https://www.forgov.qld.gov.au/information-technology/queensland-government-enterprise-architecture-qgea/qgea-directions-and-guidance/qgea-policies-standards-and-guidelines/information-security-policy-is18','Current v10.0.0; effective June 2026; checked 9 October 2026'],
    ['S03','OIC privacy reform information','https://www.oic.qld.gov.au/government/ipola','QPP reforms commenced 1 July 2025; checked 9 October 2026'],
    ['S04','OIC privacy impact assessments','https://www.oic.qld.gov.au/government/privacy/privacy-impact-assessments','Current privacy assessment guidance; checked 9 October 2026'],
    ['S05','Public Records Act 2023','https://www.legislation.qld.gov.au/view/html/inforce/current/act-2023-033','Official Queensland legislation; current version checked 9 October 2026'],
    ['S06','QPS Digital Service Standard','https://www.police.qld.gov.au/help/digital-service-standard','Official QPS customer experience context; checked 9 October 2026']
  ]
};
