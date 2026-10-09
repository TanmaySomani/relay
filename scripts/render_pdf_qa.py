from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
import subprocess,os
ROOT=Path(__file__).resolve().parents[1];env=os.environ.copy();env['FONTCONFIG_FILE']=str(ROOT/'tmp/pdf-qa/fonts.conf');env['FONTCONFIG_PATH']=str(ROOT/'tmp/pdf-qa')
cmd='/Users/tanmaysomani/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm'
for name,prefix in [('Relay-Portfolio-Pack.pdf','pack'),('Relay-One-Page-Summary.pdf','summary'),('Relay-Management-Brief.pdf','brief')]:
    result=subprocess.run([cmd,'-r','90','-png',str(ROOT/'dist/downloads'/name),str(ROOT/'tmp/pdf-qa'/prefix)],env=env,capture_output=True,timeout=90);print(prefix,result.returncode,result.stderr.decode()[:200])
from pypdf import PdfReader
paths=sorted((ROOT/'tmp/pdf-qa').glob('pack-*.png'))[:len(PdfReader(ROOT/'dist/downloads/Relay-Portfolio-Pack.pdf').pages)];w,h=300,440;sheet=Image.new('RGB',(w*5,h*7),'#dce2eb');d=ImageDraw.Draw(sheet)
for i,p in enumerate(paths):sheet.paste(ImageOps.contain(Image.open(p),(w-12,h-30)),((i%5)*w+6,(i//5)*h+23));d.text(((i%5)*w+8,(i//5)*h+5),p.stem,fill='black')
sheet.save(ROOT/'tmp/pdf-qa/contact-sheet.jpg');print('Rendered',len(paths),'pack pages')
