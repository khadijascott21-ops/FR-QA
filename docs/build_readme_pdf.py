"""Convert the complete project README into a formatted PDF."""
from pathlib import Path
from html import escape
import re
import textwrap

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, Preformatted
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output'/'pdf'
OUT.mkdir(parents=True,exist_ok=True)
raw=(ROOT/'README.md').read_text(encoding='utf-8')
# Normalize decorative punctuation/icons for dependable PDF font rendering.
# The textual status labels and assessment content remain intact.
def normalize(t):
    for a,b in {'\u2014':'-','\u2013':'-','\u2011':'-','\u2019':"'",'\u2018':"'",'\u201c':'"','\u201d':'"','✅':'','✏':'','\ufe0f':'','💡':'','🚀':''}.items():
        t=t.replace(a,b)
    return t

pdfmetrics.registerFont(TTFont('DocArial','C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('DocArial-Bold','C:/Windows/Fonts/arialbd.ttf'))
pdfmetrics.registerFont(TTFont('DocArial-Italic','C:/Windows/Fonts/ariali.ttf'))
pdfmetrics.registerFont(TTFont('DocMono','C:/Windows/Fonts/consola.ttf'))
pdfmetrics.registerFontFamily('DocArial',normal='DocArial',bold='DocArial-Bold',italic='DocArial-Italic',boldItalic='DocArial-Bold')
styles=getSampleStyleSheet()
ink=colors.HexColor('#173b57')
styles.add(ParagraphStyle(name='Body',fontName='DocArial',fontSize=9.8,leading=14,spaceAfter=9,splitLongWords=1))
styles.add(ParagraphStyle(name='DocTitle',parent=styles['Body'],fontName='DocArial-Bold',fontSize=21,leading=26,textColor=ink,spaceAfter=20,keepWithNext=True))
styles.add(ParagraphStyle(name='Section',parent=styles['Body'],fontName='DocArial-Bold',fontSize=15,leading=19,textColor=ink,spaceBefore=12,spaceAfter=11,keepWithNext=True))
styles.add(ParagraphStyle(name='Subsection',parent=styles['Body'],fontName='DocArial-Bold',fontSize=11.5,leading=15,textColor=ink,spaceBefore=9,spaceAfter=8,keepWithNext=True))
styles.add(ParagraphStyle(name='List',parent=styles['Body'],leftIndent=14,firstLineIndent=-12,spaceAfter=5))
styles.add(ParagraphStyle(name='Quote',parent=styles['Body'],leftIndent=12,borderColor=colors.HexColor('#90aec3'),borderWidth=1,borderPadding=8,spaceBefore=5,spaceAfter=13))
styles.add(ParagraphStyle(name='Cell',parent=styles['Body'],fontSize=8.7,leading=12,spaceAfter=0))
styles.add(ParagraphStyle(name='CellHead',parent=styles['Cell'],fontName='DocArial-Bold',textColor=ink))
styles.add(ParagraphStyle(name='DocCode',fontName='DocMono',fontSize=8.1,leading=11,backColor=colors.HexColor('#f1f5f8'),borderPadding=10,spaceBefore=6,spaceAfter=15))

def inline(t):
    code=[]
    def protect(match):
        code.append(match.group(1))
        return f'CODETOKEN{len(code)-1}ENDTOKEN'
    t=re.sub(r'`([^`]+)`',protect,t)
    t=escape(t)
    t=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',t)
    t=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',t)
    t=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2" color="#245d85">\1</a>',t)
    for n,value in enumerate(code):
        t=t.replace(f'CODETOKEN{n}ENDTOKEN','<font name="DocMono" size="8.3">'+escape(value)+'</font>')
    return t

def para(text,style='Body'):
    return Paragraph(inline(text),styles[style])

anchors={int(m.group(1)):m.group(2) for m in re.finditer(r'(?m)^(\d+)\. \[[^\]]+\]\(#([^)]+)\)',raw)}
lines=normalize(raw).splitlines()
story=[]
literal_code=[]
table_count=0
i=0
while i<len(lines):
    line=lines[i]
    if not line.strip():
        i+=1;continue
    if line.startswith('```'):
        code=[];i+=1
        while i<len(lines) and not lines[i].startswith('```'):
            code.append(lines[i]);i+=1
        literal_code.extend(code)
        # Wrap long code lines without altering their characters.
        wrapped=[]
        for c in code:
            wrapped.extend(textwrap.wrap(c,width=99,expand_tabs=False,replace_whitespace=False,drop_whitespace=False) or [''])
        story.append(Preformatted('\n'.join(wrapped),styles['DocCode']))
        i+=1;continue
    if line.startswith('|'):
        rows=[]
        while i<len(lines) and lines[i].startswith('|'):
            row=[c.strip() for c in lines[i].strip().strip('|').split('|')]
            if not all(re.fullmatch(r':?-+:?',c) for c in row): rows.append(row)
            i+=1
        if len(rows[0])==3:
            if rows[0][0]=='ID': widths=[38,155,319]
            elif rows[0][1]=='Status': widths=[183,108,221]
            else: widths=[108,50,354]
        elif rows[0][0]=='File':
            widths=[132,380] if rows[0][1]=='Responsibility' else [235,277]
        elif rows[0][0]=='ID': widths=[43,469]
        elif rows[0][0]=='Field': widths=[125,387]
        elif rows[0][0]=='Tool': widths=[125,387]
        else: widths=[256,256]
        data=[[para(c,'CellHead' if j==0 else 'Cell') for c in row] for j,row in enumerate(rows)]
        t=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
        t.setStyle(TableStyle([
            ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dceaf3')),
            ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f3f6f9')]),
            ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
            ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
            ('LINEBELOW',(0,0),(-1,0),0.5,colors.HexColor('#9cb7cb')),
        ]))
        story.extend([t,Spacer(1,12)]);table_count+=1;continue
    heading=re.match(r'^(#{1,3})\s+(.+)',line)
    if heading:
        hashes,title=heading.groups()
        if len(hashes)==1: story.append(para(title,'DocTitle'))
        else:
            style='Section' if len(hashes)==2 else 'Subsection'
            tag=''
            if len(hashes)==2:
                number=re.match(r'^(\d+)\.',title)
                if number and int(number.group(1)) in anchors:
                    tag=f'<a name="{anchors[int(number.group(1))]}"/>'
            story.append(Paragraph(tag+inline(title),styles[style]))
        i+=1;continue
    if line.strip()=='---':
        story.extend([Spacer(1,4),HRFlowable(width='100%',thickness=.5,color=colors.HexColor('#dce3e9'),spaceAfter=8)])
        i+=1;continue
    if line.startswith('>'):
        block=[]
        while i<len(lines) and lines[i].startswith('>'):
            block.append(lines[i].lstrip('> ').strip());i+=1
        story.append(para(' '.join(block),'Quote'));continue
    list_match=re.match(r'^(?:- |\d+\. )',line)
    if list_match:
        block=[line];i+=1
        while i<len(lines) and lines[i].startswith('   '):
            block.append(lines[i].strip());i+=1
        text=' '.join(block)
        if text.startswith('- '): text='- '+text[2:]
        story.append(para(text,'List'));continue
    block=[line];i+=1
    while i<len(lines) and lines[i].strip() and not re.match(r'^(?:#|\||```|>|---|- |\d+\. )',lines[i]):
        block.append(lines[i]);i+=1
    story.append(para(' '.join(block)))

def footer(canvas,doc):
    canvas.setStrokeColor(colors.HexColor('#dce3e9'));canvas.line(42,40,554,40)
    canvas.setFont('DocArial',8);canvas.setFillColor(colors.HexColor('#526779'))
    canvas.drawString(42,27,'QA Engineer I | Technical Assessment | README')
    canvas.drawRightString(554,27,str(doc.page))

pdf=OUT/'readMe.pdf'
SimpleDocTemplate(str(pdf),pagesize=(596,842),leftMargin=42,rightMargin=42,topMargin=42,bottomMargin=54,title='QA Engineer I - Technical Assessment',author='').build(story,onFirstPage=footer,onLaterPages=footer)
pages=PdfReader(str(pdf)).pages
text='\n'.join(p.extract_text() or '' for p in pages)
for n in range(1,23):
    assert re.search(r'\bR'+str(n)+r'\b',text),n
assert len(anchors)==9
assert table_count==10,table_count
assert 'No. Everything you need is already included.' in text
assert 'Good luck - we look forward to reviewing your work!' in text
# Confirm that every textual token from the README appears, including examples
# inside code blocks. Markdown syntax and decorative icons are ignored.
readable=normalize(raw)
readable=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'\1',readable)
codeblocks=re.findall(r'```[^\n]*\n(.*?)```',readable,re.S)
readable=re.sub(r'```[^\n]*\n.*?```','',readable,flags=re.S)+'\n'+'\n'.join(codeblocks)
words=set(re.findall(r'[A-Za-z][A-Za-z0-9_]{2,}',readable))
pdfwords=set(re.findall(r'[A-Za-z][A-Za-z0-9_]{2,}',text))
missing=words-pdfwords
assert not missing,sorted(missing)
print(f'Created {pdf}\nPages: {len(pages)}; tables: {table_count}; all R1-R22 and README text tokens verified.')
