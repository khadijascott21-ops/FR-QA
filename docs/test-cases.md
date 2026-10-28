# Currency Converter - Test Cases

14 manual GUI test cases using the README template. Each listed data row is a separate run. The traceability matrix identifies requirements that still need code-level verification. Draft - tests have not been executed.

## Setup

Use the fixed rates supplied with the project and a dot-decimal locale. Start each GUI case in a fresh session and close it afterward. Use the keyboard and a calculator for these cases; no helper calls or code changes are required.

## Test cases

### TC-01 - Convert USD to EUR
- **TC ID:** TC-01
- **Title:** Convert USD to EUR
- **Requirement(s):** R3, R4, R5, R6, R7, R10, R11
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open with a dot-decimal locale.
- **Test data:** Amount: 100; source: USD; target: EUR.
- **Steps:**
  1. Enter 100 in the amount field.
  2. Select USD in From and EUR in To.
  3. Wait for the result container, then read the converted amount and exchange rate.
- **Expected result:** The result is visible and shows 86.26 with rate 0.862623. The result has 2 decimal places. Math.abs(86.26 - 100 * 0.862623) is approximately 0.0023, within the 0.01 tolerance.

### TC-02 - Reject zero amount
- **TC ID:** TC-02
- **Title:** Reject zero amount
- **Requirement(s):** R1
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** Converter is open with a dot-decimal locale.
- **Test data:** Amount: 0.0; source: USD; target: EUR.
- **Steps:**
  1. Select USD in From and EUR in To, then enter 100 to show a valid result.
  2. Replace the amount with 0.
  3. Read the validation message and check whether the result remains visible.
- **Expected result:** A validation message says the amount must be greater than zero, and the conversion result is hidden. This checks visible rejection; the exception type cannot be verified through the GUI.

### TC-03 - Reject negative amounts
- **TC ID:** TC-03
- **Title:** Reject negative amounts
- **Requirement(s):** R1
- **Type:** Negative
- **Priority:** High
- **Preconditions:** Converter is open with a dot-decimal locale.
- **Test data:** Amounts: -100.0 and -0.01; source: USD; target: EUR.
- **Steps:**
  1. Select USD in From and EUR in To.
  2. Enter -100.0, then repeat with -0.01.
  3. For each amount, read the validation message and check result visibility.
- **Expected result:** Both amounts show a validation message saying the amount must be greater than zero. The conversion result is hidden. The exception type needs a separate code-level test.

### TC-04 - Verify the GUI prevents an empty currency selection
- **TC ID:** TC-04
- **Title:** Verify the GUI prevents an empty currency selection
- **Requirement(s):** R2 (related GUI prevention only; not direct R2 verification)
- **Type:** Negative
- **Priority:** High
- **Preconditions:** Converter is open with a dot-decimal locale.
- **Test data:** Amount: 100; default source: USD; default target: EUR. Related requirement: R2.
- **Steps:**
  1. Check that From and To already have valid currency codes selected when the converter opens.
  2. Enter 100. Focus each dropdown and try typing an invalid code, Backspace and Delete.
  3. Open both dropdown lists and check whether a blank option is available.
- **Expected result:** Both dropdowns keep a valid listed currency; neither accepts typed invalid text or a blank selection. R2 is not directly testable through the GUI: this case checks prevention only. The required null/empty-code exception still needs a code-level test.

### TC-05 - Select supported currencies in both dropdowns
- **TC ID:** TC-05
- **Title:** Select supported currencies in both dropdowns
- **Requirement(s):** R4, R5
- **Type:** Positive
- **Priority:** Medium
- **Preconditions:** Converter is open with a dot-decimal locale.
- **Test data:** Amount: 100. Currency codes: USD, EUR, GBP, JPY, CAD, AUD, CHF.
- **Steps:**
  1. Enter 100 and keep To set to EUR.
  2. Select each listed currency in From and check the selected code.
  3. Set From to USD. Select each listed currency in To and check the selected code.
- **Expected result:** Every listed currency can be selected in both dropdowns. Each dropdown shows the selected code, and the amount remains 100.

### TC-06 - Convert to the same currency
- **TC ID:** TC-06
- **Title:** Convert to the same currency
- **Requirement(s):** R3, R4, R5, R7, R10, R11
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** Converter is open with a dot-decimal locale.
- **Test data:** Amount: 100; source: USD; target: USD.
- **Steps:**
  1. Enter 100.
  2. Select USD in both dropdowns.
  3. Read the converted amount and exchange rate.
- **Expected result:** The result is 100.00 and the rate is 1.000000. The accuracy error is zero and the result has 2 decimal places.

### TC-07 - Convert currencies with very different rates
- **TC ID:** TC-07
- **Title:** Convert currencies with very different rates
- **Requirement(s):** R7, R10, R11
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open with a dot-decimal locale.
- **Test data:** Amount: 1000. Run JPY -> GBP, then GBP -> JPY.
- **Steps:**
  1. Enter 1000 and select JPY -> GBP; read the result and rate.
  2. Change the pair to GBP -> JPY; read the new result and rate.
  3. For each pair, calculate Math.abs(result - amount * displayedRate).
- **Expected result:** JPY -> GBP shows 4.71 at rate 0.004707; GBP -> JPY shows 212440.76 at rate 212.440758. Both errors are within 0.01, and both results have 2 decimal places.

### TC-08 - Check decimal result display and preserve the entered amount
- **TC ID:** TC-08
- **Title:** Check decimal result display and preserve the entered amount
- **Requirement(s):** R3, R8, R9, R11 (R8/R9 are related display checks only)
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** Converter is open with a dot-decimal locale.
- **Test data:** Use USD -> USD. Amount / expected result text: 100.0 / "100.00"; 12.3 / "12.30"; 1.234 / "1.23"; 1.236 / "1.24".
- **Steps:**
  1. Select USD in both dropdowns and enter each listed amount in turn.
  2. Compare the displayed result with the expected result text and count its decimal places.
  3. Check that the amount field still contains the entered amount, including any extra decimals.
- **Expected result:** Each result matches the expected text and has 2 decimal places. The amount field keeps its entered text, including 1.234 and 1.236. This is a related display check for R8/R9; the internal formatting method and decimal counters cannot be inspected through the GUI.

### TC-09 - Convert a small positive amount
- **TC ID:** TC-09
- **Title:** Convert a small positive amount
- **Requirement(s):** R1, R3, R10, R11
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** Converter is open with a dot-decimal locale.
- **Test data:** Amount: 0.01; source: USD; target: USD.
- **Steps:**
  1. Enter 0.01.
  2. Select USD in both dropdowns.
  3. Read the result.
- **Expected result:** The amount is accepted. The result is 0.01 at rate 1.000000, with 2 decimal places and zero accuracy error.

### TC-10 - Convert a large amount
- **TC ID:** TC-10
- **Title:** Convert a large amount
- **Requirement(s):** R3, R7, R10, R11
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** Converter is open with a dot-decimal locale.
- **Test data:** Amount: 1000000; source: USD; target: USD.
- **Steps:**
  1. Enter 1000000.
  2. Select USD in both dropdowns.
  3. Read the full converted amount and exchange rate.
- **Expected result:** The result is 1000000.00 at rate 1.000000, without truncation. The accuracy error is zero and the result has 2 decimal places.

### TC-11 - Update the result and reset the amount
- **TC ID:** TC-11
- **Title:** Update the result and reset the amount
- **Requirement(s):** R12
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open with a dot-decimal locale.
- **Test data:** Source: USD; target: EUR; amount sequence: 100 -> 200 -> 100.
- **Steps:**
  1. Enter 100 with USD -> EUR and record the result 86.26.
  2. Change the amount to 200 and wait for the result to update.
  3. Reset the amount to 100 and check the amount, currencies and result.
- **Expected result:** The changed result is 172.52, different from the original. After reset, the amount is 100, the result is 86.26, and the currencies remain USD/EUR.

### TC-12 - Show the latest conversion after changing the inputs
- **TC ID:** TC-12
- **Title:** Show the latest conversion after changing the inputs
- **Requirement(s):** R3, R4, R5, R6, R7, R10, R11
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open with a dot-decimal locale.
- **Test data:** First: 100 USD -> EUR. Second: 250.75 USD -> GBP.
- **Steps:**
  1. Enter 100 and select USD -> EUR; wait for result 86.26.
  2. Replace the amount with 250.75 and select USD -> GBP; wait for the new result.
  3. Check the visible amount, both currency selections, converted amount and rate.
- **Expected result:** The screen shows amount 250.75, source USD, target GBP, result 187.97 and rate 0.749624. The accuracy error is approximately 0.001782, within 0.01; the result has 2 decimal places. The prior EUR result is replaced. Returned ConversionResult fields are not exposed by this screen.

### TC-13 - Check accuracy for a large cross-currency conversion
- **TC ID:** TC-13
- **Title:** Check accuracy for a large cross-currency conversion
- **Requirement(s):** R7, R10
- **Type:** Edge
- **Priority:** High
- **Preconditions:** Converter is open with a dot-decimal locale.
- **Test data:** Amount: 1000000.0; source: JPY; target: GBP.
- **Steps:**
  1. Enter 1000000.0, select JPY -> GBP, and read the displayed result and rate.
  2. Calculate Math.abs(result - 1000000.0 * displayedRate).
  3. Compare the error with 0.01 and record any accuracy failure.
- **Expected result:** With the current fixed rates, the expected display is 4707.19 at rate 0.004707. The error is approximately 0.19, so the R10 accuracy check fails. Record the failed accuracy check; keep the 0.01 tolerance. Internal status flags cannot be checked through the GUI.

### TC-14 - Check the visible update for amounts below one cent
- **TC ID:** TC-14
- **Title:** Check the visible update for amounts below one cent
- **Requirement(s):** R12
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** Converter is open with a dot-decimal locale.
- **Test data:** Source: USD; target: USD; amount sequence: 0.001 -> 0.002 -> 0.001.
- **Steps:**
  1. Enter 0.001 and select USD in both dropdowns; record the result.
  2. Change the amount to 0.002 and compare the displayed result with the original.
  3. Reset the amount to 0.001 and check the final amount and result.
- **Expected result:** Both displayed results are 0.00, so the R12 visible-update check cannot pass. Record this visible-update limitation. The amount is restored to 0.001 and the result remains 0.00. Internal update/completion flags cannot be inspected through the GUI.

## Traceability matrix

GUI means the required behaviour is observable on screen. Partial and related checks do not complete the requirement; the remaining checks need code-level tests. No execution or full requirement coverage is claimed.

| Requirement | GUI cases / related observations | Verification scope |
|---|---|---|
| R1 | TC-02, TC-03, TC-09 | Partial: UI rejection/acceptance; exception type needs a code-level test. |
| R2 | TC-04 (prevention only) | Not directly testable: null/empty-code exception needs a code-level test. |
| R3 | TC-01, TC-06, TC-08, TC-09, TC-10, TC-12 | GUI |
| R4 | TC-01, TC-05, TC-06, TC-12 | GUI |
| R5 | TC-01, TC-05, TC-06, TC-12 | GUI |
| R6 | TC-01, TC-12 | GUI |
| R7 | TC-01, TC-06, TC-07, TC-10, TC-12, TC-13 | GUI |
| R8 | TC-08 (related display) | Code-level test required for String.format usage. |
| R9 | TC-08 (result digits) | Partial: result digits are visible; internal counters need a code-level test. |
| R10 | TC-01, TC-06, TC-07, TC-09, TC-10, TC-12, TC-13 | GUI: calculate using the displayed rate. |
| R11 | TC-01, TC-06, TC-07, TC-08, TC-09, TC-10, TC-12 | GUI |
| R12 | TC-11, TC-14 | GUI: compare before/after results and restore the amount. |
| R13 | TC-08, TC-12 (related) | Code-level test required: inputAmount field. |
| R14 | TC-05, TC-12 (related) | Code-level test required: sourceCurrency field. |
| R15 | TC-05, TC-12 (related) | Code-level test required: targetCurrency field. |
| R16 | TC-01, TC-08, TC-12 (related) | Code-level test required: conversionResult field. |
| R17 | TC-08 (related) | Code-level test required: inputDecimalPlaces field. |
| R18 | TC-08 (related) | Code-level test required: resultDecimalPlaces field. |
| R19 | TC-01, TC-13 (related) | Code-level test required: conversionAccurate flag. |
| R20 | TC-01, TC-08 (related) | Code-level test required: decimalPrecisionMaintained flag. |
| R21 | TC-11, TC-14 (related) | Code-level test required: resultUpdatedOnChange flag. |
| R22 | TC-01, TC-11, TC-13, TC-14 (related) | Code-level test required: conversionComplete flag. |

## Assumptions and questions

- R1: the GUI can show rejection of zero/negative amounts, but it does not expose the exception type. R2: a null or empty currency cannot be selected. TC-04 checks GUI prevention only; the required exception is not directly testable through the GUI.
- R8/R9 need code-level checks for the formatting method and internal decimal counts. R13-R22 refer to a returned ConversionResult record that the GUI does not display. Visible values and behaviour are related checks, not proof of those record fields or boolean flags.
- 0.01 is a useful two-decimal test amount, not a stated minimum. The README accepts amounts greater than zero and gives no maximum.
- Use the displayed exchange rate in the 0.01 accuracy check. TC-13 and TC-14 cover real input values for which a required visible check can fail. Record those failures without changing the stated requirement.

Prepared with OpenAI Codex assistance. Submit the test cases for PD Team review before automation.
