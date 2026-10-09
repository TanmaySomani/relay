from pathlib import Path
from html import escape
from lxml import html,etree
import json,math,re
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,CondPageBreak,Table,TableStyle,KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.graphics.shapes import Drawing,Rect,PolyLine,Polygon,String
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
FONTROOT=Path("/Users/tanmaysomani/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/pdfjs-dist/standard_fonts")
pdfmetrics.registerFont(TTFont("RelaySans",str(FONTROOT/"LiberationSans-Regular.ttf")))
pdfmetrics.registerFont(TTFont("RelaySans-Bold",str(FONTROOT/"LiberationSans-Bold.ttf")))
pdfmetrics.registerFontFamily("RelaySans",normal="RelaySans",bold="RelaySans-Bold",italic="RelaySans",boldItalic="RelaySans-Bold")
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'dist/downloads';D=json.loads((ROOT/'evidence/project-data.json').read_text());SECTIONS=json.loads((ROOT/'evidence/sections.json').read_text());W=A4[0]-100
S=getSampleStyleSheet();S.add(ParagraphStyle(name='BodyCustom',fontName='RelaySans',fontSize=9.7,leading=14.2,spaceAfter=9,textColor=colors.HexColor('#223343')));S.add(ParagraphStyle(name='MainTitle',fontName='RelaySans-Bold',fontSize=28,leading=33,spaceAfter=18,textColor=colors.black));S.add(ParagraphStyle(name='SectionTitle',fontName='RelaySans-Bold',fontSize=22,leading=28,spaceAfter=18,textColor=colors.black,keepWithNext=True));S.add(ParagraphStyle(name='SubTitle',fontName='RelaySans-Bold',fontSize=12.5,leading=16,spaceBefore=14,spaceAfter=9,textColor=colors.black,keepWithNext=True));S.add(ParagraphStyle(name='SmallCustom',fontName='RelaySans',fontSize=8.3,leading=11.5,spaceAfter=8,textColor=colors.HexColor('#526170')));S.add(ParagraphStyle(name='CellCustom',fontName='RelaySans',fontSize=8,leading=11,textColor=colors.HexColor('#223343')));S.add(ParagraphStyle(name='HeaderCustom',parent=S['CellCustom'],fontName='RelaySans-Bold',textColor=colors.white))
S.add(ParagraphStyle(name='MetaKeep',parent=S['SmallCustom'],keepWithNext=True))
def clean(s):
    for a,b in [('→',' -> '),('≥','>='),('≤','<='),('–','-'),('—','-'),('×','x'),('’',"'"),('“','"'),('”','"'),('•','-'),('\u00a0',' ')]:s=s.replace(a,b)
    return s

def para(s,style='BodyCustom'):return Paragraph(escape(clean(s)).replace('\n','<br/>'),S[style])
def markup(s,style='BodyCustom'):return Paragraph(clean(s),S[style])
def title(s):return para(s,'SubTitle')
def footer(canvas,doc):
    canvas.saveState();canvas.setStrokeColor(colors.HexColor('#dbe2eb'));canvas.line(50,45,A4[0]-50,45);canvas.setFont('RelaySans',8);canvas.setFillColor(colors.HexColor('#526170'));canvas.drawString(50,30,'Relay | Fictional independent BA portfolio | 9 October 2026');canvas.drawRightString(A4[0]-50,30,str(doc.page));canvas.restoreState()
def document(name,story):
    doc=SimpleDocTemplate(str(OUT/name),pagesize=A4,rightMargin=50,leftMargin=50,topMargin=48,bottomMargin=62,title=name.replace('-',' ').replace('.pdf',''),author='Independent portfolio project author');doc.build(list(story),onFirstPage=footer,onLaterPages=footer)
def tab(headers,rows,widths=None):
    n=len(headers);widths=widths or [W/n]*n;data=[[para(str(x),'HeaderCustom') for x in headers]]+[[para(str(x),'CellCustom') for x in row] for row in rows];t=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT');t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#16395f')),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#d9d9d9')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f6f8fc')])]));return t

def diagram(filename):
    ns={'s':'http://www.w3.org/2000/svg'};root=etree.parse(str(OUT/filename)).getroot();dw,dh=float(root.get('width')),float(root.get('height'));d=Drawing(dw,dh)
    for el in root:
        kind=etree.QName(el).localname
        if kind=='rect':d.add(Rect(float(el.get('x',0)),dh-float(el.get('y',0))-float(el.get('height')),float(el.get('width')),float(el.get('height')),rx=float(el.get('rx',0)),fillColor=colors.toColor(el.get('fill','#ffffff')),strokeColor=colors.toColor(el.get('stroke','#ffffff')),strokeWidth=float(el.get('stroke-width',1))))
        elif kind=='polyline':
            coords=[float(x) for x in re.split('[ ,]',el.get('points')) if x];coords=[(v if i%2==0 else dh-v) for i,v in enumerate(coords)];d.add(PolyLine(coords,strokeColor=colors.HexColor('#47648a'),strokeWidth=2));x,y=coords[-2:];px,py=coords[-4:-2];angle=math.atan2(y-py,x-px);a=8;d.add(Polygon([x,y,x-a*math.cos(angle)-a*.5*math.sin(angle),y-a*math.sin(angle)+a*.5*math.cos(angle),x-a*math.cos(angle)+a*.5*math.sin(angle),y-a*math.sin(angle)-a*.5*math.cos(angle)],fillColor=colors.HexColor('#47648a'),strokeColor=None))
        elif kind=='text':d.add(String(float(el.get('x')),dh-float(el.get('y')),clean(''.join(el.itertext())),fontName='RelaySans-Bold' if el.get('font-weight')=='bold' else 'RelaySans',fontSize=float(el.get('font-size',14)),fillColor=colors.toColor(el.get('fill','#132333')),textAnchor=el.get('text-anchor','start')))
    scale=W/dw;d.scale(scale,scale);d.width=dw*scale;d.height=dh*scale;return d

def textof(el):return ' '.join(' '.join(el.itertext()).split())
def convert_table(el):
    hs=[textof(x) for x in el.xpath('.//thead/tr/th')];rs=[[textof(x) for x in row.xpath('./td')] for row in el.xpath('.//tbody/tr')]
    if not hs:return []
    # Narrative-heavy matrices become labelled records to keep the PDF legible.
    if len(hs)>=5 and max((sum(map(len,r)) for r in rs),default=0)>240:
        out=[]
        for row in rs:
            block=[title(' | '.join(row[:2]))]
            for label,value in zip(hs[2:],row[2:]):block.append(markup('<b>'+escape(label)+':</b> '+escape(clean(value)),'BodyCustom'))
            out.append(KeepTogether(block))
        return out
    if len(hs)==6:widths=[W*.08,W*.16,W*.16,W*.20,W*.21,W*.19]
    elif len(hs)==7:widths=[W*.06,W*.15,W*.18,W*.24,W*.10,W*.15,W*.12]
    elif len(hs)==5:widths=[W*.12,W*.12,W*.20,W*.20,W*.36]
    elif len(hs)==3:widths=[W*.22,W*.24,W*.54]
    elif len(hs)==4:widths=[W*.16,W*.22,W*.36,W*.26]
    else:widths=None
    return [tab(hs,rs,widths),Spacer(1,12)]

def convert(el):
    tag=el.tag;out=[]
    if tag=='p':
        if 'actions' in el.get('class','') or (el.xpath('.//a') and all(x.get('href','').startswith('downloads/') for x in el.xpath('.//a'))):return []
        text=textof(el)
        if text:
            sources=el.xpath('.//a[starts-with(@href, "https://")]')
            if sources:
                links=' '.join('<link href="'+a.get('href')+'" color="#174acb">Open official source</link>' for a in sources)
                out=[markup(escape(clean(text))+'<br/>'+links)]
            else:out=[para(text)]
    elif tag in ['h3','h4']:out=[title(textof(el))]
    elif tag in ['ul','ol']:
        for i,li in enumerate(el.xpath('./li')):out.append(para(('- ' if tag=='ul' else str(i+1)+'. ')+textof(li)))
    elif tag=='article':
        badge=el.xpath('./span');out=[Spacer(1,8),para(textof(badge[0]),'SmallCustom')] if badge else []
        for child in el:
            if child.tag!='span':out.extend(convert(child))
    elif tag=='div' and 'table-scroll' in el.get('class',''):out=convert_table(el.xpath('./table')[0])
    elif tag=='img':out=[diagram(Path(el.get('src')).name),Spacer(1,14)]
    elif tag=='div' and ('actions' in el.get('class','') or 'diagram-links' in el.get('class','')):return []
    else:
        for child in el:out.extend(convert(child))
    return out
summary=[para('Relay service improvement case study','MainTitle'),para('One page summary | Independent portfolio exercise | Version 1.0','SmallCustom'),para('A complete BA case study for improving routine IT fault handling in a fictional licensing support unit.'),title('Problem and context'),para('Email, phone and spreadsheet intake lead to missing information, unclear ownership and closure without verified restoration. The scenario reflects system operationalisation and public-sector service needs. It contains no real police, licensing, staff or applicant data.'),title('Approach'),para('Model seven stakeholder groups and six simulated findings; map current and future hand-offs; analyse seven gaps; define 12 prioritised requirements with acceptance criteria; map risks and governance; build and test a working service workflow; plan a controlled pilot and benefits review.'),title('What is complete'),para('A working browser prototype with structured intake, priority rules, assignment, controlled state changes, rejection and confirmed closure, searchable queue, CSV export and local event history. Fifteen automated domain checks and one browser integration review passed. Editable maps, requirements, test cases, controls, change plan and management briefing accompany the prototype.'),title('Targets and evidence boundaries'),para('Synthetic baseline: 50 faults, 12 minutes active handling per fault, 72% complete intake and 60% confirmed closure. Proposed targets: <=6 minutes handling, >=95% completeness and 100% confirmed closure. Potential capacity: 5 hours per month at the assumed volume. No real benefits, stakeholder consultation, business UAT or production compliance are claimed.'),title('Recommendation and release gates'),para('Assess an existing approved service platform first. Consider an approved Microsoft 365 pilot only if required. Validate identity and permissions, privacy, classification, records, restore and support before live data. A four-week pilot and sponsor review determine whether to expand.'),para('Tools: stakeholder analysis, swimlanes, gap matrix, BRD, stories, traceability, JavaScript prototype, versioned evidence and Microsoft 365 delivery blueprint. Role alignment: all nine QPS AO5 capabilities.','SmallCustom')]
document('Relay-One-Page-Summary.pdf',summary)
brief1=[para('IT fault handling improvement','MainTitle'),para('Management briefing | Page 1 of 2 | Fictional portfolio scenario','SmallCustom'),para('To: Unit Manager | From: portfolio project author | Date: 9 October 2026'),title('Decision sought'),para('Approve a short discovery and pilot design to validate the service problem, platform fit and assurance requirements. This is a simulated decision request; no real budget or organisational authority is assumed.'),title('Recommendation'),para('Assess the existing approved service management platform first and configure it if fit for purpose. If it cannot meet the requirements, design a small Microsoft 365 pilot in an approved tenant, conditional on privacy, security and records gates. Use the web prototype to test workflow, not as a production solution.'),title('Issue and evidence'),para('The fictional unit tracks faults through emails and spreadsheets, creating duplicate handling, unclear ownership and unconfirmed closure. Six simulated findings and an invented sample of 50 faults support the exercise. Actual interviews, observations and service data must validate the problem and baseline before investment.'),title('Options'),tab(['Option','Benefits','Trade-offs','Assessment'],[['A: improve spreadsheet','Low effort; clearer fields and owners','Fragmentation and weak control evidence persist','Interim fallback'],['B: approved service platform','Reuse identity, support and records capabilities','Availability, licences and fit need confirmation','Preferred'],['C: Microsoft 365 low-code','Flexible intake and workflow; familiar suite','Permissions, flows, records and licensing need assurance','Conditional pilot'],['D: custom production app','Maximum workflow flexibility','Highest build, assurance and support burden','Not recommended']], [W*.21,W*.26,W*.33,W*.20])]
brief2=[para('Benefits risks and next steps','SectionTitle'),para('Management briefing | Page 2 of 2 | Fictional portfolio scenario','SmallCustom'),title('Indicative benefit and effort'),para('Assuming 50 faults per month and active administration reduced from 12 to 6 minutes: 50 x 6 / 60 = 5 staff hours per month. At an assumed A$65 loaded hourly rate, potential capacity value is A$325 per month or A$3,900 per year. This is not cash savings. At 25-100 faults per month, the same assumption releases 2.5-10 hours. Demand and improvement remain unverified.'),para('Allow an indicative 8-12 person-days for discovery, configuration, assessment, testing and training, excluding licensing, integrations and remediation. At 7.6 hours per day and A$65 per hour, effort is A$3,952-A$5,928. This estimate is for comparison, not a quote or an approved business case. These assumptions do not yet support custom development.'),title('Primary risks and conditions'),para('Inadequate access control and uncontrolled records are unacceptable for production in the current browser demo. A live pilot requires assessed classification, approved data handling, enforced SSO and ownership permissions, protected records, authorised retention and tested restore. Confirm platform location, licensing, supplier terms, support and incident channels.'),para('Mitigate adoption and accessibility risks with shift-friendly training, champions, assisted reporting and representative task tests. Agree priority definitions and service targets with the coordinator and sponsor before live use.'),title('Proposed sequence and decision gates'),para('Weeks 1-2: validate the baseline, platform fit and requirements; agree assurance and measures. Week 3: execute target-platform UAT, access-denial and restore tests; train champions. Weeks 4-7: controlled pilot with daily queue review. Week 8: sponsor reviews performance, incidents, adoption and feedback and decides expand, revise or stop.'),title('Measures and stop criteria'),para('Track active handling time, submission completeness, status-chasing contacts, confirmed closure and service/accessibility guardrails. No open Severity 1 or 2 defects or unaccepted High risks at pilot entry. Pause if access failures block critical work, a serious privacy/security event occurs or records cannot be recovered; use the approved fallback and reconcile changes before restart.'),para('Supporting evidence: G01-G07; R01-R12; K01-K09; executed T01-T16; proposed U01-U04. Organisational UAT, consultation, rollout and benefits realisation have not occurred.','SmallCustom')]
document('Relay-Management-Brief.pdf',brief1+[PageBreak()]+brief2)
pack=summary.copy()+[PageBreak()]
for id,name,content in SECTIONS:
    pack += [CondPageBreak(220),Spacer(1,18),para(name,'SectionTitle'),para('Version 1.0 | 9 October 2026 | Fictional independent exercise','MetaKeep')]
    root=html.fragment_fromstring(content,create_parent='div')
    for child in root:pack.extend(convert(child))
pack += [PageBreak(),para('Detailed test procedure appendix','SectionTitle'),para('Self-executed prototype checks on 9 October 2026. The result register and runnable test source are included in the editable evidence ZIP.','SmallCustom')]
steps=json.loads((ROOT/'evidence/test-case-steps.json').read_text());results=json.loads((ROOT/'evidence/test-results.json').read_text())['results']
for t in results:
    pre,action,expected=steps[t['id']];pack.append(KeepTogether([title(t['id']+' | '+t['name']),markup('<b>Requirements:</b> '+t['requirements']+' | <b>Result:</b> '+t['result']),markup('<b>Preconditions:</b> '+escape(pre)),markup('<b>Steps:</b> '+escape(action)),markup('<b>Expected and observed:</b> '+escape(expected))]))
document('Relay-Portfolio-Pack.pdf',pack)
from pypdf import PdfReader
for name in ['Relay-One-Page-Summary.pdf','Relay-Management-Brief.pdf','Relay-Portfolio-Pack.pdf']:
    r=PdfReader(OUT/name);print(json.dumps({'file':name,'pages':len(r.pages),'bytes':(OUT/name).stat().st_size}))
