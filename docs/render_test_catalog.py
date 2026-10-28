"""Render the catalog using the README's complete, per-case template."""
from html import escape
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
    KeepTogether, CondPageBreak,
)
from pypdf import PdfReader


GUI = 'Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.'
FIXTURE = ('A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. '
           'This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.')


def expand_case(n, i, row):
    title, action, kind, expected = row
    ident = f'TC-R{n}-{i:02}'
    pre, data, steps = GUI, action, []
    cleanup = 'Close the converter and discard this case\'s state.'
    if n == 1:
        pre = 'ConversionAssessor.validate is callable with Java double values; no GUI is required.'
        data = f'amount={action}; source="USD"; target="EUR".'
        steps = [f'Set amount to {action} without formatting or conversion.',
                 'Call ConversionAssessor.validate(amount, "USD", "EUR").',
                 'Capture any exception and compare its type, or absence, with the expected result.']
        cleanup = 'Discard the validation inputs; no GUI state was created.'
    elif n == 2:
        pre = 'ConversionAssessor.validate is callable; Java null and empty strings can be supplied directly.'
        data = f'amount=100.0; {action}'
        steps = ['Assign the source and target exactly as listed; null is not the text "null".',
                 'Call ConversionAssessor.validate(100.0, source, target).',
                 'Capture any exception and compare its type, or absence, with the expected result.']
        cleanup = 'Discard the validation inputs; no GUI state was created.'
    elif n == 3:
        data = 'source="USD"; target="EUR"; ' + action
        steps = ['Set source to USD and target to EUR; focus and clear the amount field.',
                 action, 'Read the complete amount-field text and compare it character for character with the expected result.',
                 'Verify source is still USD and target is still EUR.']
    elif n in (4, 5):
        field = 'source' if n == 4 else 'target'
        other = 'target=EUR' if n == 4 else 'source=USD'
        chosen = ['USD','EUR','GBP','JPY','CAD','AUD','CHF'][i-1] if i <= 7 else 'EUR' if i == 8 else 'GBP'
        start = 'CHF' if chosen != 'CHF' else 'USD'
        data = f'amount="100"; {other}; starting {field}={start}; {action}'
        if i <= 7:
            selection = f'Press Enter on the {field} dropdown, use arrow keys to highlight {chosen}, and press Enter to select it.'
        elif i == 8:
            selection = f'Open the {field} dropdown with Enter and select EUR using arrow keys and Enter; repeat for GBP, then JPY. Check the displayed selection after each choice.'
        else:
            selection = f'Open the {field} dropdown with Enter, select GBP using arrow keys and Enter, then press Tab to leave it.'
        steps = [f'Enter amount 100, set {other.replace("=", " to ")}, and set the starting {field} to {start}.',
                 f'Focus the {field} dropdown.', selection,
                 f'Read the final {field} selection; confirm amount remains 100 and {other.replace("=", " remains ")}.']
    elif n == 6:
        pre += ' ConverterDriver.waitForResult is available with its five-second timeout.'
        data = 'source=USD; target=EUR; ' + action
        if i == 2:
            data = 'source=USD; target=USD; amount=100; starting amount empty.'
        if i == 5:
            pre += ' A fixture can hide the result initially and expose it after one second without blocking the wait.'
            data = 'amount=100; source=USD; target=EUR; visibility false -> true after 1 second; timeout=5 seconds.'
            arrangement = 'Configure the fixture to keep the container hidden initially and expose it one second after waiting begins.'
        else:
            arrangements = {
                1: 'Select USD to EUR; clear the amount and confirm the result is hidden; enter 100.',
                2: 'Select USD to USD; clear the amount and confirm the result is hidden; enter 100.',
                3: 'Select USD to EUR; enter 0 and confirm the result is hidden; replace 0 with 100.',
                4: 'Enter 100 with USD to EUR; confirm the result is already visible.',
                6: 'Select USD to EUR; clear the amount and confirm the result remains hidden.',
            }
            arrangement = arrangements[i]
        steps = [arrangement, 'Invoke ConverterDriver.waitForResult and record its returned boolean and elapsed time.',
                 'Observe result visibility at completion and compare with the expected result.']
        if i == 6:
            steps.append('Confirm false is returned around the configured five-second deadline, allowing normal scheduling overhead, and that the wait terminates.')
    elif n == 7:
        steps = ['Establish the conversion and any subsequent change listed in Test data.',
                 'Wait for visibility; after a change, also wait until the displayed text reflects that change.',
                 'Record the amount and rate strings directly from their respective UI labels.',
                 'Invoke the driver/window extraction path and parse both strings as doubles.',
                 'Compare each extracted number with its corresponding recorded label value; check the expected result.']
    elif n == 8:
        pre = 'The assessment input-formatting path is observable; Locale.ROOT or an equivalent dot-decimal locale is active.'
        data = f'amount={action}; format="%.2f"; locale=ROOT; source=USD; target=EUR if the full assessment is used.'
        steps = [f'Supply the numeric double {action} to the input-formatting path.',
                 'Execute String.format("%.2f", amount) under the fixed locale and capture the resulting string.',
                 'Compare the entire string with the expected result, including decimal point and trailing zeros.',
                 'Count the fractional digits independently and confirm there are exactly two.']
        cleanup = 'Discard formatting inputs and outputs; close any assessment GUI used.'
    elif n == 9:
        pre = 'ConversionAssessor.countDecimalPlaces is callable; dot-decimal locale is active; controlled numeric strings are available.'
        steps = ['Set the numeric input and controlled result string exactly as listed.',
                 'Format the input with String.format("%.2f", amount) under the fixed locale.',
                 'Call countDecimalPlaces separately on the formatted input string and the unchanged result string.',
                 'Compare both returned integer counts with the expected counts, including trailing zeros.']
        cleanup = 'Discard the helper inputs and outputs.'
    elif n in (10, 19):
        pre = FIXTURE
        triples = [('1','1','1.000'),('1','1','1.009'),('1','1','0.991'),
                   ('1','0.01','0.00'),('1','1','1.011'),('1','1','0.989')]
        amount, rate, text = triples[i-1]
        changed = '2.000' if text != '2.000' else '3.000'
        data = (f'amount={amount}; source=USD; target=USD; displayed rate="{rate}"; baseline result="{text}"; '
                f'visible=true; changed result="{changed}"; restored result="{text}".')
        steps = ['Configure the fixture with the listed baseline values; return the changed and restored strings during the assessor\'s double-and-restore probe.',
                 f'Call the real assessment path with amount={amount}, source=USD and target=USD.',
                 'Independently calculate Math.abs(parsed baseline result - amount * parsed displayed rate); compare with 0.01.',
                 'Inspect conversionAccurate and compare it with the expected outcome; confirm precision and update checks pass.']
        if n == 10:
            expected = expected.replace('Accuracy passes', 'Accuracy predicate is true').replace('Accuracy fails','Accuracy predicate is false')
    elif n in (11, 20):
        pre = ('ConversionAssessor.countDecimalPlaces is callable; controlled result strings are available.' if n == 11 else FIXTURE)
        text = ['92.35','92.350','0.0001','92.3','92','0.00'][i-1]
        data = f'result text="{text}".'
        if n == 11:
            steps = ['Supply the result string exactly as listed; preserve all fractional zeros.',
                     'Count fractional digits with countDecimalPlaces.',
                     'Evaluate count >= 2 and compare with the expected precision outcome.']
            cleanup = 'Discard the helper inputs and outputs; no GUI state was created.'
        else:
            data += f' amount=1; source=USD; target=USD; displayed rate="{text}"; visible=true; changed result="184.70"; restored result="{text}".'
            steps = ['Configure baseline result and rate with the exact strings listed; arrange a changed result distinct from baseline and an exact restoration.',
                     'Call the real assess(1, "USD", "USD") path through that fixture.',
                     'Count baseline fractional digits independently; inspect resultDecimalPlaces and decimalPrecisionMaintained.',
                     'Compare decimalPrecisionMaintained with count >= 2 and the expected result; confirm accuracy and dynamic update pass.']
    elif n == 12:
        if i == 6:
            pre = FIXTURE
            data = 'amount=100; source=USD; target=USD; baseline="100.00"; changed="200.00"; attempted restored result="150.00".'
            steps = ['Configure the fixture to show the listed baseline, changed and failed-restoration values in order.',
                     'Run verifyDynamicUpdate(100, "100.00").',
                     'Check it attempted to enter 200 and then 100.',
                     'Verify the check returns false because restored result text differs from baseline.']
        else:
            sequences = [('USD','USD',['100','200','100']),('USD','USD',['100','50','100']),
                         ('USD','USD',['12.50','25.00','12.50']),('USD','EUR',['100','200','100']),
                         ('USD','USD',['100','200','300','100'])]
            source,target,amounts = sequences[i-1]
            data = f'source={source}; target={target}; amount sequence='+' -> '.join(amounts)+'.'
            steps = [f'Select {source} to {target}, enter {amounts[0]}, and wait for a visible result; record exact original amount text and baseline result.',
                     'Enter each intermediate amount in order: '+', '.join(amounts[1:-1])+'. Wait for the corresponding result and compare it with the previous result.',
                     'Restore the exact original amount text and wait for the baseline result to return.',
                     'Verify the amount field and result both equal their recorded originals, and that source and target did not change.']
    elif n == 13:
        values=['100.0','12.3','0.01','1.234','1000000.0']
        data = f'amount={values[i-1]}; source=USD; target=USD.' if i<=5 else 'first amount=100.0; second amount=250.75; source=USD; target=USD.'
        steps = ['Run assess with the listed amount and USD to USD; if two amounts are listed, run a separate assessment for each in that order.',
                 'Read inputAmount from the returned record, using the second record for the sequential case.',
                 'Compare the field with the exact original double argument; do not compare with the two-decimal formatted string.']
    elif n in (14,15):
        field,which = ('sourceCurrency','source') if n==14 else ('targetCurrency','target')
        codes=['USD','EUR','GBP','JPY','CAD','AUD','CHF']
        data = f'amount=100; {which}={codes[i-1]}; other currency=USD.' if i<=7 else f'amount=100; {which} sequence=GBP -> EUR; other currency=USD.'
        steps = [f'Run the assessment with the specified amount and currencies; for the sequential case assess GBP first, then EUR as {which}.',
                 f'Read the selected {which} code directly from the GUI after the assessment.',
                 f'Inspect {field} on the returned record, using the second record for the sequential case.',
                 'Compare the field with both the independently observed dropdown selection and the expected code.']
    elif n == 16:
        amounts=['100','12.34','0.01','1000000','1.234']
        data = f'amount={amounts[i-1]}; source=USD; target=USD.' if i<=5 else 'amount sequence=100 -> 200; source=USD; target=USD.'
        steps = ['Run assess with the specified amount and USD to USD; for the sequential case assess 100 and then 200.',
                 'Observe and record the initial result label before the assessment\'s temporary dynamic-update probe.',
                 'Read conversionResult from the relevant returned record and compare with the parsed baseline UI text using a numerical delta of 1e-9.',
                 'Verify the field represents the displayed rounded amount rather than an unrounded service calculation or a temporary probe result.']
    elif n == 17:
        values=['100.0','12.5','12.34','1.234','0.001','1000000.0']
        data=f'amount={values[i-1]}; source=USD; target=USD; input format="%.2f"; locale=ROOT.'
        steps = ['Run assess with the specified numeric input and USD to USD.',
                 'Independently form the two-decimal input string and count its fractional digits.',
                 'Inspect inputDecimalPlaces on the returned record and compare with the independent count and the expected result.']
    elif n == 18:
        pre = FIXTURE
        text=['92.35','92.350','0.0001','92.3','92','0.00'][i-1]
        data = f'amount=1; source=USD; target=USD; baseline result="{text}"; displayed rate="{text}"; visible=true; changed result="184.70"; restored result="{text}".'
        steps = ['Configure the fixture to return the exact baseline string, including all trailing zeros, and the listed rate and update sequence.',
                 'Run the real assess(1, "USD", "USD") path and retain the returned record.',
                 'Count fractional digits in the baseline string independently and compare with resultDecimalPlaces.',
                 'Verify a precision failure does not cause the reported count to be replaced with 2.']
    elif n == 21:
        if i <= 3 or i == 5:
            data = ['amount=100; source=USD; target=USD; probe=200; restore=100.',
                    'amount=12.5; source=USD; target=USD; probe=25; restore=12.5.',
                    'amount=100; source=USD; target=EUR; probe=200; restore=100.',
                    '', 'amount=0.001; source=USD; target=USD; probe=0.002; restore=0.001.'][i-1]
            amount = ['100','12.5','100','','0.001'][i-1]
            target='EUR' if i==3 else 'USD'
            steps = [f'Run assess({amount}, "USD", "{target}") and observe the baseline, doubled-amount and restored result strings.',
                     'Independently determine whether changed text differs from baseline and restored text equals baseline.',
                     'Inspect resultUpdatedOnChange and compare with the expected boolean.',
                     'Confirm the original input amount and currencies are restored.']
        else:
            pre = FIXTURE
            changed,restored = ('100.00','100.00') if i==4 else ('200.00','150.00')
            data = f'amount=100; source=USD; target=USD; baseline="100.00"; rate="1.000000"; changed="{changed}"; restored="{restored}"; visible=true.'
            steps = ['Configure the exact baseline, changed and restored strings listed.',
                     'Run the real assess(100, "USD", "USD") path through the fixture.',
                     'Confirm the dynamic probe attempts 200 and restoration attempts 100.',
                     'Inspect resultUpdatedOnChange and verify false is returned for the listed failed condition.']
    elif n == 22:
        pre = FIXTURE
        fixture_data = [
            'amount=100; source=USD; target=USD; rate="1"; baseline="100.00"; changed="200.00"; restored="100.00"; visible=true.',
            'amount=100; source=USD; target=USD; rate="1"; baseline="100.02"; changed="200.02"; restored="100.02"; visible=true.',
            'amount=100; source=USD; target=USD; rate="1"; baseline="100.0"; changed="200.0"; restored="100.0"; visible=true.',
            'amount=100; source=USD; target=USD; rate="1"; baseline="100.00"; changed="100.00"; restored="100.00"; visible=true.',
            'amount=100; source=USD; target=USD; rate="1"; baseline="100.00"; changed="200.00"; restored="100.00"; initial wait=false; update waits=true.',
            'amount=100; source=USD; target=USD; rate="1"; baseline="100.1"; changed="200.1"; restored="100.1"; visible=true.',
            'amount=100; requested source=USD; actual selected source=EUR; target=USD; controlled rate="1"; baseline="100.00"; changed="200.00"; restored="100.00"; visible=true.',
        ]
        data=fixture_data[i-1]
        if i == 7:
            pre += ' An approved fault-injection seam can make source selection disagree with the requested source before result creation; R22 field-correctness semantics require PD review.'
        steps = ['Arrange the listed fixture responses to match this case, including its passing or failing conditions; keep all result strings parseable.',
                 'Run the real assess(100, "USD", "USD") path; retain the returned record and observed selection/visibility.',
                 'Independently verify accuracy, decimal count, update/restoration and actual selected currencies from fixture evidence.',
                 'Inspect conversionComplete and compare with the expected result; record a requirement ambiguity or defect rather than modifying application behavior.']
    else:
        raise ValueError(n)
    steps.append(cleanup)
    requirement = f'R{n}'
    if n == 19: requirement += ', R10'
    if n == 20: requirement += ', R11'
    if n == 21: requirement += ', R12'
    return dict(id=ident, title=title, requirement=requirement, type=kind,
                priority='Medium' if kind=='Edge' else 'High', preconditions=pre,
                data=data, steps=steps, expected=expected)


def build_catalog(root, sections):
    out=root/'output'/'pdf'
    out.mkdir(parents=True,exist_ok=True)
    catalog=[(n,title,[expand_case(n,i,row) for i,row in enumerate(rows,1)],note)
             for n,title,setup,rows,note in sections]
    total=sum(len(cases) for _,_,cases,_ in catalog)
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Case',fontName='Helvetica-Bold',fontSize=11,leading=14,textColor=colors.HexColor('#173b57'),spaceAfter=7))
    styles.add(ParagraphStyle(name='Field',fontName='Helvetica',fontSize=9.2,leading=12.4,spaceAfter=4))
    styles.add(ParagraphStyle(name='Step',parent=styles['Field'],leftIndent=12,firstLineIndent=-10,spaceAfter=3))
    styles.add(ParagraphStyle(name='Note',fontName='Helvetica',fontSize=8.5,leading=11.5,textColor=colors.HexColor('#425466')))
    styles['Title'].textColor=styles['Heading1'].textColor=colors.HexColor('#173b57')
    styles['BodyText'].leading=14
    def p(text,style='BodyText'): return Paragraph(escape(str(text)),styles[style])
    def field(label,text): return Paragraph(f'<b>{escape(label)}:</b> {escape(str(text))}',styles['Field'])
    intro=[
        f'{total} individually documented test cases covering all 22 requirements.',
        'Status: Draft. No test execution, automation or PD Team approval is claimed.',
        'Each case uses the README template: TC ID, Title, Requirement(s), Type, Priority, Preconditions, Test data, numbered Steps, and Expected result. Numbering restarts for each requirement.',
        'The preconditions, data and steps are repeated within every case so it can be reviewed or executed independently. High priority is assigned to positive, negative and boundary cases; Edge cases are Medium.',
        'Controlled-fixture designs are explicitly identified. Mark them Not Run until a suitable fixture is available; no changes to application code or dependencies are authorized by this document.',
        'Use Locale.ROOT or an equivalent dot-decimal locale. Quotes denote strings; do not type them into the amount field. Keep the original numeric input separate from the formatted input and displayed result strings.',
        'Prepared October 16, 2026 (America/Phoenix). OpenAI Codex assisted with test design and formatting. This document retains all 152 case IDs from the prior catalog.',
    ]
    story=[p('Currency Converter','Title'),p('Test cases | R1-R22','Heading1'),Spacer(1,18)]
    for text in intro: story.extend([p(text),Spacer(1,12)])
    story += [p('Review and execution','Heading2'),p('Compare each actual outcome with its expected result and attach evidence. Restore original inputs during R12 checks and close the GUI after each case. Obtain PD Team approval before Phase 3 automation. Requirement notes, open questions and the traceability matrix follow the test cases.'),PageBreak()]
    md=['# Currency Converter - R1-R22 Test Cases','']
    md += [text+'\n' for text in intro]
    for n,title,cases,note in catalog:
        story += [p(f'R{n} | {title}','Heading1'),p(f'{len(cases)} cases | Draft, not executed','Note'),Spacer(1,12)]
        md += [f'## R{n} - {title}','']
        for case in cases:
            ident=case['id']
            block=[p(f'{ident} - {case["title"]}','Case')]
            block.append(field('TC ID',ident))
            block.append(field('Title',case['title']))
            pairs=[('Requirement(s)','requirement'),('Type','type'),('Priority','priority'),('Preconditions','preconditions'),('Test data','data')]
            for label,key in pairs: block.append(field(label,case[key]))
            block.append(field('Steps',''))
            for j,step in enumerate(case['steps'],1): block.append(p(f'{j}. {step}','Step'))
            block += [field('Expected result',case['expected']),Spacer(1,16)]
            story += [KeepTogether(block)]
            md += [f'### {ident} - {case["title"]}',f'- **TC ID:** {ident}',f'- **Title:** {case["title"]}']
            md += [f'- **{label}:** {case[key]}' for label,key in pairs]
            md += ['- **Steps:**']+[f'  {j}. {step}' for j,step in enumerate(case['steps'],1)]
            md += [f'- **Expected result:** {case["expected"]}','']
        story.append(PageBreak())
    story += [p('Traceability matrix','Heading1'),p('Every requirement R1-R22 has dedicated cases. R19 additionally traces R10, R20 traces R11, and R21 traces R12.'),Spacer(1,12)]
    matrix=[[p('Requirement','Note'),p('Dedicated cases','Note')]]
    md += ['## Traceability matrix','','| Requirement | Dedicated cases |','|---|---|']
    for n,_,cases,_ in catalog:
        text=f'TC-R{n}-01 through TC-R{n}-{len(cases):02}'
        matrix.append([p(f'R{n}','Note'),p(text,'Note')])
        md.append(f'| R{n} | {text} |')
    table=Table(matrix,colWidths=[95,417],repeatRows=1,hAlign='LEFT')
    table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dceaf3')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f3f6f9')]),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
    story += [table,PageBreak(),p('Assumptions and questions','Heading1')]
    md += ['','## Assumptions and questions','']
    for n,_,_,note in catalog:
        story += [KeepTogether([p(f'R{n}','Heading3'),p(note,'Note'),Spacer(1,7)])]
        md += [f'### R{n}',note,'']
    sources='Project README.md supplies the required template, R1-R22 and assessment rules. ConversionAssessor.java and ConverterDriver.java supply helper behavior. Test ideas originate from the project discussion. OpenAI Codex assisted with preparation; disclose this in SOLUTION.md when that deliverable is written.'
    story += [Spacer(1,12),p('Sources and AI disclosure','Heading2'),p(sources,'Note')]
    md += ['## Sources and AI disclosure','',sources,'']
    def footer(canvas,doc):
        canvas.setStrokeColor(colors.HexColor('#dce3e9'));canvas.line(42,40,554,40)
        canvas.setFillColor(colors.HexColor('#526779'));canvas.setFont('Helvetica',8)
        canvas.drawString(42,27,'FR-QA | Test cases R1-R22 | Draft')
        canvas.drawRightString(554,27,str(doc.page))
    pdf=out/'currency-converter-test-cases-R1-R22.pdf'
    doc=SimpleDocTemplate(str(pdf),pagesize=(596,842),leftMargin=42,rightMargin=42,topMargin=42,bottomMargin=54,title='Currency Converter - R1-R22 Test Cases',author='FR-QA / Codex assisted')
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    source='\n'.join(md)
    (out/'currency-converter-test-cases-R1-R22.md').write_text(source,encoding='utf-8')
    (root/'docs'/'test-cases.md').write_text(source,encoding='utf-8')
    pages=PdfReader(str(pdf)).pages
    page_texts=[page.extract_text() or '' for page in pages]
    all_text='\n'.join(page_texts)
    fields=['TC ID','Title','Requirement(s)','Type','Priority','Preconditions','Test data','Steps','Expected result']
    assert len(re.findall(r'^### TC-R\d+-\d{2} - ',source,re.M))==total
    for label in fields:
        assert source.count(f'- **{label}:**')==total,(label,'Markdown field count')
        assert all_text.count(label+':')==total,(label,'PDF field count',all_text.count(label+':'))
    positions={}
    for n,_,cases,_ in catalog:
        for case in cases:
            ident=case['id']
            assert ident in all_text
            hits=[k+1 for k,text in enumerate(page_texts) if ident+' - ' in text]
            assert len(hits)==1,(ident,hits)
            positions[ident]=hits[0]
    print(f'Updated PDF: {pdf}\nCases: {total}; pages: {len(pages)}. All nine template fields verified for every case in PDF and Markdown.\nUpdated: {root / "docs" / "test-cases.md"}')
    import json
    (root/'tmp'/'pdfs').mkdir(parents=True,exist_ok=True)
    (root/'tmp'/'pdfs'/'case-pages.json').write_text(json.dumps(positions),encoding='utf-8')
