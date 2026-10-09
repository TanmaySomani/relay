from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
ROOT=Path(__file__).resolve().parents[1];out=ROOT/'dist/downloads/Relay-Evidence-and-Source.zip'
with ZipFile(out,'w',ZIP_DEFLATED) as z:
    for name in ['README.md','streamlit_app.py','relay_core.py','requirements.txt','.gitignore','.streamlit/config.toml']:
        p=ROOT/name
        if p.exists():z.write(p,name)
    for directory in ['tests','scripts','evidence']:
        for p in (ROOT/directory).rglob('*'):
            if p.is_file() and p.suffix!='.jpg' and '__pycache__' not in str(p):z.write(p,p.relative_to(ROOT))
    for p in (ROOT/'dist').rglob('*'):
        if p.is_file() and p!=out:z.write(p,Path('dist')/p.relative_to(ROOT/'dist'))
print(out)
