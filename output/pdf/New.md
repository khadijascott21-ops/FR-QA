# Currency Converter - Combined Test Cases

22 test designs covering R1-R22. Each test-data row is a separate execution. The C in each ID identifies a combined case.

All cases are drafts, not executed. Cases requiring controlled results need a test fixture that exercises the actual assessment logic.

### TC-R1-C01 - Reject zero and negative amounts
- **TC ID:** TC-R1-C01
- **Title:** Reject zero and negative amounts.
- **Requirement(s):** R1
- **Type:** Negative / Boundary
- **Priority:** High
- **Preconditions:** ConversionAssessor.validate accepts numeric double inputs directly.
- **Test data:** Source = "USD"; target = "EUR".

| Amount | Purpose |
|---|---|
| 0.0 | Exact rejection boundary |
| -0.0 | Negative-zero edge case |
| -100.0 | Negative whole number |
| -0.01 | Negative fraction |
| -Double.MIN_VALUE | Negative value closest to zero |
| -Double.MAX_VALUE | Most negative finite value |

- **Steps:**
  1. Supply the amount and valid currency codes.
  2. Run input validation.
  3. Capture the exception.
  4. Repeat independently for each row.
- **Expected result:** Every row throws IllegalArgumentException.

### TC-R1-C02 - Accept positive amounts during validation
- **TC ID:** TC-R1-C02
- **Title:** Accept positive amounts during validation.
- **Requirement(s):** R1
- **Type:** Positive / Boundary
- **Priority:** High
- **Preconditions:** Numeric validation can be tested separately from GUI formatting and conversion arithmetic.
- **Test data:** Source = "USD"; target = "EUR".

| Amount | Purpose |
|---|---|
| Double.MIN_VALUE | Smallest positive value |
| 100.0 | Typical positive value |
| Double.MAX_VALUE | Largest finite positive value |

- **Steps:**
  1. Supply the amount directly, without formatting it.
  2. Run input validation.
  3. Check whether an exception occurs.
  4. Repeat independently for each row.
- **Expected result:** All amounts pass validation. This does not establish that later conversion or display operations succeed.

### TC-R2-C01 - Reject missing or empty currency codes
- **TC ID:** TC-R2-C01
- **Title:** Reject missing or empty currency codes.
- **Requirement(s):** R2
- **Type:** Negative
- **Priority:** High
- **Preconditions:** Validation accepts Java null and empty-string arguments directly.
- **Test data:** Amount = 100.0.

| Source | Target |
|---|---|
| null | "EUR" |
| "" | "EUR" |
| "USD" | null |
| "USD" | "" |
| null | null |
| "" | "" |

- **Steps:**
  1. Assign the source and target exactly as listed.
  2. Run input validation.
  3. Capture the exception.
  4. Repeat independently for each row.
- **Expected result:** Every row throws IllegalArgumentException. Here, null is not the text "null".

### TC-R2-C02 - Accept populated, valid currency codes
- **TC ID:** TC-R2-C02
- **Title:** Accept populated, valid currency codes.
- **Requirement(s):** R2
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Input validation is available.
- **Test data:** Amount = 100.0.

| Source | Target |
|---|---|
| "USD" | "EUR" |
| "USD" | "USD" |

- **Steps:**
  1. Supply the amount and currency codes.
  2. Run input validation.
  3. Check whether an exception occurs.
- **Expected result:** Both rows pass validation, including the same-currency pair.

### TC-R3-C01 - Enter amounts and verify their returned values
- **TC ID:** TC-R3-C01
- **Title:** Enter amounts and verify their returned values.
- **Requirement(s):** R3, R7, R13, R16
- **Type:** Positive / Edge
- **Priority:** High
- **Preconditions:** Converter is open with a dot-decimal locale. Source and target are both USD.
- **Test data:**

| Entered text | Expected inputAmount | Expected displayed amount / conversionResult |
|---|---|---|
| "100" | 100.0 | "100.00" / 100.0 |
| "12.50" | 12.5 | "12.50" / 12.5 |
| "0.01" | 0.01 | "0.01" / 0.01 |
| "1000000" | 1000000.0 | "1000000.00" / 1000000.0 |
| "1.234567" | 1.234567 | "1.23" / 1.23 |
| "12.3" | 12.3 | "12.30" / 12.3 |
| "1.234" | 1.234 | "1.23" / 1.23 |
| "12.34" | 12.34 | "12.34" / 12.34 |

- **Steps:**
  1. Clear the amount field and enter the listed text without quotation marks.
  2. Confirm the field preserves the entered text before invoking assessment.
  3. Run assessment using the corresponding numeric amount.
  4. Capture the baseline displayed result and exchange rate.
  5. Compare extracted values with their UI labels.
  6. Inspect inputAmount and conversionResult.
  7. Close or reset the converter.
- **Expected result:** Entry text is correct; inputAmount retains the original numeric value; conversionResult matches the displayed rounded amount. Extracted rate is 1.0.

### TC-R3-C02 - Replace or edit an amount without returning stale values
- **TC ID:** TC-R3-C02
- **Title:** Replace or edit an amount without returning stale values.
- **Requirement(s):** R3, R7, R13, R16
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open with USD to USD and a dot-decimal locale.
- **Test data:**

| Starting text | Action | Final text |
|---|---|---|
| "100" | Replace the entire value | "250" |
| "125" | Delete the last digit and type 0 | "120" |
| "100" | Replace the entire value | "250.75" |

- **Steps:**
  1. Enter the starting text and establish its conversion.
  2. Perform the listed edit.
  3. Verify the final field text.
  4. Assess the final numeric amount and inspect the returned record.
  5. Compare extracted and returned results with the final display.
  6. Close or reset the converter.
- **Expected result:** Final text matches the table. Returned input and conversion values correspond to the final amount, with no stale starting value.

### TC-R4-C01 - Select each source currency and verify its returned code
- **TC ID:** TC-R4-C01
- **Title:** Select each source currency and verify its returned code.
- **Requirement(s):** R4, R14
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open; amount = "100"; target = EUR. Start with a different source from the one being tested.
- **Test data:** Source selections: USD, EUR, GBP, JPY, CAD, AUD, CHF. Execute once for each currency.
- **Steps:**
  1. Focus the source dropdown.
  2. Press Enter, select the currency using arrow keys, and confirm with Enter.
  3. Read the selected source directly from the dropdown.
  4. Run assessment with that source and target EUR.
  5. Inspect sourceCurrency.
  6. Reset before testing the next currency.
- **Expected result:** Each currency can be selected. The dropdown and returned sourceCurrency both match the selected code. Amount remains 100 and target remains EUR.

### TC-R4-C02 - Preserve the latest source selection through changes and focus movement
- **TC ID:** TC-R4-C02
- **Title:** Preserve the latest source selection through changes and focus movement.
- **Requirement(s):** R4, R14
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open; amount = "100"; target = EUR; initial source = CHF.
- **Test data:**

| Selection sequence | Expected final source |
|---|---|
| EUR -> GBP -> JPY | JPY |
| GBP -> EUR | EUR |

- **Steps:**
  1. Select each source in the listed order.
  2. After each selection, press Tab to leave the dropdown.
  3. Verify the selection persists, then return focus for the next choice.
  4. Assess the final selection.
  5. Inspect sourceCurrency.
- **Expected result:** Every selection persists after focus moves. The final dropdown selection and returned field match the table, without retaining an earlier code.

### TC-R5-C01 - Select each target currency and verify its returned code
- **TC ID:** TC-R5-C01
- **Title:** Select each target currency and verify its returned code.
- **Requirement(s):** R5, R15
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open; amount = "100"; source = USD. Start with a different target from the one being tested.
- **Test data:** Target selections: USD, EUR, GBP, JPY, CAD, AUD, CHF. Execute once for each currency.
- **Steps:**
  1. Focus the target dropdown.
  2. Press Enter, select the currency using arrow keys, and confirm with Enter.
  3. Read the selected target directly from the dropdown.
  4. Run assessment with source USD and that target.
  5. Inspect targetCurrency.
  6. Reset before testing the next currency.
- **Expected result:** Each currency can be selected. The dropdown and returned targetCurrency match the selected code. Amount remains 100 and source remains USD.

### TC-R5-C02 - Preserve the latest target selection through changes and focus movement
- **TC ID:** TC-R5-C02
- **Title:** Preserve the latest target selection through changes and focus movement.
- **Requirement(s):** R5, R15
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open; amount = "100"; source = USD; initial target = CHF.
- **Test data:**

| Selection sequence | Expected final target |
|---|---|
| EUR -> GBP -> JPY | JPY |
| GBP -> EUR | EUR |

- **Steps:**
  1. Select each target in the listed order.
  2. After each selection, press Tab to leave the dropdown.
  3. Verify the selection persists, then return focus for the next choice.
  4. Assess the final selection.
  5. Inspect targetCurrency.
- **Expected result:** Every selection persists after focus moves. The final dropdown selection and returned field match the table.

### TC-R6-C01 - Wait successfully for valid and recovered results
- **TC ID:** TC-R6-C01
- **Title:** Wait successfully for valid and recovered results.
- **Requirement(s):** R6
- **Type:** Positive / Edge
- **Priority:** High
- **Preconditions:** Converter and waitForResult are available. Default timeout is five seconds.
- **Test data:**

| Initial amount | Final amount | Source to target |
|---|---|---|
| Empty | 100 | USD to EUR |
| Empty | 100 | USD to USD |
| 0 | 100 | USD to EUR |

- **Steps:**
  1. Set the currency pair and initial amount.
  2. Confirm the result container is hidden.
  3. Enter the final amount.
  4. Call waitForResult.
  5. Once visible, call waitForResult again without changing anything.
- **Expected result:** Both calls return true. The second succeeds when the container is already visible, without requiring another visibility transition.

### TC-R6-C02 - Handle delayed and missing results
- **TC ID:** TC-R6-C02
- **Title:** Handle delayed and missing results.
- **Requirement(s):** R6
- **Type:** Boundary / Negative
- **Priority:** High
- **Preconditions:** A controlled fixture can schedule visibility independently of the wait. Timeout is five seconds.
- **Test data:** Amount = 100; USD to EUR.

| Visibility behavior | Expected wait outcome |
|---|---|
| Hidden initially; visible after one second | true after visibility |
| Hidden throughout the timeout | false after timeout |

- **Steps:**
  1. Configure the listed visibility behavior.
  2. Start waiting while the container is hidden.
  3. Record the return value, elapsed time, and final visibility.
  4. Reset the fixture between rows.
- **Expected result:** The wait succeeds only after visibility occurs. A missing result returns false around the configured deadline, allowing normal scheduling overhead, and does not hang.

### TC-R7-C01 - Extract displayed amounts and exchange rates correctly
- **TC ID:** TC-R7-C01
- **Title:** Extract displayed amounts and exchange rates correctly.
- **Requirement(s):** R7, R16
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open with a dot-decimal locale and the supplied fixed currency rates.
- **Test data:** Amount = 100.

| Source to target | Expected amount text | Expected rate text |
|---|---|---|
| USD to EUR | "86.26" | "0.862623" |
| USD to USD | "100.00" | "1.000000" |
| JPY to GBP | "0.47" | "0.004707" |

- **Steps:**
  1. Assess the listed conversion.
  2. Capture the baseline amount and rate labels before the temporary update probe.
  3. Extract and parse both displayed values.
  4. Compare extracted values with the recorded labels.
  5. Inspect conversionResult.
- **Expected result:** Displayed strings match the table. Extraction retains all displayed numeric digits, and conversionResult matches the baseline displayed amount.

### TC-R7-C02 - Extract current values after an input change
- **TC ID:** TC-R7-C02
- **Title:** Extract current values after an input change.
- **Requirement(s):** R7, R16
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Establish a visible conversion for 100, USD to USD.
- **Test data:**

| Change | Expected amount | Expected rate |
|---|---|---|
| Change amount to 200 | 200.0 | 1.0 |
| Keep amount 100; change target to EUR | 86.26 | 0.862623 |

- **Steps:**
  1. Restore the starting conversion before each row.
  2. Make the listed change.
  3. Wait until the displayed contents reflect the change.
  4. Extract the amount and rate.
  5. Assess the final inputs and inspect conversionResult.
- **Expected result:** Extracted values and the returned conversion amount match the updated conversion. No earlier amount or rate is returned.

### TC-R8-C01 - Format input and return the correct input decimal count
- **TC ID:** TC-R8-C01
- **Title:** Format input and return the correct input decimal count.
- **Requirement(s):** R8, R9, R13, R17
- **Type:** Positive / Boundary / Edge
- **Priority:** High
- **Preconditions:** Dot-decimal locale is fixed. The assessment's formatted-input string can be observed through a test fixture or debugger. Use USD to USD.
- **Test data:**

| Numeric input | Expected formatted string |
|---|---|
| 100.0 | "100.00" |
| 12.5 | "12.50" |
| 12.34 | "12.34" |
| 12.344 | "12.34" |
| 12.346 | "12.35" |
| 1.125 | "1.13" |
| 9.999 | "10.00" |
| 0.001 | "0.00" |
| 1.234 | "1.23" |
| 1000000.0 | "1000000.00" |

- **Steps:**
  1. Assess the original numeric input.
  2. Capture the formatted input produced by String.format("%.2f", amount).
  3. Compare it with the expected string.
  4. Count its fractional digits independently.
  5. Inspect inputDecimalPlaces and inputAmount.
- **Expected result:** The formatted string matches the table; its count and inputDecimalPlaces are both 2. inputAmount retains the original numeric input, including digits removed by formatting.

### TC-R9-C01 - Count result decimals and return truthful precision fields
- **TC ID:** TC-R9-C01
- **Title:** Count result decimals and return truthful precision fields.
- **Requirement(s):** R9, R11, R18, R20, R22
- **Type:** Positive / Negative / Boundary
- **Priority:** High
- **Preconditions:** A controlled assessment fixture supplies exact result strings. Visibility, accuracy, and dynamic update/restoration pass independently. Use valid USD to USD codes and a fixed dot-decimal locale.
- **Test data:**

| Input | Result text | Result decimal count | Precision flag |
|---|---|---|---|
| 100 | "92.35" | 2 | true |
| 12.5 | "11.50" | 2 | true |
| 1.234 | "1.1400" | 4 | true |
| 100 | "92.350" | 3 | true |
| 100 | "92.3" | 1 | false |
| 100 | "92" | 0 | false |
| 0.001 | "0.0001" | 4 | true |
| 1 | "0.00" | 2 | true |

- **Steps:**
  1. Configure the baseline result string exactly as listed.
  2. Supply a controlled rate that makes baseline accuracy pass.
  3. Arrange a changed result distinct from baseline and an exact restoration.
  4. Run the actual assessment path.
  5. Count decimals independently in the formatted input and baseline result.
  6. Inspect resultDecimalPlaces, decimalPrecisionMaintained, and conversionComplete.
- **Expected result:** Input decimal count is 2. Result count and precision flag match the table. Because other completion conditions pass, conversionComplete equals the precision flag.

### TC-R10-C01 - Validate accuracy and return truthful accuracy and completion flags
- **TC ID:** TC-R10-C01
- **Title:** Validate accuracy and return truthful accuracy and completion flags.
- **Requirement(s):** R10, R19, R22
- **Type:** Positive / Negative / Boundary
- **Priority:** High
- **Preconditions:** A controlled assessment fixture supplies the listed amount, displayed rate, and result. Visibility, precision, and update/restoration pass. Use valid USD to USD codes.
- **Test data:**

| Amount | Rate | Result text | Expected accurate |
|---|---|---|---|
| 1 | 1 | "1.000" | true |
| 1 | 1 | "1.009" | true |
| 1 | 1 | "0.991" | true |
| 1 | 0.01 | "0.00" | true |
| 1 | 1 | "1.011" | false |
| 1 | 1 | "0.989" | false |

- **Steps:**
  1. Configure the fixture with the listed baseline values.
  2. Arrange a distinct changed result and an exact baseline restoration.
  3. Run the actual assessment path.
  4. Independently calculate Math.abs(result - amount * rate).
  5. Compare the difference with 0.01.
  6. Inspect conversionAccurate and conversionComplete.
- **Expected result:** Both flags match the table because all other completion conditions pass. The fourth row tests equality at the tolerance boundary without subtracting nearly equal numbers.

### TC-R12-C01 - Update and restore a conversion successfully
- **TC ID:** TC-R12-C01
- **Title:** Update and restore a conversion successfully.
- **Requirement(s):** R12, R21, R22
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open; baseline visibility, accuracy, and precision pass.
- **Test data:**

| Source to target | Original -> changed -> restored amount |
|---|---|
| USD to USD | 100 -> 200 -> 100 |
| USD to USD | 12.5 -> 25 -> 12.5 |
| USD to EUR | 100 -> 200 -> 100 |

- **Steps:**
  1. Run assessment using the original amount and listed currencies.
  2. Observe the baseline result.
  3. Observe the assessor doubling the amount and obtaining a different result.
  4. Observe restoration of the original amount and result.
  5. Inspect resultUpdatedOnChange and conversionComplete.
  6. Verify the original numeric amount and currencies are restored.
- **Expected result:** Changed result differs from baseline; restored result equals baseline. Both flags are true, and original inputs are restored.

### TC-R12-C02 - Handle decreasing and repeated amount changes
- **TC ID:** TC-R12-C02
- **Title:** Handle decreasing and repeated amount changes.
- **Requirement(s):** R12
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open with USD to USD. Driver operations can change amounts directly.
- **Test data:**

| Amount sequence | Expected result sequence |
|---|---|
| 100 -> 50 -> 100 | "100.00" -> "50.00" -> "100.00" |
| 100 -> 200 -> 300 -> 100 | "100.00" -> "200.00" -> "300.00" -> "100.00" |

- **Steps:**
  1. Establish and record the original amount and result.
  2. Enter each subsequent amount in order.
  3. Wait for the corresponding result after each change.
  4. Restore the exact original amount text.
  5. Check final amount, result, and currencies.
- **Expected result:** Every result matches the latest input. Final amount and result equal their originals. These sequences are checked separately because the supplied update helper only doubles the amount.

### TC-R12-C03 - Reject unsuccessful updates or restoration
- **TC ID:** TC-R12-C03
- **Title:** Reject unsuccessful updates or restoration.
- **Requirement(s):** R12, R21, R22
- **Type:** Negative / Edge
- **Priority:** High
- **Preconditions:** A controlled fixture can supply frozen or incorrectly restored results. Baseline visibility, precision, and accuracy pass. Use USD to USD with displayed rate 1.
- **Test data:**

| Situation | Original amount | Baseline -> changed -> restored result |
|---|---|---|
| Frozen result | 100 | "100.00" -> "100.00" -> "100.00" |
| Change hidden by rounding | 0.001 | "0.00" -> "0.00" -> "0.00" |
| Failed restoration | 100 | "100.00" -> "200.00" -> "150.00" |

- **Steps:**
  1. Configure the listed result sequence; the rounding row can also use the real UI.
  2. Run assessment with the original amount.
  3. Confirm the probe attempts twice the amount, followed by the original amount.
  4. Compare baseline, changed, and restored strings.
  5. Inspect resultUpdatedOnChange and conversionComplete.
  6. Close the converter to clear any failed-restoration state.
- **Expected result:** Both flags are false. An unchanged display or unsuccessful restoration must not be reported as a successful dynamic update.

### TC-R22-C01 - Reject incomplete conversions when visibility or multiple checks fail
- **TC ID:** TC-R22-C01
- **Title:** Reject incomplete conversions when visibility or multiple checks fail.
- **Requirement(s):** R22
- **Type:** Negative
- **Priority:** High
- **Preconditions:** A controlled assessment fixture can return visibility outcomes and parseable result strings. Amount = 100; source = USD; target = USD; rate = 1.
- **Test data:**

| Situation | Visibility | Baseline -> changed -> restored result |
|---|---|---|
| Initial visibility wait fails | Initial wait false; later probe waits true | "100.00" -> "200.00" -> "100.00" |
| Accuracy and precision both fail | true | "100.1" -> "200.1" -> "100.1" |

- **Steps:**
  1. Configure the listed visibility responses and result strings.
  2. Run the actual assessment path.
  3. Independently verify which conditions pass and fail.
  4. Inspect conversionComplete.
- **Expected result:** conversionComplete is false for both rows. The first isolates failed visibility; the second verifies combined accuracy and precision failures.

### TC-R22-C02 - Reject completion when a returned currency disagrees with the selection
- **TC ID:** TC-R22-C02
- **Title:** Reject completion when a returned currency disagrees with the selection.
- **Requirement(s):** R14, R22
- **Type:** Negative
- **Priority:** High
- **Preconditions:** PD review confirms that R22 includes returned-field correctness. A controlled selection fault can make the actual source differ from the requested source before the record is created.
- **Test data:** Amount = 100; requested source = USD; actual selected source = EUR; target = USD. Controlled visibility, accuracy, precision, and update checks all pass.
- **Steps:**
  1. Configure the source-selection fault.
  2. Run assessment requesting USD to USD.
  3. Read the actual source selection independently.
  4. Compare it with returned sourceCurrency.
  5. Inspect conversionComplete.
- **Expected result:** Under the stated interpretation, a record with an incorrect source field must not report successful completion. Record any contrary behavior as a defect. This case remains review-dependent because the current completion calculation does not explicitly check field correctness.

## Requirement mapping

| Requirement | Combined cases |
|---|---|
| R1 | TC-R1-C01, TC-R1-C02 |
| R2 | TC-R2-C01, TC-R2-C02 |
| R3 | TC-R3-C01, TC-R3-C02 |
| R4 | TC-R4-C01, TC-R4-C02 |
| R5 | TC-R5-C01, TC-R5-C02 |
| R6 | TC-R6-C01, TC-R6-C02 |
| R7 | TC-R3-C01, TC-R3-C02, TC-R7-C01, TC-R7-C02 |
| R8 | TC-R8-C01 |
| R9 | TC-R8-C01, TC-R9-C01 |
| R10 | TC-R10-C01 |
| R11 | TC-R9-C01 |
| R12 | TC-R12-C01, TC-R12-C02, TC-R12-C03 |
| R13 | TC-R3-C01, TC-R3-C02, TC-R8-C01 |
| R14 | TC-R4-C01, TC-R4-C02, TC-R22-C02 |
| R15 | TC-R5-C01, TC-R5-C02 |
| R16 | TC-R3-C01, TC-R3-C02, TC-R7-C01, TC-R7-C02 |
| R17 | TC-R8-C01 |
| R18 | TC-R9-C01 |
| R19 | TC-R10-C01 |
| R20 | TC-R9-C01 |
| R21 | TC-R12-C01, TC-R12-C03 |
| R22 | TC-R9-C01, TC-R10-C01, TC-R12-C01, TC-R12-C03, TC-R22-C01, TC-R22-C02 |
