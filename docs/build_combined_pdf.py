"""Create New.pdf from the combined cases printed in the project discussion."""
from pathlib import Path
from html import escape
import re

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output'/'pdf'
source=(OUT/'New.md').read_text(encoding='utf-8')
styles=getSampleStyleSheet()
ink=colors.HexColor('#173b57')
styles['Title'].textColor=ink
styles.add(ParagraphStyle(name='CaseTitle',fontName='Helvetica-Bold',fontSize=14,leading=18,textColor=ink,spaceAfter=13))
styles.add(ParagraphStyle(name='Field',fontName='Helvetica',fontSize=9.6,leading=13,spaceAfter=7))
styles.add(ParagraphStyle(name='Step',parent=styles['Field'],leftIndent=13,firstLineIndent=-11,spaceAfter=5))
styles.add(ParagraphStyle(name='Cell',fontName='Helvetica',fontSize=9,leading=12))
styles.add(ParagraphStyle(name='CellHead',parent=styles['Cell'],fontName='Helvetica-Bold',textColor=ink))
styles.add(ParagraphStyle(name='Note',fontName='Helvetica',fontSize=9.5,leading=14,textColor=colors.HexColor('#425466'),spaceAfter=12))

def p(text,style='Field'):
    return Paragraph(escape(text),styles[style])

def table(lines):
    rows=[]
    for line in lines:
        cells=[c.strip() for c in line.strip().strip('|').split('|')]
        if all(re.fullmatch(r':?-+:?',c) for c in cells): continue
        rows.append(cells)
    count=len(rows[0])
    if count==2:
        widths=[125,387] if rows[0][0]=='Requirement' else [240,272]
    elif count==3:
        if rows[0][0]=='Entered text': widths=[105,135,272]
        elif rows[0][0]=='Situation': widths=[134,110,268]
        else: widths=[185,165,162]
    elif count==4: widths=[85,118,145,164]
    else: raise ValueError(count)
    data=[[p(c,'CellHead' if i==0 else 'Cell') for c in row] for i,row in enumerate(rows)]
    result=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
    result.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dceaf3')),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f2f6f9')]),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
        ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
        ('LINEBELOW',(0,0),(-1,0),0.5,colors.HexColor('#9cb7cb')),
    ]))
    return result

story=[p('Currency Converter','Title'),p('Combined test cases | R1-R22','CaseTitle'),Spacer(1,16)]
story.extend(p(t,'Note') for t in [
    '22 combined test designs using the required individual test-case template.',
    'Each test-data row is a separate execution. The C in each ID identifies a combined case. All cases are drafts and have not been executed.',
    'Controlled-result cases require a fixture that exercises the actual assessment path. TC-R22-C02 remains dependent on PD review of field-correctness expectations.',
    'This PDF reproduces the combined test cases and requirement mapping from the project discussion.',
    'OpenAI Codex assisted with test design and PDF preparation.',
])
story.append(PageBreak())

parts=re.split(r'(?m)^### ',source)[1:]
assert len(parts)==22
ids=[]
for part in parts:
    if '\n## Requirement mapping' in part:
        part=part.split('\n## Requirement mapping')[0]
    lines=part.strip().splitlines()
    ids.append(lines[0].split(' - ')[0])
    story.append(p(lines[0],'CaseTitle'))
    i=1
    while i<len(lines):
        line=lines[i].strip()
        if not line:
            i+=1;continue
        if line.startswith('|'):
            block=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                block.append(lines[i]);i+=1
            story.extend([table(block),Spacer(1,12)])
            continue
        match=re.match(r'- \*\*(.+?):\*\*\s*(.*)',line)
        if match:
            label,text=match.groups()
            story.append(Paragraph(f'<b>{escape(label)}:</b> {escape(text)}',styles['Field']))
        elif re.match(r'\d+\. ',line): story.append(p(line,'Step'))
        else: story.append(p(line))
        i+=1
    story.append(PageBreak())

story.append(p('Requirement mapping','CaseTitle'))
mapping=source.split('## Requirement mapping')[1]
story.append(table([l for l in mapping.splitlines() if l.startswith('|')]))

def footer(canvas,doc):
    canvas.setStrokeColor(colors.HexColor('#dce3e9'));canvas.line(42,40,554,40)
    canvas.setFont('Helvetica',8);canvas.setFillColor(colors.HexColor('#526779'))
    canvas.drawString(42,27,'FR-QA | Combined test cases | Draft')
    canvas.drawRightString(554,27,str(doc.page))

pdf=OUT/'New.pdf'
doc=SimpleDocTemplate(str(pdf),pagesize=(596,842),leftMargin=42,rightMargin=42,topMargin=42,bottomMargin=54,title='New - Combined Currency Converter Test Cases',author='FR-QA / Codex assisted')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
pages=PdfReader(str(pdf)).pages
texts=[page.extract_text() or '' for page in pages]
text='\n'.join(texts)
for label in ['TC ID','Title','Requirement(s)','Type','Priority','Preconditions','Test data','Steps','Expected result']:
    assert text.count(label+':')==22,(label,text.count(label+':'))
for ident in ids:
    found=[n+1 for n,t in enumerate(texts) if 'TC ID: '+ident+'\n' in t]
    assert len(found)==1,(ident,found)
    assert 'Expected result:' in texts[found[0]-1],(ident,'split case')
print(f'Created {pdf}\n{len(ids)} combined cases; {len(pages)} pages; all nine template fields verified.')
