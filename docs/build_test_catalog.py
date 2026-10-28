from pathlib import Path
from html import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output' / 'pdf'
OUT.mkdir(parents=True, exist_ok=True)
sections = []
def add(n, title, setup, rows, note=''):
    cases = [line.split('|') for line in rows.strip().splitlines()]
    assert all(len(r)==4 for r in cases), n
    sections.append((n,title,setup,cases,note))

add(1,'Reject amounts less than or equal to zero','Use USD to EUR. Supply each numeric amount directly to ConversionAssessor.validate.', '''Reject zero|0.0|Boundary|Throws IllegalArgumentException.
Reject negative zero|-0.0|Edge|Throws IllegalArgumentException.
Reject negative whole amount|-100.0|Negative|Throws IllegalArgumentException.
Reject negative fraction|-0.01|Negative|Throws IllegalArgumentException.
Reject negative value nearest zero|-Double.MIN_VALUE|Boundary|Throws IllegalArgumentException.
Reject most negative finite value|-Double.MAX_VALUE|Boundary|Throws IllegalArgumentException.
Accept smallest positive value|Double.MIN_VALUE|Boundary|Passes amount validation.
Accept typical positive amount|100.0|Positive|Passes amount validation.
Accept largest finite positive value|Double.MAX_VALUE|Boundary|Passes amount validation.''','Direct numeric validation only. R1 defines no positive minimum or upper limit. NaN and infinity require clarification; conversion overflow and GUI formatting are separate concerns.')
add(2,'Reject null or empty currency codes','Use amount 100.0. Call ConversionAssessor.validate with the listed source and target.', '''Missing source|source=null; target=EUR|Negative|Throws IllegalArgumentException.
Empty source|source=""; target=EUR|Negative|Throws IllegalArgumentException.
Missing target|source=USD; target=null|Negative|Throws IllegalArgumentException.
Empty target|source=USD; target=""|Negative|Throws IllegalArgumentException.
Both missing|source=null; target=null|Negative|Throws IllegalArgumentException.
Both empty|source=""; target=""|Negative|Throws IllegalArgumentException.
Valid different currencies|source=USD; target=EUR|Positive|Validation passes.
Same valid currency|source=USD; target=USD|Positive|Validation passes.''','Null is no value; an empty string has zero characters. Whitespace and unsupported codes need separate expectations.')
add(3,'Enter the amount into the amount field','Open the converter with USD to EUR. Focus and clear the amount field before each case; inspect its text after the action.', '''Whole number|Enter "100".|Positive|Field contains "100".
Decimal amount|Enter "12.50".|Positive|Field contains "12.50", including the trailing zero.
Small positive amount|Enter "0.01".|Positive|Field contains "0.01".
Large amount|Enter "1000000".|Edge|Complete value is present without truncation.
Several decimal places|Enter "1.234567".|Edge|Complete text remains without entry-time rounding.
Replace amount|Enter "100", then replace with "250".|Positive|Field contains only "250".
Edit amount|Enter "125", delete final digit, then type "0".|Positive|Field contains "120".''','Quotes identify text and are not typed. Text preservation is an assumption; R8 formats a separate input string. Keyboard editing is manual coverage; the supplied driver sets text directly.')
for n, field, other, currencies in [(4,'source','target EUR',['USD','EUR','GBP','JPY','CAD','AUD','CHF']),(5,'target','source USD',['USD','EUR','GBP','JPY','CAD','AUD','CHF'])]:
    rows='\n'.join(f'Select {c}|Choose {c} in the {field} dropdown.|Positive|Selected {field} displays {c}.' for c in currencies)
    rows += f'\nRepeated selection|Choose EUR, then GBP, then JPY.|Positive|Each selection is displayed; final {field} is JPY.'
    rows += f'\nPreserve selection on blur|Choose GBP, then press Tab.|Positive|Selected {field} remains GBP.'
    add(n,f'Select the {field} currency',f'Open converter; amount 100; {other}. Begin with a different {field} selection. Open dropdown with Enter, navigate with arrows, and confirm with Enter. Check amount and the other currency remain unchanged.', rows,'All seven supported currencies are covered, including a same-currency pair. Keyboard navigation and focus persistence are manual checks; driver selection alone does not prove keyboard behavior.')
add(6,'Wait for the result container to become visible','Use ConverterDriver.waitForResult. Default timeout in the supplied driver is five seconds. Reset or close the GUI after each case.', '''Valid amount|USD to EUR; clear amount, enter 100, then wait.|Positive|Wait returns true and container is visible.
Same-currency conversion|USD to USD; clear amount, enter 100, then wait.|Positive|Wait returns true and container is visible.
Correct invalid input|USD to EUR; enter 0 and confirm hidden; replace with 100 and wait.|Positive|Container becomes visible and wait returns true.
Already visible|Establish visible result for 100 USD to EUR; invoke wait again.|Edge|Wait returns true without requiring another visibility transition.
Delayed visibility|Controlled fixture exposes result after wait starts, before timeout.|Positive|Wait does not succeed while hidden; returns true after visibility.
No result|Leave amount empty; invoke wait.|Negative|Wait returns false after its timeout; it does not hang or report success.''','Delayed visibility requires a controlled fixture beyond the current synchronous UI. Timeout failure is false, not an exception. Visibility does not guarantee current result contents.')
add(7,'Extract converted amount and exchange rate','Establish each conversion and wait for visibility and any content update. Record displayed amount and rate before extraction; compare numerically with extracted values.', '''Typical conversion|100 USD to EUR.|Positive|Both extracted values match their respective displayed values.
Same-currency values|100 USD to USD.|Positive|Extracted amount=100.0; rate=1.0.
Small amount|0.01 USD to USD.|Edge|Extracted amount=0.01; rate=1.0.
Large amount|1000000 USD to USD.|Edge|Extracted amount=1000000.0; rate=1.0; no truncation.
Rate precision|100 JPY to GBP.|Positive|All displayed rate digits are retained numerically; amount matches display.
After amount change|100 USD to USD; change to 200 and extract again.|Positive|Amount=200.0; rate=1.0; no stale amount.
After currency change|100 USD to USD; change target to EUR and extract again.|Positive|Both values match the new display; no stale values.''','R7 verifies extraction, not arithmetic accuracy. Numeric values do not retain trailing-zero formatting; preserve original strings for decimal-count tests.')
add(8,'Format input amount to two decimal places','Use a fixed dot-decimal locale. Exercise the formatting path used by assessment: String.format("%.2f", amount). Inspect the formatted string.', '''Whole number|100.0|Positive|"100.00"
One decimal place|12.5|Positive|"12.50"
Two decimal places|12.34|Positive|"12.34"
Round down|12.344|Boundary|"12.34"
Round up|12.346|Boundary|"12.35"
Exact halfway value|1.125|Boundary|"1.13"
Carry into whole part|9.999|Edge|"10.00"
Below one cent|0.001|Edge|"0.00"''','Check exact strings and exactly two fractional digits. Formatting does not change the original numeric amount or require replacing GUI text. The original 0.001 passes R1.')
add(9,'Count decimal places in input and result strings','Fix locale to dot decimal. Format the input with %.2f; pass its string and the result string separately to countDecimalPlaces. Controlled result strings are helper fixtures.', '''Whole-number input|Input 100; result "92.35".|Positive|Input count=2; result count=2.
One-decimal input|Input 12.5; result "11.50".|Positive|Input count=2; result count=2.
Rounded input|Input 1.234; result "1.1400".|Positive|Formatted input "1.23": count=2; result count=4.
One result decimal|Input 100; result "92.3".|Boundary|Input count=2; result count=1.
Integer result text|Input 100; result "92".|Boundary|Input count=2; result count=0.
Leading fractional zeros|Input 0.001; result "0.0001".|Edge|Formatted input "0.00": count=2; result count=4.''','Count characters after the decimal point, including trailing zeros. Fixtures use plain numeric strings; scientific notation, commas and malformed text are outside the stated contract.')
accuracy='''Exact result|amount=1; rate=1; result=1.|Positive|Accuracy passes: difference is zero.
Within tolerance above|amount=1; rate=1; result=1.009.|Boundary|Accuracy passes: difference is below 0.01.
Within tolerance below|amount=1; rate=1; result=0.991.|Boundary|Accuracy passes: difference is below 0.01.
Exactly at tolerance|amount=1; rate=0.01; result=0.|Boundary|Accuracy passes: evaluated difference equals 0.01.
Above tolerance, high|amount=1; rate=1; result=1.011.|Negative|Accuracy fails: difference exceeds 0.01.
Above tolerance, low|amount=1; rate=1; result=0.989.|Negative|Accuracy fails: difference exceeds 0.01.'''
add(10,'Validate conversion accuracy','Use controlled numeric fixtures for amount, displayed rate and extracted result. Evaluate Math.abs(result - amount * rate) <= 0.01 and compare with expected status.',accuracy,'Controlled fixtures isolate the predicate; they are not necessarily real UI conversions. The exact-boundary fixture avoids subtracting two nearly equal values. Use the displayed rate as required; rounded rates can cause larger errors for large amounts.')
precision='''Exactly two digits|Result text "92.35".|Boundary|Precision passes.
Three digits|Result text "92.350".|Positive|Precision passes; trailing zero counts.
Four digits|Result text "0.0001".|Positive|Precision passes.
One digit|Result text "92.3".|Negative|Precision fails.
No decimal point|Result text "92".|Negative|Precision fails.
Zero with two digits|Result text "0.00".|Edge|Precision passes; numeric magnitude does not affect digit count.'''
add(11,'Require at least two result decimal places','Use controlled displayed-result strings. Count fractional digits and evaluate whether the count is at least two.',precision,'The real UI normally displays two decimals. Nonstandard precision strings require helper-level fixtures; no application changes are assumed.')
add(12,'Update the result and restore the original amount','Establish a visible baseline, record amount and result, keep currencies fixed, change amount, wait for updated content, then restore the exact original amount and verify the original result.', '''Increase amount|USD to USD: 100 -> 200 -> 100.|Positive|Result 100.00 -> 200.00 -> 100.00; original amount restored.
Decrease amount|USD to USD: 100 -> 50 -> 100.|Positive|Result 100.00 -> 50.00 -> 100.00; original amount restored.
Fractional amount|USD to USD: 12.50 -> 25.00 -> 12.50.|Positive|Results follow each amount; final result 12.50 and original amount restored.
Different currencies|USD to EUR: 100 -> 200 -> 100.|Positive|Middle displayed result differs; final result equals baseline.
Repeated changes|USD to USD: 100 -> 200 -> 300 -> 100.|Positive|Results 100.00, 200.00, 300.00, 100.00; no stale intermediate value.
Failure to restore|Controlled fixture updates result but prevents baseline restoration.|Negative|Dynamic-update check fails; successful change alone does not satisfy R12.''','The supplied verifyDynamicUpdate doubles the amount and checks result-text change plus restored result text. Decrease/repeated-change cases need separate driver sequences. Check restored input independently; the helper only verifies restored result text.')
add(13,'Return the original input amount','Assess each amount with USD to USD. Inspect ConversionResult.inputAmount and compare directly with the supplied double, rather than the two-decimal formatting.', '''Whole amount|100.0|Positive|inputAmount=100.0.
Fractional amount|12.3|Positive|inputAmount=12.3.
Small amount|0.01|Positive|inputAmount=0.01.
Extra precision|1.234|Edge|inputAmount=1.234, not 1.23.
Large amount|1000000.0|Edge|inputAmount=1000000.0.
After another assessment|Assess 100.0, then 250.75.|Positive|Second record inputAmount=250.75, with no stale first amount.''','Compare the original double value exactly for this pass-through field. A false completion flag caused by rounded display does not justify changing inputAmount.')
for n,field,target in [(14,'sourceCurrency','source'),(15,'targetCurrency','target')]:
    rows='\n'.join(f'Return {c}|Assess 100 with {target}={c}; other currency=USD.|Positive|{field}="{c}".' for c in ['USD','EUR','GBP','JPY','CAD','AUD','CHF'])
    rows+=f'\nReturn latest selection|Assess with {target}=GBP, then assess with {target}=EUR.|Positive|Second record {field}="EUR", not "GBP".'
    add(n,f'Return the selected {target} currency',f'Use amount 100 and valid currency selections. Assess each conversion and compare ConversionResult.{field} with the actual selected dropdown code.',rows,'Check the dropdown selection independently, rather than only comparing the returned field with the argument passed to assess.')
add(16,'Return the converted amount extracted from the UI','Assess the conversion; capture the baseline result text before the dynamic-update probe. Compare ConversionResult.conversionResult with the numeric value of that text.', '''Whole result|100 USD to USD; baseline "100.00".|Positive|conversionResult=100.0.
Fractional result|12.34 USD to USD; baseline "12.34".|Positive|conversionResult=12.34.
Small result|0.01 USD to USD; baseline "0.01".|Edge|conversionResult=0.01.
Large result|1000000 USD to USD.|Edge|conversionResult=1000000.0.
Displayed rounding|1.234 USD to USD; baseline "1.23".|Boundary|conversionResult=1.23, rather than unrounded 1.234.
Latest conversion|Assess 100 USD to USD, then 200 USD to USD.|Positive|Second record conversionResult=200.0.''','R16 checks the observed UI value, not a separately recomputed mathematical value. Numeric comparison may use a small floating-point delta appropriate to parsing.')
add(17,'Return the formatted input decimal count','Assess each amount with USD to USD. Inspect inputDecimalPlaces and independently check the %.2f input string under the fixed locale.', '''Whole input|100.0 -> "100.00".|Positive|inputDecimalPlaces=2.
One decimal|12.5 -> "12.50".|Positive|inputDecimalPlaces=2.
Two decimals|12.34 -> "12.34".|Positive|inputDecimalPlaces=2.
Extra decimals|1.234 -> "1.23".|Edge|inputDecimalPlaces=2, not 3.
Rounded to zero|0.001 -> "0.00".|Edge|inputDecimalPlaces=2 even if completion is false.
Large input|1000000.0 -> "1000000.00".|Edge|inputDecimalPlaces=2.''','Field counts the formatted input string, not the raw amount text or the double representation.')
add(18,'Return the displayed result decimal count','Inspect resultDecimalPlaces against an independently counted baseline result string. For strings the real UI cannot produce, use a controlled assessor/driver fixture.', '''Normal result|Baseline "92.35".|Positive|resultDecimalPlaces=2.
Trailing zero|Baseline "92.350".|Positive|resultDecimalPlaces=3.
Leading fractional zeros|Baseline "0.0001".|Edge|resultDecimalPlaces=4.
One decimal|Baseline "92.3".|Negative|resultDecimalPlaces=1; do not force the count to 2.
Integer text|Baseline "92".|Negative|resultDecimalPlaces=0.
Zero display|Baseline "0.00".|Edge|resultDecimalPlaces=2.''','Nonstandard display strings are controlled tests, not ordinary UI inputs. R18 reports the count even when R11 fails.')
add(19,'Return a truthful accuracy flag','Use controlled assessment fixtures. Inspect conversionAccurate; arrange visibility, precision and update to pass independently.',accuracy.replace('Accuracy passes','conversionAccurate=true').replace('Accuracy fails','conversionAccurate=false'),'Tests trace both the numeric predicate (R10) and its returned field (R19). Controlled full-assessment fixtures require a test seam; direct construction of a record does not test the assessor.')
add(20,'Return a truthful precision flag','Use controlled baseline result strings in assessment. Inspect decimalPrecisionMaintained and independently count decimal places.',precision.replace('Precision passes','decimalPrecisionMaintained=true').replace('Precision fails','decimalPrecisionMaintained=false'),'Tests trace both the precision rule (R11) and returned flag (R20). Nonstandard UI output requires controlled fixtures.')
add(21,'Return a truthful dynamic-update flag','Inspect resultUpdatedOnChange after assessment. Record baseline, changed and restored text. Keep currencies fixed and check the original amount is restored.', '''Increase and restore|USD to USD: baseline 100; probe doubles to 200; restore 100.|Positive|resultUpdatedOnChange=true.
Fractional update|USD to USD: 12.5 -> 25 -> 12.5.|Positive|resultUpdatedOnChange=true.
Different currencies|USD to EUR: 100 -> 200 -> 100.|Positive|resultUpdatedOnChange=true when changed text differs and restored text matches.
Frozen result|Controlled fixture retains baseline text after amount doubles.|Negative|resultUpdatedOnChange=false.
Change hidden by rounding|USD to USD: 0.001 -> 0.002 -> 0.001; each displays 0.00.|Edge|resultUpdatedOnChange=false because displayed result never changes.
Restoration fails|Controlled fixture changes result but restored text differs from baseline.|Negative|resultUpdatedOnChange=false.''','The current helper requires both visible text change and restoration. R21 wording emphasizes update, while the helper also incorporates R12 cleanup; confirm this interpretation with reviewers.')
add(22,'Return a truthful completion flag','Use a controlled assessment fixture for isolated failures. Start with valid amount/currency fields. Inspect conversionComplete and all contributing values.', '''All conditions pass|Visible=true; accurate=true; precise=true; updated=true; fields correct.|Positive|conversionComplete=true.
Accuracy fails|Only accurate=false; other three conditions true.|Negative|conversionComplete=false.
Precision fails|Only precise=false; other three conditions true.|Negative|conversionComplete=false.
Update fails|Only updated=false; other three conditions true.|Negative|conversionComplete=false.
Visibility fails|Only visible=false; fixture still supplies parseable result text.|Negative|conversionComplete=false.
Multiple failures|accurate=false and precise=false; visible and updated true.|Negative|conversionComplete=false.
Incorrect returned field|Other checks pass; controlled fault returns a currency field that differs from selection.|Negative|Under the full R22 requirement, completion must not be reported true; flag any contrary behavior as a defect.''','Current code computes complete = visible && accurate && precise && updated. It does not independently validate every returned field or restored input. The final case is a requirement-driven fault-injection design, not a passing claim about current code. Clarify whether R22 requires explicit field-correctness checks.')

from render_test_catalog import build_catalog
build_catalog(ROOT, sections)
