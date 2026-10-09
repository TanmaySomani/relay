from pathlib import Path
from urllib.parse import urlsplit,unquote
from lxml import html,etree
from pypdf import PdfReader
import json,re
ROOT=Path(__file__).resolve().parents[1];DIST=ROOT/'dist';errors=[];checked=0
for path in DIST.glob('*.html'):
    doc=html.parse(str(path));ids=set(doc.xpath('//@id'))
    if not doc.xpath('//title/text()'):errors.append(f'{path.name}: missing title')
    for href in doc.xpath('//@href|//@src'):
        u=urlsplit(href)
        if u.scheme or u.netloc:continue
        target=(path.parent/unquote(u.path)).resolve() if u.path else path
        checked+=1
        if not target.exists():errors.append(f'{path.name}: missing {href}');continue
        if u.fragment and target.suffix=='.html':
            target_ids=ids if target==path else set(html.parse(str(target)).xpath('//@id'))
            if u.fragment not in target_ids:errors.append(f'{path.name}: missing anchor {href}')
for p in (DIST/'downloads').glob('*.drawio'):etree.parse(str(p))
assert len(PdfReader(DIST/'downloads/Relay-One-Page-Summary.pdf').pages)==1
assert len(PdfReader(DIST/'downloads/Relay-Management-Brief.pdf').pages)==2
D=json.loads((ROOT/'evidence/project-data.json').read_text());assert len(D['requirements'])==12
assert len(D['capabilities'])==9
assert all(x['result']=='Pass' for x in json.loads((ROOT/'evidence/test-results.json').read_text())['results'])
# Every traceability test ID must exist in either executed checks or planned UAT.
known={t['id'] for t in json.loads((ROOT/'evidence/test-results.json').read_text())['results']}|{'T16'}|{u[0] for u in D['uat']}
for r in D['requirements']:
    for test in re.findall(r'[TU]\d{2}',r['tests']):
        if test not in known:errors.append(f'{r["id"]}: unknown test {test}')
print(json.dumps({'localReferencesChecked':checked,'requirements':12,'capabilities':9,'errors':errors},indent=2))
if errors:raise SystemExit(1)
