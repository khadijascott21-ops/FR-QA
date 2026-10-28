# Currency Converter - R1-R22 Test Cases

152 individually documented test cases covering all 22 requirements.

Status: Draft. No test execution, automation or PD Team approval is claimed.

Each case uses the README template: TC ID, Title, Requirement(s), Type, Priority, Preconditions, Test data, numbered Steps, and Expected result. Numbering restarts for each requirement.

The preconditions, data and steps are repeated within every case so it can be reviewed or executed independently. High priority is assigned to positive, negative and boundary cases; Edge cases are Medium.

Controlled-fixture designs are explicitly identified. Mark them Not Run until a suitable fixture is available; no changes to application code or dependencies are authorized by this document.

Use Locale.ROOT or an equivalent dot-decimal locale. Quotes denote strings; do not type them into the amount field. Keep the original numeric input separate from the formatted input and displayed result strings.

Prepared October 16, 2026 (America/Phoenix). OpenAI Codex assisted with test design and formatting. This document retains all 152 case IDs from the prior catalog.

## R1 - Reject amounts less than or equal to zero

### TC-R1-01 - Reject zero
- **TC ID:** TC-R1-01
- **Title:** Reject zero
- **Requirement(s):** R1
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** ConversionAssessor.validate is callable with Java double values; no GUI is required.
- **Test data:** amount=0.0; source="USD"; target="EUR".
- **Steps:**
  1. Set amount to 0.0 without formatting or conversion.
  2. Call ConversionAssessor.validate(amount, "USD", "EUR").
  3. Capture any exception and compare its type, or absence, with the expected result.
  4. Discard the validation inputs; no GUI state was created.
- **Expected result:** Throws IllegalArgumentException.

### TC-R1-02 - Reject negative zero
- **TC ID:** TC-R1-02
- **Title:** Reject negative zero
- **Requirement(s):** R1
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** ConversionAssessor.validate is callable with Java double values; no GUI is required.
- **Test data:** amount=-0.0; source="USD"; target="EUR".
- **Steps:**
  1. Set amount to -0.0 without formatting or conversion.
  2. Call ConversionAssessor.validate(amount, "USD", "EUR").
  3. Capture any exception and compare its type, or absence, with the expected result.
  4. Discard the validation inputs; no GUI state was created.
- **Expected result:** Throws IllegalArgumentException.

### TC-R1-03 - Reject negative whole amount
- **TC ID:** TC-R1-03
- **Title:** Reject negative whole amount
- **Requirement(s):** R1
- **Type:** Negative
- **Priority:** High
- **Preconditions:** ConversionAssessor.validate is callable with Java double values; no GUI is required.
- **Test data:** amount=-100.0; source="USD"; target="EUR".
- **Steps:**
  1. Set amount to -100.0 without formatting or conversion.
  2. Call ConversionAssessor.validate(amount, "USD", "EUR").
  3. Capture any exception and compare its type, or absence, with the expected result.
  4. Discard the validation inputs; no GUI state was created.
- **Expected result:** Throws IllegalArgumentException.

### TC-R1-04 - Reject negative fraction
- **TC ID:** TC-R1-04
- **Title:** Reject negative fraction
- **Requirement(s):** R1
- **Type:** Negative
- **Priority:** High
- **Preconditions:** ConversionAssessor.validate is callable with Java double values; no GUI is required.
- **Test data:** amount=-0.01; source="USD"; target="EUR".
- **Steps:**
  1. Set amount to -0.01 without formatting or conversion.
  2. Call ConversionAssessor.validate(amount, "USD", "EUR").
  3. Capture any exception and compare its type, or absence, with the expected result.
  4. Discard the validation inputs; no GUI state was created.
- **Expected result:** Throws IllegalArgumentException.

### TC-R1-05 - Reject negative value nearest zero
- **TC ID:** TC-R1-05
- **Title:** Reject negative value nearest zero
- **Requirement(s):** R1
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** ConversionAssessor.validate is callable with Java double values; no GUI is required.
- **Test data:** amount=-Double.MIN_VALUE; source="USD"; target="EUR".
- **Steps:**
  1. Set amount to -Double.MIN_VALUE without formatting or conversion.
  2. Call ConversionAssessor.validate(amount, "USD", "EUR").
  3. Capture any exception and compare its type, or absence, with the expected result.
  4. Discard the validation inputs; no GUI state was created.
- **Expected result:** Throws IllegalArgumentException.

### TC-R1-06 - Reject most negative finite value
- **TC ID:** TC-R1-06
- **Title:** Reject most negative finite value
- **Requirement(s):** R1
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** ConversionAssessor.validate is callable with Java double values; no GUI is required.
- **Test data:** amount=-Double.MAX_VALUE; source="USD"; target="EUR".
- **Steps:**
  1. Set amount to -Double.MAX_VALUE without formatting or conversion.
  2. Call ConversionAssessor.validate(amount, "USD", "EUR").
  3. Capture any exception and compare its type, or absence, with the expected result.
  4. Discard the validation inputs; no GUI state was created.
- **Expected result:** Throws IllegalArgumentException.

### TC-R1-07 - Accept smallest positive value
- **TC ID:** TC-R1-07
- **Title:** Accept smallest positive value
- **Requirement(s):** R1
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** ConversionAssessor.validate is callable with Java double values; no GUI is required.
- **Test data:** amount=Double.MIN_VALUE; source="USD"; target="EUR".
- **Steps:**
  1. Set amount to Double.MIN_VALUE without formatting or conversion.
  2. Call ConversionAssessor.validate(amount, "USD", "EUR").
  3. Capture any exception and compare its type, or absence, with the expected result.
  4. Discard the validation inputs; no GUI state was created.
- **Expected result:** Passes amount validation.

### TC-R1-08 - Accept typical positive amount
- **TC ID:** TC-R1-08
- **Title:** Accept typical positive amount
- **Requirement(s):** R1
- **Type:** Positive
- **Priority:** High
- **Preconditions:** ConversionAssessor.validate is callable with Java double values; no GUI is required.
- **Test data:** amount=100.0; source="USD"; target="EUR".
- **Steps:**
  1. Set amount to 100.0 without formatting or conversion.
  2. Call ConversionAssessor.validate(amount, "USD", "EUR").
  3. Capture any exception and compare its type, or absence, with the expected result.
  4. Discard the validation inputs; no GUI state was created.
- **Expected result:** Passes amount validation.

### TC-R1-09 - Accept largest finite positive value
- **TC ID:** TC-R1-09
- **Title:** Accept largest finite positive value
- **Requirement(s):** R1
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** ConversionAssessor.validate is callable with Java double values; no GUI is required.
- **Test data:** amount=Double.MAX_VALUE; source="USD"; target="EUR".
- **Steps:**
  1. Set amount to Double.MAX_VALUE without formatting or conversion.
  2. Call ConversionAssessor.validate(amount, "USD", "EUR").
  3. Capture any exception and compare its type, or absence, with the expected result.
  4. Discard the validation inputs; no GUI state was created.
- **Expected result:** Passes amount validation.

## R2 - Reject null or empty currency codes

### TC-R2-01 - Missing source
- **TC ID:** TC-R2-01
- **Title:** Missing source
- **Requirement(s):** R2
- **Type:** Negative
- **Priority:** High
- **Preconditions:** ConversionAssessor.validate is callable; Java null and empty strings can be supplied directly.
- **Test data:** amount=100.0; source=null; target=EUR
- **Steps:**
  1. Assign the source and target exactly as listed; null is not the text "null".
  2. Call ConversionAssessor.validate(100.0, source, target).
  3. Capture any exception and compare its type, or absence, with the expected result.
  4. Discard the validation inputs; no GUI state was created.
- **Expected result:** Throws IllegalArgumentException.

### TC-R2-02 - Empty source
- **TC ID:** TC-R2-02
- **Title:** Empty source
- **Requirement(s):** R2
- **Type:** Negative
- **Priority:** High
- **Preconditions:** ConversionAssessor.validate is callable; Java null and empty strings can be supplied directly.
- **Test data:** amount=100.0; source=""; target=EUR
- **Steps:**
  1. Assign the source and target exactly as listed; null is not the text "null".
  2. Call ConversionAssessor.validate(100.0, source, target).
  3. Capture any exception and compare its type, or absence, with the expected result.
  4. Discard the validation inputs; no GUI state was created.
- **Expected result:** Throws IllegalArgumentException.

### TC-R2-03 - Missing target
- **TC ID:** TC-R2-03
- **Title:** Missing target
- **Requirement(s):** R2
- **Type:** Negative
- **Priority:** High
- **Preconditions:** ConversionAssessor.validate is callable; Java null and empty strings can be supplied directly.
- **Test data:** amount=100.0; source=USD; target=null
- **Steps:**
  1. Assign the source and target exactly as listed; null is not the text "null".
  2. Call ConversionAssessor.validate(100.0, source, target).
  3. Capture any exception and compare its type, or absence, with the expected result.
  4. Discard the validation inputs; no GUI state was created.
- **Expected result:** Throws IllegalArgumentException.

### TC-R2-04 - Empty target
- **TC ID:** TC-R2-04
- **Title:** Empty target
- **Requirement(s):** R2
- **Type:** Negative
- **Priority:** High
- **Preconditions:** ConversionAssessor.validate is callable; Java null and empty strings can be supplied directly.
- **Test data:** amount=100.0; source=USD; target=""
- **Steps:**
  1. Assign the source and target exactly as listed; null is not the text "null".
  2. Call ConversionAssessor.validate(100.0, source, target).
  3. Capture any exception and compare its type, or absence, with the expected result.
  4. Discard the validation inputs; no GUI state was created.
- **Expected result:** Throws IllegalArgumentException.

### TC-R2-05 - Both missing
- **TC ID:** TC-R2-05
- **Title:** Both missing
- **Requirement(s):** R2
- **Type:** Negative
- **Priority:** High
- **Preconditions:** ConversionAssessor.validate is callable; Java null and empty strings can be supplied directly.
- **Test data:** amount=100.0; source=null; target=null
- **Steps:**
  1. Assign the source and target exactly as listed; null is not the text "null".
  2. Call ConversionAssessor.validate(100.0, source, target).
  3. Capture any exception and compare its type, or absence, with the expected result.
  4. Discard the validation inputs; no GUI state was created.
- **Expected result:** Throws IllegalArgumentException.

### TC-R2-06 - Both empty
- **TC ID:** TC-R2-06
- **Title:** Both empty
- **Requirement(s):** R2
- **Type:** Negative
- **Priority:** High
- **Preconditions:** ConversionAssessor.validate is callable; Java null and empty strings can be supplied directly.
- **Test data:** amount=100.0; source=""; target=""
- **Steps:**
  1. Assign the source and target exactly as listed; null is not the text "null".
  2. Call ConversionAssessor.validate(100.0, source, target).
  3. Capture any exception and compare its type, or absence, with the expected result.
  4. Discard the validation inputs; no GUI state was created.
- **Expected result:** Throws IllegalArgumentException.

### TC-R2-07 - Valid different currencies
- **TC ID:** TC-R2-07
- **Title:** Valid different currencies
- **Requirement(s):** R2
- **Type:** Positive
- **Priority:** High
- **Preconditions:** ConversionAssessor.validate is callable; Java null and empty strings can be supplied directly.
- **Test data:** amount=100.0; source=USD; target=EUR
- **Steps:**
  1. Assign the source and target exactly as listed; null is not the text "null".
  2. Call ConversionAssessor.validate(100.0, source, target).
  3. Capture any exception and compare its type, or absence, with the expected result.
  4. Discard the validation inputs; no GUI state was created.
- **Expected result:** Validation passes.

### TC-R2-08 - Same valid currency
- **TC ID:** TC-R2-08
- **Title:** Same valid currency
- **Requirement(s):** R2
- **Type:** Positive
- **Priority:** High
- **Preconditions:** ConversionAssessor.validate is callable; Java null and empty strings can be supplied directly.
- **Test data:** amount=100.0; source=USD; target=USD
- **Steps:**
  1. Assign the source and target exactly as listed; null is not the text "null".
  2. Call ConversionAssessor.validate(100.0, source, target).
  3. Capture any exception and compare its type, or absence, with the expected result.
  4. Discard the validation inputs; no GUI state was created.
- **Expected result:** Validation passes.

## R3 - Enter the amount into the amount field

### TC-R3-01 - Whole number
- **TC ID:** TC-R3-01
- **Title:** Whole number
- **Requirement(s):** R3
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** source="USD"; target="EUR"; Enter "100".
- **Steps:**
  1. Set source to USD and target to EUR; focus and clear the amount field.
  2. Enter "100".
  3. Read the complete amount-field text and compare it character for character with the expected result.
  4. Verify source is still USD and target is still EUR.
  5. Close the converter and discard this case's state.
- **Expected result:** Field contains "100".

### TC-R3-02 - Decimal amount
- **TC ID:** TC-R3-02
- **Title:** Decimal amount
- **Requirement(s):** R3
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** source="USD"; target="EUR"; Enter "12.50".
- **Steps:**
  1. Set source to USD and target to EUR; focus and clear the amount field.
  2. Enter "12.50".
  3. Read the complete amount-field text and compare it character for character with the expected result.
  4. Verify source is still USD and target is still EUR.
  5. Close the converter and discard this case's state.
- **Expected result:** Field contains "12.50", including the trailing zero.

### TC-R3-03 - Small positive amount
- **TC ID:** TC-R3-03
- **Title:** Small positive amount
- **Requirement(s):** R3
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** source="USD"; target="EUR"; Enter "0.01".
- **Steps:**
  1. Set source to USD and target to EUR; focus and clear the amount field.
  2. Enter "0.01".
  3. Read the complete amount-field text and compare it character for character with the expected result.
  4. Verify source is still USD and target is still EUR.
  5. Close the converter and discard this case's state.
- **Expected result:** Field contains "0.01".

### TC-R3-04 - Large amount
- **TC ID:** TC-R3-04
- **Title:** Large amount
- **Requirement(s):** R3
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** source="USD"; target="EUR"; Enter "1000000".
- **Steps:**
  1. Set source to USD and target to EUR; focus and clear the amount field.
  2. Enter "1000000".
  3. Read the complete amount-field text and compare it character for character with the expected result.
  4. Verify source is still USD and target is still EUR.
  5. Close the converter and discard this case's state.
- **Expected result:** Complete value is present without truncation.

### TC-R3-05 - Several decimal places
- **TC ID:** TC-R3-05
- **Title:** Several decimal places
- **Requirement(s):** R3
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** source="USD"; target="EUR"; Enter "1.234567".
- **Steps:**
  1. Set source to USD and target to EUR; focus and clear the amount field.
  2. Enter "1.234567".
  3. Read the complete amount-field text and compare it character for character with the expected result.
  4. Verify source is still USD and target is still EUR.
  5. Close the converter and discard this case's state.
- **Expected result:** Complete text remains without entry-time rounding.

### TC-R3-06 - Replace amount
- **TC ID:** TC-R3-06
- **Title:** Replace amount
- **Requirement(s):** R3
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** source="USD"; target="EUR"; Enter "100", then replace with "250".
- **Steps:**
  1. Set source to USD and target to EUR; focus and clear the amount field.
  2. Enter "100", then replace with "250".
  3. Read the complete amount-field text and compare it character for character with the expected result.
  4. Verify source is still USD and target is still EUR.
  5. Close the converter and discard this case's state.
- **Expected result:** Field contains only "250".

### TC-R3-07 - Edit amount
- **TC ID:** TC-R3-07
- **Title:** Edit amount
- **Requirement(s):** R3
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** source="USD"; target="EUR"; Enter "125", delete final digit, then type "0".
- **Steps:**
  1. Set source to USD and target to EUR; focus and clear the amount field.
  2. Enter "125", delete final digit, then type "0".
  3. Read the complete amount-field text and compare it character for character with the expected result.
  4. Verify source is still USD and target is still EUR.
  5. Close the converter and discard this case's state.
- **Expected result:** Field contains "120".

## R4 - Select the source currency

### TC-R4-01 - Select USD
- **TC ID:** TC-R4-01
- **Title:** Select USD
- **Requirement(s):** R4
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount="100"; target=EUR; starting source=CHF; Choose USD in the source dropdown.
- **Steps:**
  1. Enter amount 100, set target to EUR, and set the starting source to CHF.
  2. Focus the source dropdown.
  3. Press Enter on the source dropdown, use arrow keys to highlight USD, and press Enter to select it.
  4. Read the final source selection; confirm amount remains 100 and target remains EUR.
  5. Close the converter and discard this case's state.
- **Expected result:** Selected source displays USD.

### TC-R4-02 - Select EUR
- **TC ID:** TC-R4-02
- **Title:** Select EUR
- **Requirement(s):** R4
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount="100"; target=EUR; starting source=CHF; Choose EUR in the source dropdown.
- **Steps:**
  1. Enter amount 100, set target to EUR, and set the starting source to CHF.
  2. Focus the source dropdown.
  3. Press Enter on the source dropdown, use arrow keys to highlight EUR, and press Enter to select it.
  4. Read the final source selection; confirm amount remains 100 and target remains EUR.
  5. Close the converter and discard this case's state.
- **Expected result:** Selected source displays EUR.

### TC-R4-03 - Select GBP
- **TC ID:** TC-R4-03
- **Title:** Select GBP
- **Requirement(s):** R4
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount="100"; target=EUR; starting source=CHF; Choose GBP in the source dropdown.
- **Steps:**
  1. Enter amount 100, set target to EUR, and set the starting source to CHF.
  2. Focus the source dropdown.
  3. Press Enter on the source dropdown, use arrow keys to highlight GBP, and press Enter to select it.
  4. Read the final source selection; confirm amount remains 100 and target remains EUR.
  5. Close the converter and discard this case's state.
- **Expected result:** Selected source displays GBP.

### TC-R4-04 - Select JPY
- **TC ID:** TC-R4-04
- **Title:** Select JPY
- **Requirement(s):** R4
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount="100"; target=EUR; starting source=CHF; Choose JPY in the source dropdown.
- **Steps:**
  1. Enter amount 100, set target to EUR, and set the starting source to CHF.
  2. Focus the source dropdown.
  3. Press Enter on the source dropdown, use arrow keys to highlight JPY, and press Enter to select it.
  4. Read the final source selection; confirm amount remains 100 and target remains EUR.
  5. Close the converter and discard this case's state.
- **Expected result:** Selected source displays JPY.

### TC-R4-05 - Select CAD
- **TC ID:** TC-R4-05
- **Title:** Select CAD
- **Requirement(s):** R4
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount="100"; target=EUR; starting source=CHF; Choose CAD in the source dropdown.
- **Steps:**
  1. Enter amount 100, set target to EUR, and set the starting source to CHF.
  2. Focus the source dropdown.
  3. Press Enter on the source dropdown, use arrow keys to highlight CAD, and press Enter to select it.
  4. Read the final source selection; confirm amount remains 100 and target remains EUR.
  5. Close the converter and discard this case's state.
- **Expected result:** Selected source displays CAD.

### TC-R4-06 - Select AUD
- **TC ID:** TC-R4-06
- **Title:** Select AUD
- **Requirement(s):** R4
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount="100"; target=EUR; starting source=CHF; Choose AUD in the source dropdown.
- **Steps:**
  1. Enter amount 100, set target to EUR, and set the starting source to CHF.
  2. Focus the source dropdown.
  3. Press Enter on the source dropdown, use arrow keys to highlight AUD, and press Enter to select it.
  4. Read the final source selection; confirm amount remains 100 and target remains EUR.
  5. Close the converter and discard this case's state.
- **Expected result:** Selected source displays AUD.

### TC-R4-07 - Select CHF
- **TC ID:** TC-R4-07
- **Title:** Select CHF
- **Requirement(s):** R4
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount="100"; target=EUR; starting source=USD; Choose CHF in the source dropdown.
- **Steps:**
  1. Enter amount 100, set target to EUR, and set the starting source to USD.
  2. Focus the source dropdown.
  3. Press Enter on the source dropdown, use arrow keys to highlight CHF, and press Enter to select it.
  4. Read the final source selection; confirm amount remains 100 and target remains EUR.
  5. Close the converter and discard this case's state.
- **Expected result:** Selected source displays CHF.

### TC-R4-08 - Repeated selection
- **TC ID:** TC-R4-08
- **Title:** Repeated selection
- **Requirement(s):** R4
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount="100"; target=EUR; starting source=CHF; Choose EUR, then GBP, then JPY.
- **Steps:**
  1. Enter amount 100, set target to EUR, and set the starting source to CHF.
  2. Focus the source dropdown.
  3. Open the source dropdown with Enter and select EUR using arrow keys and Enter; repeat for GBP, then JPY. Check the displayed selection after each choice.
  4. Read the final source selection; confirm amount remains 100 and target remains EUR.
  5. Close the converter and discard this case's state.
- **Expected result:** Each selection is displayed; final source is JPY.

### TC-R4-09 - Preserve selection on blur
- **TC ID:** TC-R4-09
- **Title:** Preserve selection on blur
- **Requirement(s):** R4
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount="100"; target=EUR; starting source=CHF; Choose GBP, then press Tab.
- **Steps:**
  1. Enter amount 100, set target to EUR, and set the starting source to CHF.
  2. Focus the source dropdown.
  3. Open the source dropdown with Enter, select GBP using arrow keys and Enter, then press Tab to leave it.
  4. Read the final source selection; confirm amount remains 100 and target remains EUR.
  5. Close the converter and discard this case's state.
- **Expected result:** Selected source remains GBP.

## R5 - Select the target currency

### TC-R5-01 - Select USD
- **TC ID:** TC-R5-01
- **Title:** Select USD
- **Requirement(s):** R5
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount="100"; source=USD; starting target=CHF; Choose USD in the target dropdown.
- **Steps:**
  1. Enter amount 100, set source to USD, and set the starting target to CHF.
  2. Focus the target dropdown.
  3. Press Enter on the target dropdown, use arrow keys to highlight USD, and press Enter to select it.
  4. Read the final target selection; confirm amount remains 100 and source remains USD.
  5. Close the converter and discard this case's state.
- **Expected result:** Selected target displays USD.

### TC-R5-02 - Select EUR
- **TC ID:** TC-R5-02
- **Title:** Select EUR
- **Requirement(s):** R5
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount="100"; source=USD; starting target=CHF; Choose EUR in the target dropdown.
- **Steps:**
  1. Enter amount 100, set source to USD, and set the starting target to CHF.
  2. Focus the target dropdown.
  3. Press Enter on the target dropdown, use arrow keys to highlight EUR, and press Enter to select it.
  4. Read the final target selection; confirm amount remains 100 and source remains USD.
  5. Close the converter and discard this case's state.
- **Expected result:** Selected target displays EUR.

### TC-R5-03 - Select GBP
- **TC ID:** TC-R5-03
- **Title:** Select GBP
- **Requirement(s):** R5
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount="100"; source=USD; starting target=CHF; Choose GBP in the target dropdown.
- **Steps:**
  1. Enter amount 100, set source to USD, and set the starting target to CHF.
  2. Focus the target dropdown.
  3. Press Enter on the target dropdown, use arrow keys to highlight GBP, and press Enter to select it.
  4. Read the final target selection; confirm amount remains 100 and source remains USD.
  5. Close the converter and discard this case's state.
- **Expected result:** Selected target displays GBP.

### TC-R5-04 - Select JPY
- **TC ID:** TC-R5-04
- **Title:** Select JPY
- **Requirement(s):** R5
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount="100"; source=USD; starting target=CHF; Choose JPY in the target dropdown.
- **Steps:**
  1. Enter amount 100, set source to USD, and set the starting target to CHF.
  2. Focus the target dropdown.
  3. Press Enter on the target dropdown, use arrow keys to highlight JPY, and press Enter to select it.
  4. Read the final target selection; confirm amount remains 100 and source remains USD.
  5. Close the converter and discard this case's state.
- **Expected result:** Selected target displays JPY.

### TC-R5-05 - Select CAD
- **TC ID:** TC-R5-05
- **Title:** Select CAD
- **Requirement(s):** R5
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount="100"; source=USD; starting target=CHF; Choose CAD in the target dropdown.
- **Steps:**
  1. Enter amount 100, set source to USD, and set the starting target to CHF.
  2. Focus the target dropdown.
  3. Press Enter on the target dropdown, use arrow keys to highlight CAD, and press Enter to select it.
  4. Read the final target selection; confirm amount remains 100 and source remains USD.
  5. Close the converter and discard this case's state.
- **Expected result:** Selected target displays CAD.

### TC-R5-06 - Select AUD
- **TC ID:** TC-R5-06
- **Title:** Select AUD
- **Requirement(s):** R5
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount="100"; source=USD; starting target=CHF; Choose AUD in the target dropdown.
- **Steps:**
  1. Enter amount 100, set source to USD, and set the starting target to CHF.
  2. Focus the target dropdown.
  3. Press Enter on the target dropdown, use arrow keys to highlight AUD, and press Enter to select it.
  4. Read the final target selection; confirm amount remains 100 and source remains USD.
  5. Close the converter and discard this case's state.
- **Expected result:** Selected target displays AUD.

### TC-R5-07 - Select CHF
- **TC ID:** TC-R5-07
- **Title:** Select CHF
- **Requirement(s):** R5
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount="100"; source=USD; starting target=USD; Choose CHF in the target dropdown.
- **Steps:**
  1. Enter amount 100, set source to USD, and set the starting target to USD.
  2. Focus the target dropdown.
  3. Press Enter on the target dropdown, use arrow keys to highlight CHF, and press Enter to select it.
  4. Read the final target selection; confirm amount remains 100 and source remains USD.
  5. Close the converter and discard this case's state.
- **Expected result:** Selected target displays CHF.

### TC-R5-08 - Repeated selection
- **TC ID:** TC-R5-08
- **Title:** Repeated selection
- **Requirement(s):** R5
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount="100"; source=USD; starting target=CHF; Choose EUR, then GBP, then JPY.
- **Steps:**
  1. Enter amount 100, set source to USD, and set the starting target to CHF.
  2. Focus the target dropdown.
  3. Open the target dropdown with Enter and select EUR using arrow keys and Enter; repeat for GBP, then JPY. Check the displayed selection after each choice.
  4. Read the final target selection; confirm amount remains 100 and source remains USD.
  5. Close the converter and discard this case's state.
- **Expected result:** Each selection is displayed; final target is JPY.

### TC-R5-09 - Preserve selection on blur
- **TC ID:** TC-R5-09
- **Title:** Preserve selection on blur
- **Requirement(s):** R5
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount="100"; source=USD; starting target=CHF; Choose GBP, then press Tab.
- **Steps:**
  1. Enter amount 100, set source to USD, and set the starting target to CHF.
  2. Focus the target dropdown.
  3. Open the target dropdown with Enter, select GBP using arrow keys and Enter, then press Tab to leave it.
  4. Read the final target selection; confirm amount remains 100 and source remains USD.
  5. Close the converter and discard this case's state.
- **Expected result:** Selected target remains GBP.

## R6 - Wait for the result container to become visible

### TC-R6-01 - Valid amount
- **TC ID:** TC-R6-01
- **Title:** Valid amount
- **Requirement(s):** R6
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running. ConverterDriver.waitForResult is available with its five-second timeout.
- **Test data:** source=USD; target=EUR; USD to EUR; clear amount, enter 100, then wait.
- **Steps:**
  1. Select USD to EUR; clear the amount and confirm the result is hidden; enter 100.
  2. Invoke ConverterDriver.waitForResult and record its returned boolean and elapsed time.
  3. Observe result visibility at completion and compare with the expected result.
  4. Close the converter and discard this case's state.
- **Expected result:** Wait returns true and container is visible.

### TC-R6-02 - Same-currency conversion
- **TC ID:** TC-R6-02
- **Title:** Same-currency conversion
- **Requirement(s):** R6
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running. ConverterDriver.waitForResult is available with its five-second timeout.
- **Test data:** source=USD; target=USD; amount=100; starting amount empty.
- **Steps:**
  1. Select USD to USD; clear the amount and confirm the result is hidden; enter 100.
  2. Invoke ConverterDriver.waitForResult and record its returned boolean and elapsed time.
  3. Observe result visibility at completion and compare with the expected result.
  4. Close the converter and discard this case's state.
- **Expected result:** Wait returns true and container is visible.

### TC-R6-03 - Correct invalid input
- **TC ID:** TC-R6-03
- **Title:** Correct invalid input
- **Requirement(s):** R6
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running. ConverterDriver.waitForResult is available with its five-second timeout.
- **Test data:** source=USD; target=EUR; USD to EUR; enter 0 and confirm hidden; replace with 100 and wait.
- **Steps:**
  1. Select USD to EUR; enter 0 and confirm the result is hidden; replace 0 with 100.
  2. Invoke ConverterDriver.waitForResult and record its returned boolean and elapsed time.
  3. Observe result visibility at completion and compare with the expected result.
  4. Close the converter and discard this case's state.
- **Expected result:** Container becomes visible and wait returns true.

### TC-R6-04 - Already visible
- **TC ID:** TC-R6-04
- **Title:** Already visible
- **Requirement(s):** R6
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running. ConverterDriver.waitForResult is available with its five-second timeout.
- **Test data:** source=USD; target=EUR; Establish visible result for 100 USD to EUR; invoke wait again.
- **Steps:**
  1. Enter 100 with USD to EUR; confirm the result is already visible.
  2. Invoke ConverterDriver.waitForResult and record its returned boolean and elapsed time.
  3. Observe result visibility at completion and compare with the expected result.
  4. Close the converter and discard this case's state.
- **Expected result:** Wait returns true without requiring another visibility transition.

### TC-R6-05 - Delayed visibility
- **TC ID:** TC-R6-05
- **Title:** Delayed visibility
- **Requirement(s):** R6
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running. ConverterDriver.waitForResult is available with its five-second timeout. A fixture can hide the result initially and expose it after one second without blocking the wait.
- **Test data:** amount=100; source=USD; target=EUR; visibility false -> true after 1 second; timeout=5 seconds.
- **Steps:**
  1. Configure the fixture to keep the container hidden initially and expose it one second after waiting begins.
  2. Invoke ConverterDriver.waitForResult and record its returned boolean and elapsed time.
  3. Observe result visibility at completion and compare with the expected result.
  4. Close the converter and discard this case's state.
- **Expected result:** Wait does not succeed while hidden; returns true after visibility.

### TC-R6-06 - No result
- **TC ID:** TC-R6-06
- **Title:** No result
- **Requirement(s):** R6
- **Type:** Negative
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running. ConverterDriver.waitForResult is available with its five-second timeout.
- **Test data:** source=USD; target=EUR; Leave amount empty; invoke wait.
- **Steps:**
  1. Select USD to EUR; clear the amount and confirm the result remains hidden.
  2. Invoke ConverterDriver.waitForResult and record its returned boolean and elapsed time.
  3. Observe result visibility at completion and compare with the expected result.
  4. Confirm false is returned around the configured five-second deadline, allowing normal scheduling overhead, and that the wait terminates.
  5. Close the converter and discard this case's state.
- **Expected result:** Wait returns false after its timeout; it does not hang or report success.

## R7 - Extract converted amount and exchange rate

### TC-R7-01 - Typical conversion
- **TC ID:** TC-R7-01
- **Title:** Typical conversion
- **Requirement(s):** R7
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** 100 USD to EUR.
- **Steps:**
  1. Establish the conversion and any subsequent change listed in Test data.
  2. Wait for visibility; after a change, also wait until the displayed text reflects that change.
  3. Record the amount and rate strings directly from their respective UI labels.
  4. Invoke the driver/window extraction path and parse both strings as doubles.
  5. Compare each extracted number with its corresponding recorded label value; check the expected result.
  6. Close the converter and discard this case's state.
- **Expected result:** Both extracted values match their respective displayed values.

### TC-R7-02 - Same-currency values
- **TC ID:** TC-R7-02
- **Title:** Same-currency values
- **Requirement(s):** R7
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** 100 USD to USD.
- **Steps:**
  1. Establish the conversion and any subsequent change listed in Test data.
  2. Wait for visibility; after a change, also wait until the displayed text reflects that change.
  3. Record the amount and rate strings directly from their respective UI labels.
  4. Invoke the driver/window extraction path and parse both strings as doubles.
  5. Compare each extracted number with its corresponding recorded label value; check the expected result.
  6. Close the converter and discard this case's state.
- **Expected result:** Extracted amount=100.0; rate=1.0.

### TC-R7-03 - Small amount
- **TC ID:** TC-R7-03
- **Title:** Small amount
- **Requirement(s):** R7
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** 0.01 USD to USD.
- **Steps:**
  1. Establish the conversion and any subsequent change listed in Test data.
  2. Wait for visibility; after a change, also wait until the displayed text reflects that change.
  3. Record the amount and rate strings directly from their respective UI labels.
  4. Invoke the driver/window extraction path and parse both strings as doubles.
  5. Compare each extracted number with its corresponding recorded label value; check the expected result.
  6. Close the converter and discard this case's state.
- **Expected result:** Extracted amount=0.01; rate=1.0.

### TC-R7-04 - Large amount
- **TC ID:** TC-R7-04
- **Title:** Large amount
- **Requirement(s):** R7
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** 1000000 USD to USD.
- **Steps:**
  1. Establish the conversion and any subsequent change listed in Test data.
  2. Wait for visibility; after a change, also wait until the displayed text reflects that change.
  3. Record the amount and rate strings directly from their respective UI labels.
  4. Invoke the driver/window extraction path and parse both strings as doubles.
  5. Compare each extracted number with its corresponding recorded label value; check the expected result.
  6. Close the converter and discard this case's state.
- **Expected result:** Extracted amount=1000000.0; rate=1.0; no truncation.

### TC-R7-05 - Rate precision
- **TC ID:** TC-R7-05
- **Title:** Rate precision
- **Requirement(s):** R7
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** 100 JPY to GBP.
- **Steps:**
  1. Establish the conversion and any subsequent change listed in Test data.
  2. Wait for visibility; after a change, also wait until the displayed text reflects that change.
  3. Record the amount and rate strings directly from their respective UI labels.
  4. Invoke the driver/window extraction path and parse both strings as doubles.
  5. Compare each extracted number with its corresponding recorded label value; check the expected result.
  6. Close the converter and discard this case's state.
- **Expected result:** All displayed rate digits are retained numerically; amount matches display.

### TC-R7-06 - After amount change
- **TC ID:** TC-R7-06
- **Title:** After amount change
- **Requirement(s):** R7
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** 100 USD to USD; change to 200 and extract again.
- **Steps:**
  1. Establish the conversion and any subsequent change listed in Test data.
  2. Wait for visibility; after a change, also wait until the displayed text reflects that change.
  3. Record the amount and rate strings directly from their respective UI labels.
  4. Invoke the driver/window extraction path and parse both strings as doubles.
  5. Compare each extracted number with its corresponding recorded label value; check the expected result.
  6. Close the converter and discard this case's state.
- **Expected result:** Amount=200.0; rate=1.0; no stale amount.

### TC-R7-07 - After currency change
- **TC ID:** TC-R7-07
- **Title:** After currency change
- **Requirement(s):** R7
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** 100 USD to USD; change target to EUR and extract again.
- **Steps:**
  1. Establish the conversion and any subsequent change listed in Test data.
  2. Wait for visibility; after a change, also wait until the displayed text reflects that change.
  3. Record the amount and rate strings directly from their respective UI labels.
  4. Invoke the driver/window extraction path and parse both strings as doubles.
  5. Compare each extracted number with its corresponding recorded label value; check the expected result.
  6. Close the converter and discard this case's state.
- **Expected result:** Both values match the new display; no stale values.

## R8 - Format input amount to two decimal places

### TC-R8-01 - Whole number
- **TC ID:** TC-R8-01
- **Title:** Whole number
- **Requirement(s):** R8
- **Type:** Positive
- **Priority:** High
- **Preconditions:** The assessment input-formatting path is observable; Locale.ROOT or an equivalent dot-decimal locale is active.
- **Test data:** amount=100.0; format="%.2f"; locale=ROOT; source=USD; target=EUR if the full assessment is used.
- **Steps:**
  1. Supply the numeric double 100.0 to the input-formatting path.
  2. Execute String.format("%.2f", amount) under the fixed locale and capture the resulting string.
  3. Compare the entire string with the expected result, including decimal point and trailing zeros.
  4. Count the fractional digits independently and confirm there are exactly two.
  5. Discard formatting inputs and outputs; close any assessment GUI used.
- **Expected result:** "100.00"

### TC-R8-02 - One decimal place
- **TC ID:** TC-R8-02
- **Title:** One decimal place
- **Requirement(s):** R8
- **Type:** Positive
- **Priority:** High
- **Preconditions:** The assessment input-formatting path is observable; Locale.ROOT or an equivalent dot-decimal locale is active.
- **Test data:** amount=12.5; format="%.2f"; locale=ROOT; source=USD; target=EUR if the full assessment is used.
- **Steps:**
  1. Supply the numeric double 12.5 to the input-formatting path.
  2. Execute String.format("%.2f", amount) under the fixed locale and capture the resulting string.
  3. Compare the entire string with the expected result, including decimal point and trailing zeros.
  4. Count the fractional digits independently and confirm there are exactly two.
  5. Discard formatting inputs and outputs; close any assessment GUI used.
- **Expected result:** "12.50"

### TC-R8-03 - Two decimal places
- **TC ID:** TC-R8-03
- **Title:** Two decimal places
- **Requirement(s):** R8
- **Type:** Positive
- **Priority:** High
- **Preconditions:** The assessment input-formatting path is observable; Locale.ROOT or an equivalent dot-decimal locale is active.
- **Test data:** amount=12.34; format="%.2f"; locale=ROOT; source=USD; target=EUR if the full assessment is used.
- **Steps:**
  1. Supply the numeric double 12.34 to the input-formatting path.
  2. Execute String.format("%.2f", amount) under the fixed locale and capture the resulting string.
  3. Compare the entire string with the expected result, including decimal point and trailing zeros.
  4. Count the fractional digits independently and confirm there are exactly two.
  5. Discard formatting inputs and outputs; close any assessment GUI used.
- **Expected result:** "12.34"

### TC-R8-04 - Round down
- **TC ID:** TC-R8-04
- **Title:** Round down
- **Requirement(s):** R8
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** The assessment input-formatting path is observable; Locale.ROOT or an equivalent dot-decimal locale is active.
- **Test data:** amount=12.344; format="%.2f"; locale=ROOT; source=USD; target=EUR if the full assessment is used.
- **Steps:**
  1. Supply the numeric double 12.344 to the input-formatting path.
  2. Execute String.format("%.2f", amount) under the fixed locale and capture the resulting string.
  3. Compare the entire string with the expected result, including decimal point and trailing zeros.
  4. Count the fractional digits independently and confirm there are exactly two.
  5. Discard formatting inputs and outputs; close any assessment GUI used.
- **Expected result:** "12.34"

### TC-R8-05 - Round up
- **TC ID:** TC-R8-05
- **Title:** Round up
- **Requirement(s):** R8
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** The assessment input-formatting path is observable; Locale.ROOT or an equivalent dot-decimal locale is active.
- **Test data:** amount=12.346; format="%.2f"; locale=ROOT; source=USD; target=EUR if the full assessment is used.
- **Steps:**
  1. Supply the numeric double 12.346 to the input-formatting path.
  2. Execute String.format("%.2f", amount) under the fixed locale and capture the resulting string.
  3. Compare the entire string with the expected result, including decimal point and trailing zeros.
  4. Count the fractional digits independently and confirm there are exactly two.
  5. Discard formatting inputs and outputs; close any assessment GUI used.
- **Expected result:** "12.35"

### TC-R8-06 - Exact halfway value
- **TC ID:** TC-R8-06
- **Title:** Exact halfway value
- **Requirement(s):** R8
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** The assessment input-formatting path is observable; Locale.ROOT or an equivalent dot-decimal locale is active.
- **Test data:** amount=1.125; format="%.2f"; locale=ROOT; source=USD; target=EUR if the full assessment is used.
- **Steps:**
  1. Supply the numeric double 1.125 to the input-formatting path.
  2. Execute String.format("%.2f", amount) under the fixed locale and capture the resulting string.
  3. Compare the entire string with the expected result, including decimal point and trailing zeros.
  4. Count the fractional digits independently and confirm there are exactly two.
  5. Discard formatting inputs and outputs; close any assessment GUI used.
- **Expected result:** "1.13"

### TC-R8-07 - Carry into whole part
- **TC ID:** TC-R8-07
- **Title:** Carry into whole part
- **Requirement(s):** R8
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** The assessment input-formatting path is observable; Locale.ROOT or an equivalent dot-decimal locale is active.
- **Test data:** amount=9.999; format="%.2f"; locale=ROOT; source=USD; target=EUR if the full assessment is used.
- **Steps:**
  1. Supply the numeric double 9.999 to the input-formatting path.
  2. Execute String.format("%.2f", amount) under the fixed locale and capture the resulting string.
  3. Compare the entire string with the expected result, including decimal point and trailing zeros.
  4. Count the fractional digits independently and confirm there are exactly two.
  5. Discard formatting inputs and outputs; close any assessment GUI used.
- **Expected result:** "10.00"

### TC-R8-08 - Below one cent
- **TC ID:** TC-R8-08
- **Title:** Below one cent
- **Requirement(s):** R8
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** The assessment input-formatting path is observable; Locale.ROOT or an equivalent dot-decimal locale is active.
- **Test data:** amount=0.001; format="%.2f"; locale=ROOT; source=USD; target=EUR if the full assessment is used.
- **Steps:**
  1. Supply the numeric double 0.001 to the input-formatting path.
  2. Execute String.format("%.2f", amount) under the fixed locale and capture the resulting string.
  3. Compare the entire string with the expected result, including decimal point and trailing zeros.
  4. Count the fractional digits independently and confirm there are exactly two.
  5. Discard formatting inputs and outputs; close any assessment GUI used.
- **Expected result:** "0.00"

## R9 - Count decimal places in input and result strings

### TC-R9-01 - Whole-number input
- **TC ID:** TC-R9-01
- **Title:** Whole-number input
- **Requirement(s):** R9
- **Type:** Positive
- **Priority:** High
- **Preconditions:** ConversionAssessor.countDecimalPlaces is callable; dot-decimal locale is active; controlled numeric strings are available.
- **Test data:** Input 100; result "92.35".
- **Steps:**
  1. Set the numeric input and controlled result string exactly as listed.
  2. Format the input with String.format("%.2f", amount) under the fixed locale.
  3. Call countDecimalPlaces separately on the formatted input string and the unchanged result string.
  4. Compare both returned integer counts with the expected counts, including trailing zeros.
  5. Discard the helper inputs and outputs.
- **Expected result:** Input count=2; result count=2.

### TC-R9-02 - One-decimal input
- **TC ID:** TC-R9-02
- **Title:** One-decimal input
- **Requirement(s):** R9
- **Type:** Positive
- **Priority:** High
- **Preconditions:** ConversionAssessor.countDecimalPlaces is callable; dot-decimal locale is active; controlled numeric strings are available.
- **Test data:** Input 12.5; result "11.50".
- **Steps:**
  1. Set the numeric input and controlled result string exactly as listed.
  2. Format the input with String.format("%.2f", amount) under the fixed locale.
  3. Call countDecimalPlaces separately on the formatted input string and the unchanged result string.
  4. Compare both returned integer counts with the expected counts, including trailing zeros.
  5. Discard the helper inputs and outputs.
- **Expected result:** Input count=2; result count=2.

### TC-R9-03 - Rounded input
- **TC ID:** TC-R9-03
- **Title:** Rounded input
- **Requirement(s):** R9
- **Type:** Positive
- **Priority:** High
- **Preconditions:** ConversionAssessor.countDecimalPlaces is callable; dot-decimal locale is active; controlled numeric strings are available.
- **Test data:** Input 1.234; result "1.1400".
- **Steps:**
  1. Set the numeric input and controlled result string exactly as listed.
  2. Format the input with String.format("%.2f", amount) under the fixed locale.
  3. Call countDecimalPlaces separately on the formatted input string and the unchanged result string.
  4. Compare both returned integer counts with the expected counts, including trailing zeros.
  5. Discard the helper inputs and outputs.
- **Expected result:** Formatted input "1.23": count=2; result count=4.

### TC-R9-04 - One result decimal
- **TC ID:** TC-R9-04
- **Title:** One result decimal
- **Requirement(s):** R9
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** ConversionAssessor.countDecimalPlaces is callable; dot-decimal locale is active; controlled numeric strings are available.
- **Test data:** Input 100; result "92.3".
- **Steps:**
  1. Set the numeric input and controlled result string exactly as listed.
  2. Format the input with String.format("%.2f", amount) under the fixed locale.
  3. Call countDecimalPlaces separately on the formatted input string and the unchanged result string.
  4. Compare both returned integer counts with the expected counts, including trailing zeros.
  5. Discard the helper inputs and outputs.
- **Expected result:** Input count=2; result count=1.

### TC-R9-05 - Integer result text
- **TC ID:** TC-R9-05
- **Title:** Integer result text
- **Requirement(s):** R9
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** ConversionAssessor.countDecimalPlaces is callable; dot-decimal locale is active; controlled numeric strings are available.
- **Test data:** Input 100; result "92".
- **Steps:**
  1. Set the numeric input and controlled result string exactly as listed.
  2. Format the input with String.format("%.2f", amount) under the fixed locale.
  3. Call countDecimalPlaces separately on the formatted input string and the unchanged result string.
  4. Compare both returned integer counts with the expected counts, including trailing zeros.
  5. Discard the helper inputs and outputs.
- **Expected result:** Input count=2; result count=0.

### TC-R9-06 - Leading fractional zeros
- **TC ID:** TC-R9-06
- **Title:** Leading fractional zeros
- **Requirement(s):** R9
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** ConversionAssessor.countDecimalPlaces is callable; dot-decimal locale is active; controlled numeric strings are available.
- **Test data:** Input 0.001; result "0.0001".
- **Steps:**
  1. Set the numeric input and controlled result string exactly as listed.
  2. Format the input with String.format("%.2f", amount) under the fixed locale.
  3. Call countDecimalPlaces separately on the formatted input string and the unchanged result string.
  4. Compare both returned integer counts with the expected counts, including trailing zeros.
  5. Discard the helper inputs and outputs.
- **Expected result:** Formatted input "0.00": count=2; result count=4.

## R10 - Validate conversion accuracy

### TC-R10-01 - Exact result
- **TC ID:** TC-R10-01
- **Title:** Exact result
- **Requirement(s):** R10
- **Type:** Positive
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=1; source=USD; target=USD; displayed rate="1"; baseline result="1.000"; visible=true; changed result="2.000"; restored result="1.000".
- **Steps:**
  1. Configure the fixture with the listed baseline values; return the changed and restored strings during the assessor's double-and-restore probe.
  2. Call the real assessment path with amount=1, source=USD and target=USD.
  3. Independently calculate Math.abs(parsed baseline result - amount * parsed displayed rate); compare with 0.01.
  4. Inspect conversionAccurate and compare it with the expected outcome; confirm precision and update checks pass.
  5. Close the converter and discard this case's state.
- **Expected result:** Accuracy predicate is true: difference is zero.

### TC-R10-02 - Within tolerance above
- **TC ID:** TC-R10-02
- **Title:** Within tolerance above
- **Requirement(s):** R10
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=1; source=USD; target=USD; displayed rate="1"; baseline result="1.009"; visible=true; changed result="2.000"; restored result="1.009".
- **Steps:**
  1. Configure the fixture with the listed baseline values; return the changed and restored strings during the assessor's double-and-restore probe.
  2. Call the real assessment path with amount=1, source=USD and target=USD.
  3. Independently calculate Math.abs(parsed baseline result - amount * parsed displayed rate); compare with 0.01.
  4. Inspect conversionAccurate and compare it with the expected outcome; confirm precision and update checks pass.
  5. Close the converter and discard this case's state.
- **Expected result:** Accuracy predicate is true: difference is below 0.01.

### TC-R10-03 - Within tolerance below
- **TC ID:** TC-R10-03
- **Title:** Within tolerance below
- **Requirement(s):** R10
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=1; source=USD; target=USD; displayed rate="1"; baseline result="0.991"; visible=true; changed result="2.000"; restored result="0.991".
- **Steps:**
  1. Configure the fixture with the listed baseline values; return the changed and restored strings during the assessor's double-and-restore probe.
  2. Call the real assessment path with amount=1, source=USD and target=USD.
  3. Independently calculate Math.abs(parsed baseline result - amount * parsed displayed rate); compare with 0.01.
  4. Inspect conversionAccurate and compare it with the expected outcome; confirm precision and update checks pass.
  5. Close the converter and discard this case's state.
- **Expected result:** Accuracy predicate is true: difference is below 0.01.

### TC-R10-04 - Exactly at tolerance
- **TC ID:** TC-R10-04
- **Title:** Exactly at tolerance
- **Requirement(s):** R10
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=1; source=USD; target=USD; displayed rate="0.01"; baseline result="0.00"; visible=true; changed result="2.000"; restored result="0.00".
- **Steps:**
  1. Configure the fixture with the listed baseline values; return the changed and restored strings during the assessor's double-and-restore probe.
  2. Call the real assessment path with amount=1, source=USD and target=USD.
  3. Independently calculate Math.abs(parsed baseline result - amount * parsed displayed rate); compare with 0.01.
  4. Inspect conversionAccurate and compare it with the expected outcome; confirm precision and update checks pass.
  5. Close the converter and discard this case's state.
- **Expected result:** Accuracy predicate is true: evaluated difference equals 0.01.

### TC-R10-05 - Above tolerance, high
- **TC ID:** TC-R10-05
- **Title:** Above tolerance, high
- **Requirement(s):** R10
- **Type:** Negative
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=1; source=USD; target=USD; displayed rate="1"; baseline result="1.011"; visible=true; changed result="2.000"; restored result="1.011".
- **Steps:**
  1. Configure the fixture with the listed baseline values; return the changed and restored strings during the assessor's double-and-restore probe.
  2. Call the real assessment path with amount=1, source=USD and target=USD.
  3. Independently calculate Math.abs(parsed baseline result - amount * parsed displayed rate); compare with 0.01.
  4. Inspect conversionAccurate and compare it with the expected outcome; confirm precision and update checks pass.
  5. Close the converter and discard this case's state.
- **Expected result:** Accuracy predicate is false: difference exceeds 0.01.

### TC-R10-06 - Above tolerance, low
- **TC ID:** TC-R10-06
- **Title:** Above tolerance, low
- **Requirement(s):** R10
- **Type:** Negative
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=1; source=USD; target=USD; displayed rate="1"; baseline result="0.989"; visible=true; changed result="2.000"; restored result="0.989".
- **Steps:**
  1. Configure the fixture with the listed baseline values; return the changed and restored strings during the assessor's double-and-restore probe.
  2. Call the real assessment path with amount=1, source=USD and target=USD.
  3. Independently calculate Math.abs(parsed baseline result - amount * parsed displayed rate); compare with 0.01.
  4. Inspect conversionAccurate and compare it with the expected outcome; confirm precision and update checks pass.
  5. Close the converter and discard this case's state.
- **Expected result:** Accuracy predicate is false: difference exceeds 0.01.

## R11 - Require at least two result decimal places

### TC-R11-01 - Exactly two digits
- **TC ID:** TC-R11-01
- **Title:** Exactly two digits
- **Requirement(s):** R11
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** ConversionAssessor.countDecimalPlaces is callable; controlled result strings are available.
- **Test data:** result text="92.35".
- **Steps:**
  1. Supply the result string exactly as listed; preserve all fractional zeros.
  2. Count fractional digits with countDecimalPlaces.
  3. Evaluate count >= 2 and compare with the expected precision outcome.
  4. Discard the helper inputs and outputs; no GUI state was created.
- **Expected result:** Precision passes.

### TC-R11-02 - Three digits
- **TC ID:** TC-R11-02
- **Title:** Three digits
- **Requirement(s):** R11
- **Type:** Positive
- **Priority:** High
- **Preconditions:** ConversionAssessor.countDecimalPlaces is callable; controlled result strings are available.
- **Test data:** result text="92.350".
- **Steps:**
  1. Supply the result string exactly as listed; preserve all fractional zeros.
  2. Count fractional digits with countDecimalPlaces.
  3. Evaluate count >= 2 and compare with the expected precision outcome.
  4. Discard the helper inputs and outputs; no GUI state was created.
- **Expected result:** Precision passes; trailing zero counts.

### TC-R11-03 - Four digits
- **TC ID:** TC-R11-03
- **Title:** Four digits
- **Requirement(s):** R11
- **Type:** Positive
- **Priority:** High
- **Preconditions:** ConversionAssessor.countDecimalPlaces is callable; controlled result strings are available.
- **Test data:** result text="0.0001".
- **Steps:**
  1. Supply the result string exactly as listed; preserve all fractional zeros.
  2. Count fractional digits with countDecimalPlaces.
  3. Evaluate count >= 2 and compare with the expected precision outcome.
  4. Discard the helper inputs and outputs; no GUI state was created.
- **Expected result:** Precision passes.

### TC-R11-04 - One digit
- **TC ID:** TC-R11-04
- **Title:** One digit
- **Requirement(s):** R11
- **Type:** Negative
- **Priority:** High
- **Preconditions:** ConversionAssessor.countDecimalPlaces is callable; controlled result strings are available.
- **Test data:** result text="92.3".
- **Steps:**
  1. Supply the result string exactly as listed; preserve all fractional zeros.
  2. Count fractional digits with countDecimalPlaces.
  3. Evaluate count >= 2 and compare with the expected precision outcome.
  4. Discard the helper inputs and outputs; no GUI state was created.
- **Expected result:** Precision fails.

### TC-R11-05 - No decimal point
- **TC ID:** TC-R11-05
- **Title:** No decimal point
- **Requirement(s):** R11
- **Type:** Negative
- **Priority:** High
- **Preconditions:** ConversionAssessor.countDecimalPlaces is callable; controlled result strings are available.
- **Test data:** result text="92".
- **Steps:**
  1. Supply the result string exactly as listed; preserve all fractional zeros.
  2. Count fractional digits with countDecimalPlaces.
  3. Evaluate count >= 2 and compare with the expected precision outcome.
  4. Discard the helper inputs and outputs; no GUI state was created.
- **Expected result:** Precision fails.

### TC-R11-06 - Zero with two digits
- **TC ID:** TC-R11-06
- **Title:** Zero with two digits
- **Requirement(s):** R11
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** ConversionAssessor.countDecimalPlaces is callable; controlled result strings are available.
- **Test data:** result text="0.00".
- **Steps:**
  1. Supply the result string exactly as listed; preserve all fractional zeros.
  2. Count fractional digits with countDecimalPlaces.
  3. Evaluate count >= 2 and compare with the expected precision outcome.
  4. Discard the helper inputs and outputs; no GUI state was created.
- **Expected result:** Precision passes; numeric magnitude does not affect digit count.

## R12 - Update the result and restore the original amount

### TC-R12-01 - Increase amount
- **TC ID:** TC-R12-01
- **Title:** Increase amount
- **Requirement(s):** R12
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** source=USD; target=USD; amount sequence=100 -> 200 -> 100.
- **Steps:**
  1. Select USD to USD, enter 100, and wait for a visible result; record exact original amount text and baseline result.
  2. Enter each intermediate amount in order: 200. Wait for the corresponding result and compare it with the previous result.
  3. Restore the exact original amount text and wait for the baseline result to return.
  4. Verify the amount field and result both equal their recorded originals, and that source and target did not change.
  5. Close the converter and discard this case's state.
- **Expected result:** Result 100.00 -> 200.00 -> 100.00; original amount restored.

### TC-R12-02 - Decrease amount
- **TC ID:** TC-R12-02
- **Title:** Decrease amount
- **Requirement(s):** R12
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** source=USD; target=USD; amount sequence=100 -> 50 -> 100.
- **Steps:**
  1. Select USD to USD, enter 100, and wait for a visible result; record exact original amount text and baseline result.
  2. Enter each intermediate amount in order: 50. Wait for the corresponding result and compare it with the previous result.
  3. Restore the exact original amount text and wait for the baseline result to return.
  4. Verify the amount field and result both equal their recorded originals, and that source and target did not change.
  5. Close the converter and discard this case's state.
- **Expected result:** Result 100.00 -> 50.00 -> 100.00; original amount restored.

### TC-R12-03 - Fractional amount
- **TC ID:** TC-R12-03
- **Title:** Fractional amount
- **Requirement(s):** R12
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** source=USD; target=USD; amount sequence=12.50 -> 25.00 -> 12.50.
- **Steps:**
  1. Select USD to USD, enter 12.50, and wait for a visible result; record exact original amount text and baseline result.
  2. Enter each intermediate amount in order: 25.00. Wait for the corresponding result and compare it with the previous result.
  3. Restore the exact original amount text and wait for the baseline result to return.
  4. Verify the amount field and result both equal their recorded originals, and that source and target did not change.
  5. Close the converter and discard this case's state.
- **Expected result:** Results follow each amount; final result 12.50 and original amount restored.

### TC-R12-04 - Different currencies
- **TC ID:** TC-R12-04
- **Title:** Different currencies
- **Requirement(s):** R12
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** source=USD; target=EUR; amount sequence=100 -> 200 -> 100.
- **Steps:**
  1. Select USD to EUR, enter 100, and wait for a visible result; record exact original amount text and baseline result.
  2. Enter each intermediate amount in order: 200. Wait for the corresponding result and compare it with the previous result.
  3. Restore the exact original amount text and wait for the baseline result to return.
  4. Verify the amount field and result both equal their recorded originals, and that source and target did not change.
  5. Close the converter and discard this case's state.
- **Expected result:** Middle displayed result differs; final result equals baseline.

### TC-R12-05 - Repeated changes
- **TC ID:** TC-R12-05
- **Title:** Repeated changes
- **Requirement(s):** R12
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** source=USD; target=USD; amount sequence=100 -> 200 -> 300 -> 100.
- **Steps:**
  1. Select USD to USD, enter 100, and wait for a visible result; record exact original amount text and baseline result.
  2. Enter each intermediate amount in order: 200, 300. Wait for the corresponding result and compare it with the previous result.
  3. Restore the exact original amount text and wait for the baseline result to return.
  4. Verify the amount field and result both equal their recorded originals, and that source and target did not change.
  5. Close the converter and discard this case's state.
- **Expected result:** Results 100.00, 200.00, 300.00, 100.00; no stale intermediate value.

### TC-R12-06 - Failure to restore
- **TC ID:** TC-R12-06
- **Title:** Failure to restore
- **Requirement(s):** R12
- **Type:** Negative
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=100; source=USD; target=USD; baseline="100.00"; changed="200.00"; attempted restored result="150.00".
- **Steps:**
  1. Configure the fixture to show the listed baseline, changed and failed-restoration values in order.
  2. Run verifyDynamicUpdate(100, "100.00").
  3. Check it attempted to enter 200 and then 100.
  4. Verify the check returns false because restored result text differs from baseline.
  5. Close the converter and discard this case's state.
- **Expected result:** Dynamic-update check fails; successful change alone does not satisfy R12.

## R13 - Return the original input amount

### TC-R13-01 - Whole amount
- **TC ID:** TC-R13-01
- **Title:** Whole amount
- **Requirement(s):** R13
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=100.0; source=USD; target=USD.
- **Steps:**
  1. Run assess with the listed amount and USD to USD; if two amounts are listed, run a separate assessment for each in that order.
  2. Read inputAmount from the returned record, using the second record for the sequential case.
  3. Compare the field with the exact original double argument; do not compare with the two-decimal formatted string.
  4. Close the converter and discard this case's state.
- **Expected result:** inputAmount=100.0.

### TC-R13-02 - Fractional amount
- **TC ID:** TC-R13-02
- **Title:** Fractional amount
- **Requirement(s):** R13
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=12.3; source=USD; target=USD.
- **Steps:**
  1. Run assess with the listed amount and USD to USD; if two amounts are listed, run a separate assessment for each in that order.
  2. Read inputAmount from the returned record, using the second record for the sequential case.
  3. Compare the field with the exact original double argument; do not compare with the two-decimal formatted string.
  4. Close the converter and discard this case's state.
- **Expected result:** inputAmount=12.3.

### TC-R13-03 - Small amount
- **TC ID:** TC-R13-03
- **Title:** Small amount
- **Requirement(s):** R13
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=0.01; source=USD; target=USD.
- **Steps:**
  1. Run assess with the listed amount and USD to USD; if two amounts are listed, run a separate assessment for each in that order.
  2. Read inputAmount from the returned record, using the second record for the sequential case.
  3. Compare the field with the exact original double argument; do not compare with the two-decimal formatted string.
  4. Close the converter and discard this case's state.
- **Expected result:** inputAmount=0.01.

### TC-R13-04 - Extra precision
- **TC ID:** TC-R13-04
- **Title:** Extra precision
- **Requirement(s):** R13
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=1.234; source=USD; target=USD.
- **Steps:**
  1. Run assess with the listed amount and USD to USD; if two amounts are listed, run a separate assessment for each in that order.
  2. Read inputAmount from the returned record, using the second record for the sequential case.
  3. Compare the field with the exact original double argument; do not compare with the two-decimal formatted string.
  4. Close the converter and discard this case's state.
- **Expected result:** inputAmount=1.234, not 1.23.

### TC-R13-05 - Large amount
- **TC ID:** TC-R13-05
- **Title:** Large amount
- **Requirement(s):** R13
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=1000000.0; source=USD; target=USD.
- **Steps:**
  1. Run assess with the listed amount and USD to USD; if two amounts are listed, run a separate assessment for each in that order.
  2. Read inputAmount from the returned record, using the second record for the sequential case.
  3. Compare the field with the exact original double argument; do not compare with the two-decimal formatted string.
  4. Close the converter and discard this case's state.
- **Expected result:** inputAmount=1000000.0.

### TC-R13-06 - After another assessment
- **TC ID:** TC-R13-06
- **Title:** After another assessment
- **Requirement(s):** R13
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** first amount=100.0; second amount=250.75; source=USD; target=USD.
- **Steps:**
  1. Run assess with the listed amount and USD to USD; if two amounts are listed, run a separate assessment for each in that order.
  2. Read inputAmount from the returned record, using the second record for the sequential case.
  3. Compare the field with the exact original double argument; do not compare with the two-decimal formatted string.
  4. Close the converter and discard this case's state.
- **Expected result:** Second record inputAmount=250.75, with no stale first amount.

## R14 - Return the selected source currency

### TC-R14-01 - Return USD
- **TC ID:** TC-R14-01
- **Title:** Return USD
- **Requirement(s):** R14
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=100; source=USD; other currency=USD.
- **Steps:**
  1. Run the assessment with the specified amount and currencies; for the sequential case assess GBP first, then EUR as source.
  2. Read the selected source code directly from the GUI after the assessment.
  3. Inspect sourceCurrency on the returned record, using the second record for the sequential case.
  4. Compare the field with both the independently observed dropdown selection and the expected code.
  5. Close the converter and discard this case's state.
- **Expected result:** sourceCurrency="USD".

### TC-R14-02 - Return EUR
- **TC ID:** TC-R14-02
- **Title:** Return EUR
- **Requirement(s):** R14
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=100; source=EUR; other currency=USD.
- **Steps:**
  1. Run the assessment with the specified amount and currencies; for the sequential case assess GBP first, then EUR as source.
  2. Read the selected source code directly from the GUI after the assessment.
  3. Inspect sourceCurrency on the returned record, using the second record for the sequential case.
  4. Compare the field with both the independently observed dropdown selection and the expected code.
  5. Close the converter and discard this case's state.
- **Expected result:** sourceCurrency="EUR".

### TC-R14-03 - Return GBP
- **TC ID:** TC-R14-03
- **Title:** Return GBP
- **Requirement(s):** R14
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=100; source=GBP; other currency=USD.
- **Steps:**
  1. Run the assessment with the specified amount and currencies; for the sequential case assess GBP first, then EUR as source.
  2. Read the selected source code directly from the GUI after the assessment.
  3. Inspect sourceCurrency on the returned record, using the second record for the sequential case.
  4. Compare the field with both the independently observed dropdown selection and the expected code.
  5. Close the converter and discard this case's state.
- **Expected result:** sourceCurrency="GBP".

### TC-R14-04 - Return JPY
- **TC ID:** TC-R14-04
- **Title:** Return JPY
- **Requirement(s):** R14
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=100; source=JPY; other currency=USD.
- **Steps:**
  1. Run the assessment with the specified amount and currencies; for the sequential case assess GBP first, then EUR as source.
  2. Read the selected source code directly from the GUI after the assessment.
  3. Inspect sourceCurrency on the returned record, using the second record for the sequential case.
  4. Compare the field with both the independently observed dropdown selection and the expected code.
  5. Close the converter and discard this case's state.
- **Expected result:** sourceCurrency="JPY".

### TC-R14-05 - Return CAD
- **TC ID:** TC-R14-05
- **Title:** Return CAD
- **Requirement(s):** R14
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=100; source=CAD; other currency=USD.
- **Steps:**
  1. Run the assessment with the specified amount and currencies; for the sequential case assess GBP first, then EUR as source.
  2. Read the selected source code directly from the GUI after the assessment.
  3. Inspect sourceCurrency on the returned record, using the second record for the sequential case.
  4. Compare the field with both the independently observed dropdown selection and the expected code.
  5. Close the converter and discard this case's state.
- **Expected result:** sourceCurrency="CAD".

### TC-R14-06 - Return AUD
- **TC ID:** TC-R14-06
- **Title:** Return AUD
- **Requirement(s):** R14
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=100; source=AUD; other currency=USD.
- **Steps:**
  1. Run the assessment with the specified amount and currencies; for the sequential case assess GBP first, then EUR as source.
  2. Read the selected source code directly from the GUI after the assessment.
  3. Inspect sourceCurrency on the returned record, using the second record for the sequential case.
  4. Compare the field with both the independently observed dropdown selection and the expected code.
  5. Close the converter and discard this case's state.
- **Expected result:** sourceCurrency="AUD".

### TC-R14-07 - Return CHF
- **TC ID:** TC-R14-07
- **Title:** Return CHF
- **Requirement(s):** R14
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=100; source=CHF; other currency=USD.
- **Steps:**
  1. Run the assessment with the specified amount and currencies; for the sequential case assess GBP first, then EUR as source.
  2. Read the selected source code directly from the GUI after the assessment.
  3. Inspect sourceCurrency on the returned record, using the second record for the sequential case.
  4. Compare the field with both the independently observed dropdown selection and the expected code.
  5. Close the converter and discard this case's state.
- **Expected result:** sourceCurrency="CHF".

### TC-R14-08 - Return latest selection
- **TC ID:** TC-R14-08
- **Title:** Return latest selection
- **Requirement(s):** R14
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=100; source sequence=GBP -> EUR; other currency=USD.
- **Steps:**
  1. Run the assessment with the specified amount and currencies; for the sequential case assess GBP first, then EUR as source.
  2. Read the selected source code directly from the GUI after the assessment.
  3. Inspect sourceCurrency on the returned record, using the second record for the sequential case.
  4. Compare the field with both the independently observed dropdown selection and the expected code.
  5. Close the converter and discard this case's state.
- **Expected result:** Second record sourceCurrency="EUR", not "GBP".

## R15 - Return the selected target currency

### TC-R15-01 - Return USD
- **TC ID:** TC-R15-01
- **Title:** Return USD
- **Requirement(s):** R15
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=100; target=USD; other currency=USD.
- **Steps:**
  1. Run the assessment with the specified amount and currencies; for the sequential case assess GBP first, then EUR as target.
  2. Read the selected target code directly from the GUI after the assessment.
  3. Inspect targetCurrency on the returned record, using the second record for the sequential case.
  4. Compare the field with both the independently observed dropdown selection and the expected code.
  5. Close the converter and discard this case's state.
- **Expected result:** targetCurrency="USD".

### TC-R15-02 - Return EUR
- **TC ID:** TC-R15-02
- **Title:** Return EUR
- **Requirement(s):** R15
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=100; target=EUR; other currency=USD.
- **Steps:**
  1. Run the assessment with the specified amount and currencies; for the sequential case assess GBP first, then EUR as target.
  2. Read the selected target code directly from the GUI after the assessment.
  3. Inspect targetCurrency on the returned record, using the second record for the sequential case.
  4. Compare the field with both the independently observed dropdown selection and the expected code.
  5. Close the converter and discard this case's state.
- **Expected result:** targetCurrency="EUR".

### TC-R15-03 - Return GBP
- **TC ID:** TC-R15-03
- **Title:** Return GBP
- **Requirement(s):** R15
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=100; target=GBP; other currency=USD.
- **Steps:**
  1. Run the assessment with the specified amount and currencies; for the sequential case assess GBP first, then EUR as target.
  2. Read the selected target code directly from the GUI after the assessment.
  3. Inspect targetCurrency on the returned record, using the second record for the sequential case.
  4. Compare the field with both the independently observed dropdown selection and the expected code.
  5. Close the converter and discard this case's state.
- **Expected result:** targetCurrency="GBP".

### TC-R15-04 - Return JPY
- **TC ID:** TC-R15-04
- **Title:** Return JPY
- **Requirement(s):** R15
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=100; target=JPY; other currency=USD.
- **Steps:**
  1. Run the assessment with the specified amount and currencies; for the sequential case assess GBP first, then EUR as target.
  2. Read the selected target code directly from the GUI after the assessment.
  3. Inspect targetCurrency on the returned record, using the second record for the sequential case.
  4. Compare the field with both the independently observed dropdown selection and the expected code.
  5. Close the converter and discard this case's state.
- **Expected result:** targetCurrency="JPY".

### TC-R15-05 - Return CAD
- **TC ID:** TC-R15-05
- **Title:** Return CAD
- **Requirement(s):** R15
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=100; target=CAD; other currency=USD.
- **Steps:**
  1. Run the assessment with the specified amount and currencies; for the sequential case assess GBP first, then EUR as target.
  2. Read the selected target code directly from the GUI after the assessment.
  3. Inspect targetCurrency on the returned record, using the second record for the sequential case.
  4. Compare the field with both the independently observed dropdown selection and the expected code.
  5. Close the converter and discard this case's state.
- **Expected result:** targetCurrency="CAD".

### TC-R15-06 - Return AUD
- **TC ID:** TC-R15-06
- **Title:** Return AUD
- **Requirement(s):** R15
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=100; target=AUD; other currency=USD.
- **Steps:**
  1. Run the assessment with the specified amount and currencies; for the sequential case assess GBP first, then EUR as target.
  2. Read the selected target code directly from the GUI after the assessment.
  3. Inspect targetCurrency on the returned record, using the second record for the sequential case.
  4. Compare the field with both the independently observed dropdown selection and the expected code.
  5. Close the converter and discard this case's state.
- **Expected result:** targetCurrency="AUD".

### TC-R15-07 - Return CHF
- **TC ID:** TC-R15-07
- **Title:** Return CHF
- **Requirement(s):** R15
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=100; target=CHF; other currency=USD.
- **Steps:**
  1. Run the assessment with the specified amount and currencies; for the sequential case assess GBP first, then EUR as target.
  2. Read the selected target code directly from the GUI after the assessment.
  3. Inspect targetCurrency on the returned record, using the second record for the sequential case.
  4. Compare the field with both the independently observed dropdown selection and the expected code.
  5. Close the converter and discard this case's state.
- **Expected result:** targetCurrency="CHF".

### TC-R15-08 - Return latest selection
- **TC ID:** TC-R15-08
- **Title:** Return latest selection
- **Requirement(s):** R15
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=100; target sequence=GBP -> EUR; other currency=USD.
- **Steps:**
  1. Run the assessment with the specified amount and currencies; for the sequential case assess GBP first, then EUR as target.
  2. Read the selected target code directly from the GUI after the assessment.
  3. Inspect targetCurrency on the returned record, using the second record for the sequential case.
  4. Compare the field with both the independently observed dropdown selection and the expected code.
  5. Close the converter and discard this case's state.
- **Expected result:** Second record targetCurrency="EUR", not "GBP".

## R16 - Return the converted amount extracted from the UI

### TC-R16-01 - Whole result
- **TC ID:** TC-R16-01
- **Title:** Whole result
- **Requirement(s):** R16
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=100; source=USD; target=USD.
- **Steps:**
  1. Run assess with the specified amount and USD to USD; for the sequential case assess 100 and then 200.
  2. Observe and record the initial result label before the assessment's temporary dynamic-update probe.
  3. Read conversionResult from the relevant returned record and compare with the parsed baseline UI text using a numerical delta of 1e-9.
  4. Verify the field represents the displayed rounded amount rather than an unrounded service calculation or a temporary probe result.
  5. Close the converter and discard this case's state.
- **Expected result:** conversionResult=100.0.

### TC-R16-02 - Fractional result
- **TC ID:** TC-R16-02
- **Title:** Fractional result
- **Requirement(s):** R16
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=12.34; source=USD; target=USD.
- **Steps:**
  1. Run assess with the specified amount and USD to USD; for the sequential case assess 100 and then 200.
  2. Observe and record the initial result label before the assessment's temporary dynamic-update probe.
  3. Read conversionResult from the relevant returned record and compare with the parsed baseline UI text using a numerical delta of 1e-9.
  4. Verify the field represents the displayed rounded amount rather than an unrounded service calculation or a temporary probe result.
  5. Close the converter and discard this case's state.
- **Expected result:** conversionResult=12.34.

### TC-R16-03 - Small result
- **TC ID:** TC-R16-03
- **Title:** Small result
- **Requirement(s):** R16
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=0.01; source=USD; target=USD.
- **Steps:**
  1. Run assess with the specified amount and USD to USD; for the sequential case assess 100 and then 200.
  2. Observe and record the initial result label before the assessment's temporary dynamic-update probe.
  3. Read conversionResult from the relevant returned record and compare with the parsed baseline UI text using a numerical delta of 1e-9.
  4. Verify the field represents the displayed rounded amount rather than an unrounded service calculation or a temporary probe result.
  5. Close the converter and discard this case's state.
- **Expected result:** conversionResult=0.01.

### TC-R16-04 - Large result
- **TC ID:** TC-R16-04
- **Title:** Large result
- **Requirement(s):** R16
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=1000000; source=USD; target=USD.
- **Steps:**
  1. Run assess with the specified amount and USD to USD; for the sequential case assess 100 and then 200.
  2. Observe and record the initial result label before the assessment's temporary dynamic-update probe.
  3. Read conversionResult from the relevant returned record and compare with the parsed baseline UI text using a numerical delta of 1e-9.
  4. Verify the field represents the displayed rounded amount rather than an unrounded service calculation or a temporary probe result.
  5. Close the converter and discard this case's state.
- **Expected result:** conversionResult=1000000.0.

### TC-R16-05 - Displayed rounding
- **TC ID:** TC-R16-05
- **Title:** Displayed rounding
- **Requirement(s):** R16
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=1.234; source=USD; target=USD.
- **Steps:**
  1. Run assess with the specified amount and USD to USD; for the sequential case assess 100 and then 200.
  2. Observe and record the initial result label before the assessment's temporary dynamic-update probe.
  3. Read conversionResult from the relevant returned record and compare with the parsed baseline UI text using a numerical delta of 1e-9.
  4. Verify the field represents the displayed rounded amount rather than an unrounded service calculation or a temporary probe result.
  5. Close the converter and discard this case's state.
- **Expected result:** conversionResult=1.23, rather than unrounded 1.234.

### TC-R16-06 - Latest conversion
- **TC ID:** TC-R16-06
- **Title:** Latest conversion
- **Requirement(s):** R16
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount sequence=100 -> 200; source=USD; target=USD.
- **Steps:**
  1. Run assess with the specified amount and USD to USD; for the sequential case assess 100 and then 200.
  2. Observe and record the initial result label before the assessment's temporary dynamic-update probe.
  3. Read conversionResult from the relevant returned record and compare with the parsed baseline UI text using a numerical delta of 1e-9.
  4. Verify the field represents the displayed rounded amount rather than an unrounded service calculation or a temporary probe result.
  5. Close the converter and discard this case's state.
- **Expected result:** Second record conversionResult=200.0.

## R17 - Return the formatted input decimal count

### TC-R17-01 - Whole input
- **TC ID:** TC-R17-01
- **Title:** Whole input
- **Requirement(s):** R17
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=100.0; source=USD; target=USD; input format="%.2f"; locale=ROOT.
- **Steps:**
  1. Run assess with the specified numeric input and USD to USD.
  2. Independently form the two-decimal input string and count its fractional digits.
  3. Inspect inputDecimalPlaces on the returned record and compare with the independent count and the expected result.
  4. Close the converter and discard this case's state.
- **Expected result:** inputDecimalPlaces=2.

### TC-R17-02 - One decimal
- **TC ID:** TC-R17-02
- **Title:** One decimal
- **Requirement(s):** R17
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=12.5; source=USD; target=USD; input format="%.2f"; locale=ROOT.
- **Steps:**
  1. Run assess with the specified numeric input and USD to USD.
  2. Independently form the two-decimal input string and count its fractional digits.
  3. Inspect inputDecimalPlaces on the returned record and compare with the independent count and the expected result.
  4. Close the converter and discard this case's state.
- **Expected result:** inputDecimalPlaces=2.

### TC-R17-03 - Two decimals
- **TC ID:** TC-R17-03
- **Title:** Two decimals
- **Requirement(s):** R17
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=12.34; source=USD; target=USD; input format="%.2f"; locale=ROOT.
- **Steps:**
  1. Run assess with the specified numeric input and USD to USD.
  2. Independently form the two-decimal input string and count its fractional digits.
  3. Inspect inputDecimalPlaces on the returned record and compare with the independent count and the expected result.
  4. Close the converter and discard this case's state.
- **Expected result:** inputDecimalPlaces=2.

### TC-R17-04 - Extra decimals
- **TC ID:** TC-R17-04
- **Title:** Extra decimals
- **Requirement(s):** R17
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=1.234; source=USD; target=USD; input format="%.2f"; locale=ROOT.
- **Steps:**
  1. Run assess with the specified numeric input and USD to USD.
  2. Independently form the two-decimal input string and count its fractional digits.
  3. Inspect inputDecimalPlaces on the returned record and compare with the independent count and the expected result.
  4. Close the converter and discard this case's state.
- **Expected result:** inputDecimalPlaces=2, not 3.

### TC-R17-05 - Rounded to zero
- **TC ID:** TC-R17-05
- **Title:** Rounded to zero
- **Requirement(s):** R17
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=0.001; source=USD; target=USD; input format="%.2f"; locale=ROOT.
- **Steps:**
  1. Run assess with the specified numeric input and USD to USD.
  2. Independently form the two-decimal input string and count its fractional digits.
  3. Inspect inputDecimalPlaces on the returned record and compare with the independent count and the expected result.
  4. Close the converter and discard this case's state.
- **Expected result:** inputDecimalPlaces=2 even if completion is false.

### TC-R17-06 - Large input
- **TC ID:** TC-R17-06
- **Title:** Large input
- **Requirement(s):** R17
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=1000000.0; source=USD; target=USD; input format="%.2f"; locale=ROOT.
- **Steps:**
  1. Run assess with the specified numeric input and USD to USD.
  2. Independently form the two-decimal input string and count its fractional digits.
  3. Inspect inputDecimalPlaces on the returned record and compare with the independent count and the expected result.
  4. Close the converter and discard this case's state.
- **Expected result:** inputDecimalPlaces=2.

## R18 - Return the displayed result decimal count

### TC-R18-01 - Normal result
- **TC ID:** TC-R18-01
- **Title:** Normal result
- **Requirement(s):** R18
- **Type:** Positive
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=1; source=USD; target=USD; baseline result="92.35"; displayed rate="92.35"; visible=true; changed result="184.70"; restored result="92.35".
- **Steps:**
  1. Configure the fixture to return the exact baseline string, including all trailing zeros, and the listed rate and update sequence.
  2. Run the real assess(1, "USD", "USD") path and retain the returned record.
  3. Count fractional digits in the baseline string independently and compare with resultDecimalPlaces.
  4. Verify a precision failure does not cause the reported count to be replaced with 2.
  5. Close the converter and discard this case's state.
- **Expected result:** resultDecimalPlaces=2.

### TC-R18-02 - Trailing zero
- **TC ID:** TC-R18-02
- **Title:** Trailing zero
- **Requirement(s):** R18
- **Type:** Positive
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=1; source=USD; target=USD; baseline result="92.350"; displayed rate="92.350"; visible=true; changed result="184.70"; restored result="92.350".
- **Steps:**
  1. Configure the fixture to return the exact baseline string, including all trailing zeros, and the listed rate and update sequence.
  2. Run the real assess(1, "USD", "USD") path and retain the returned record.
  3. Count fractional digits in the baseline string independently and compare with resultDecimalPlaces.
  4. Verify a precision failure does not cause the reported count to be replaced with 2.
  5. Close the converter and discard this case's state.
- **Expected result:** resultDecimalPlaces=3.

### TC-R18-03 - Leading fractional zeros
- **TC ID:** TC-R18-03
- **Title:** Leading fractional zeros
- **Requirement(s):** R18
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=1; source=USD; target=USD; baseline result="0.0001"; displayed rate="0.0001"; visible=true; changed result="184.70"; restored result="0.0001".
- **Steps:**
  1. Configure the fixture to return the exact baseline string, including all trailing zeros, and the listed rate and update sequence.
  2. Run the real assess(1, "USD", "USD") path and retain the returned record.
  3. Count fractional digits in the baseline string independently and compare with resultDecimalPlaces.
  4. Verify a precision failure does not cause the reported count to be replaced with 2.
  5. Close the converter and discard this case's state.
- **Expected result:** resultDecimalPlaces=4.

### TC-R18-04 - One decimal
- **TC ID:** TC-R18-04
- **Title:** One decimal
- **Requirement(s):** R18
- **Type:** Negative
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=1; source=USD; target=USD; baseline result="92.3"; displayed rate="92.3"; visible=true; changed result="184.70"; restored result="92.3".
- **Steps:**
  1. Configure the fixture to return the exact baseline string, including all trailing zeros, and the listed rate and update sequence.
  2. Run the real assess(1, "USD", "USD") path and retain the returned record.
  3. Count fractional digits in the baseline string independently and compare with resultDecimalPlaces.
  4. Verify a precision failure does not cause the reported count to be replaced with 2.
  5. Close the converter and discard this case's state.
- **Expected result:** resultDecimalPlaces=1; do not force the count to 2.

### TC-R18-05 - Integer text
- **TC ID:** TC-R18-05
- **Title:** Integer text
- **Requirement(s):** R18
- **Type:** Negative
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=1; source=USD; target=USD; baseline result="92"; displayed rate="92"; visible=true; changed result="184.70"; restored result="92".
- **Steps:**
  1. Configure the fixture to return the exact baseline string, including all trailing zeros, and the listed rate and update sequence.
  2. Run the real assess(1, "USD", "USD") path and retain the returned record.
  3. Count fractional digits in the baseline string independently and compare with resultDecimalPlaces.
  4. Verify a precision failure does not cause the reported count to be replaced with 2.
  5. Close the converter and discard this case's state.
- **Expected result:** resultDecimalPlaces=0.

### TC-R18-06 - Zero display
- **TC ID:** TC-R18-06
- **Title:** Zero display
- **Requirement(s):** R18
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=1; source=USD; target=USD; baseline result="0.00"; displayed rate="0.00"; visible=true; changed result="184.70"; restored result="0.00".
- **Steps:**
  1. Configure the fixture to return the exact baseline string, including all trailing zeros, and the listed rate and update sequence.
  2. Run the real assess(1, "USD", "USD") path and retain the returned record.
  3. Count fractional digits in the baseline string independently and compare with resultDecimalPlaces.
  4. Verify a precision failure does not cause the reported count to be replaced with 2.
  5. Close the converter and discard this case's state.
- **Expected result:** resultDecimalPlaces=2.

## R19 - Return a truthful accuracy flag

### TC-R19-01 - Exact result
- **TC ID:** TC-R19-01
- **Title:** Exact result
- **Requirement(s):** R19, R10
- **Type:** Positive
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=1; source=USD; target=USD; displayed rate="1"; baseline result="1.000"; visible=true; changed result="2.000"; restored result="1.000".
- **Steps:**
  1. Configure the fixture with the listed baseline values; return the changed and restored strings during the assessor's double-and-restore probe.
  2. Call the real assessment path with amount=1, source=USD and target=USD.
  3. Independently calculate Math.abs(parsed baseline result - amount * parsed displayed rate); compare with 0.01.
  4. Inspect conversionAccurate and compare it with the expected outcome; confirm precision and update checks pass.
  5. Close the converter and discard this case's state.
- **Expected result:** conversionAccurate=true: difference is zero.

### TC-R19-02 - Within tolerance above
- **TC ID:** TC-R19-02
- **Title:** Within tolerance above
- **Requirement(s):** R19, R10
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=1; source=USD; target=USD; displayed rate="1"; baseline result="1.009"; visible=true; changed result="2.000"; restored result="1.009".
- **Steps:**
  1. Configure the fixture with the listed baseline values; return the changed and restored strings during the assessor's double-and-restore probe.
  2. Call the real assessment path with amount=1, source=USD and target=USD.
  3. Independently calculate Math.abs(parsed baseline result - amount * parsed displayed rate); compare with 0.01.
  4. Inspect conversionAccurate and compare it with the expected outcome; confirm precision and update checks pass.
  5. Close the converter and discard this case's state.
- **Expected result:** conversionAccurate=true: difference is below 0.01.

### TC-R19-03 - Within tolerance below
- **TC ID:** TC-R19-03
- **Title:** Within tolerance below
- **Requirement(s):** R19, R10
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=1; source=USD; target=USD; displayed rate="1"; baseline result="0.991"; visible=true; changed result="2.000"; restored result="0.991".
- **Steps:**
  1. Configure the fixture with the listed baseline values; return the changed and restored strings during the assessor's double-and-restore probe.
  2. Call the real assessment path with amount=1, source=USD and target=USD.
  3. Independently calculate Math.abs(parsed baseline result - amount * parsed displayed rate); compare with 0.01.
  4. Inspect conversionAccurate and compare it with the expected outcome; confirm precision and update checks pass.
  5. Close the converter and discard this case's state.
- **Expected result:** conversionAccurate=true: difference is below 0.01.

### TC-R19-04 - Exactly at tolerance
- **TC ID:** TC-R19-04
- **Title:** Exactly at tolerance
- **Requirement(s):** R19, R10
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=1; source=USD; target=USD; displayed rate="0.01"; baseline result="0.00"; visible=true; changed result="2.000"; restored result="0.00".
- **Steps:**
  1. Configure the fixture with the listed baseline values; return the changed and restored strings during the assessor's double-and-restore probe.
  2. Call the real assessment path with amount=1, source=USD and target=USD.
  3. Independently calculate Math.abs(parsed baseline result - amount * parsed displayed rate); compare with 0.01.
  4. Inspect conversionAccurate and compare it with the expected outcome; confirm precision and update checks pass.
  5. Close the converter and discard this case's state.
- **Expected result:** conversionAccurate=true: evaluated difference equals 0.01.

### TC-R19-05 - Above tolerance, high
- **TC ID:** TC-R19-05
- **Title:** Above tolerance, high
- **Requirement(s):** R19, R10
- **Type:** Negative
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=1; source=USD; target=USD; displayed rate="1"; baseline result="1.011"; visible=true; changed result="2.000"; restored result="1.011".
- **Steps:**
  1. Configure the fixture with the listed baseline values; return the changed and restored strings during the assessor's double-and-restore probe.
  2. Call the real assessment path with amount=1, source=USD and target=USD.
  3. Independently calculate Math.abs(parsed baseline result - amount * parsed displayed rate); compare with 0.01.
  4. Inspect conversionAccurate and compare it with the expected outcome; confirm precision and update checks pass.
  5. Close the converter and discard this case's state.
- **Expected result:** conversionAccurate=false: difference exceeds 0.01.

### TC-R19-06 - Above tolerance, low
- **TC ID:** TC-R19-06
- **Title:** Above tolerance, low
- **Requirement(s):** R19, R10
- **Type:** Negative
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=1; source=USD; target=USD; displayed rate="1"; baseline result="0.989"; visible=true; changed result="2.000"; restored result="0.989".
- **Steps:**
  1. Configure the fixture with the listed baseline values; return the changed and restored strings during the assessor's double-and-restore probe.
  2. Call the real assessment path with amount=1, source=USD and target=USD.
  3. Independently calculate Math.abs(parsed baseline result - amount * parsed displayed rate); compare with 0.01.
  4. Inspect conversionAccurate and compare it with the expected outcome; confirm precision and update checks pass.
  5. Close the converter and discard this case's state.
- **Expected result:** conversionAccurate=false: difference exceeds 0.01.

## R20 - Return a truthful precision flag

### TC-R20-01 - Exactly two digits
- **TC ID:** TC-R20-01
- **Title:** Exactly two digits
- **Requirement(s):** R20, R11
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** result text="92.35". amount=1; source=USD; target=USD; displayed rate="92.35"; visible=true; changed result="184.70"; restored result="92.35".
- **Steps:**
  1. Configure baseline result and rate with the exact strings listed; arrange a changed result distinct from baseline and an exact restoration.
  2. Call the real assess(1, "USD", "USD") path through that fixture.
  3. Count baseline fractional digits independently; inspect resultDecimalPlaces and decimalPrecisionMaintained.
  4. Compare decimalPrecisionMaintained with count >= 2 and the expected result; confirm accuracy and dynamic update pass.
  5. Close the converter and discard this case's state.
- **Expected result:** decimalPrecisionMaintained=true.

### TC-R20-02 - Three digits
- **TC ID:** TC-R20-02
- **Title:** Three digits
- **Requirement(s):** R20, R11
- **Type:** Positive
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** result text="92.350". amount=1; source=USD; target=USD; displayed rate="92.350"; visible=true; changed result="184.70"; restored result="92.350".
- **Steps:**
  1. Configure baseline result and rate with the exact strings listed; arrange a changed result distinct from baseline and an exact restoration.
  2. Call the real assess(1, "USD", "USD") path through that fixture.
  3. Count baseline fractional digits independently; inspect resultDecimalPlaces and decimalPrecisionMaintained.
  4. Compare decimalPrecisionMaintained with count >= 2 and the expected result; confirm accuracy and dynamic update pass.
  5. Close the converter and discard this case's state.
- **Expected result:** decimalPrecisionMaintained=true; trailing zero counts.

### TC-R20-03 - Four digits
- **TC ID:** TC-R20-03
- **Title:** Four digits
- **Requirement(s):** R20, R11
- **Type:** Positive
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** result text="0.0001". amount=1; source=USD; target=USD; displayed rate="0.0001"; visible=true; changed result="184.70"; restored result="0.0001".
- **Steps:**
  1. Configure baseline result and rate with the exact strings listed; arrange a changed result distinct from baseline and an exact restoration.
  2. Call the real assess(1, "USD", "USD") path through that fixture.
  3. Count baseline fractional digits independently; inspect resultDecimalPlaces and decimalPrecisionMaintained.
  4. Compare decimalPrecisionMaintained with count >= 2 and the expected result; confirm accuracy and dynamic update pass.
  5. Close the converter and discard this case's state.
- **Expected result:** decimalPrecisionMaintained=true.

### TC-R20-04 - One digit
- **TC ID:** TC-R20-04
- **Title:** One digit
- **Requirement(s):** R20, R11
- **Type:** Negative
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** result text="92.3". amount=1; source=USD; target=USD; displayed rate="92.3"; visible=true; changed result="184.70"; restored result="92.3".
- **Steps:**
  1. Configure baseline result and rate with the exact strings listed; arrange a changed result distinct from baseline and an exact restoration.
  2. Call the real assess(1, "USD", "USD") path through that fixture.
  3. Count baseline fractional digits independently; inspect resultDecimalPlaces and decimalPrecisionMaintained.
  4. Compare decimalPrecisionMaintained with count >= 2 and the expected result; confirm accuracy and dynamic update pass.
  5. Close the converter and discard this case's state.
- **Expected result:** decimalPrecisionMaintained=false.

### TC-R20-05 - No decimal point
- **TC ID:** TC-R20-05
- **Title:** No decimal point
- **Requirement(s):** R20, R11
- **Type:** Negative
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** result text="92". amount=1; source=USD; target=USD; displayed rate="92"; visible=true; changed result="184.70"; restored result="92".
- **Steps:**
  1. Configure baseline result and rate with the exact strings listed; arrange a changed result distinct from baseline and an exact restoration.
  2. Call the real assess(1, "USD", "USD") path through that fixture.
  3. Count baseline fractional digits independently; inspect resultDecimalPlaces and decimalPrecisionMaintained.
  4. Compare decimalPrecisionMaintained with count >= 2 and the expected result; confirm accuracy and dynamic update pass.
  5. Close the converter and discard this case's state.
- **Expected result:** decimalPrecisionMaintained=false.

### TC-R20-06 - Zero with two digits
- **TC ID:** TC-R20-06
- **Title:** Zero with two digits
- **Requirement(s):** R20, R11
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** result text="0.00". amount=1; source=USD; target=USD; displayed rate="0.00"; visible=true; changed result="184.70"; restored result="0.00".
- **Steps:**
  1. Configure baseline result and rate with the exact strings listed; arrange a changed result distinct from baseline and an exact restoration.
  2. Call the real assess(1, "USD", "USD") path through that fixture.
  3. Count baseline fractional digits independently; inspect resultDecimalPlaces and decimalPrecisionMaintained.
  4. Compare decimalPrecisionMaintained with count >= 2 and the expected result; confirm accuracy and dynamic update pass.
  5. Close the converter and discard this case's state.
- **Expected result:** decimalPrecisionMaintained=true; numeric magnitude does not affect digit count.

## R21 - Return a truthful dynamic-update flag

### TC-R21-01 - Increase and restore
- **TC ID:** TC-R21-01
- **Title:** Increase and restore
- **Requirement(s):** R21, R12
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=100; source=USD; target=USD; probe=200; restore=100.
- **Steps:**
  1. Run assess(100, "USD", "USD") and observe the baseline, doubled-amount and restored result strings.
  2. Independently determine whether changed text differs from baseline and restored text equals baseline.
  3. Inspect resultUpdatedOnChange and compare with the expected boolean.
  4. Confirm the original input amount and currencies are restored.
  5. Close the converter and discard this case's state.
- **Expected result:** resultUpdatedOnChange=true.

### TC-R21-02 - Fractional update
- **TC ID:** TC-R21-02
- **Title:** Fractional update
- **Requirement(s):** R21, R12
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=12.5; source=USD; target=USD; probe=25; restore=12.5.
- **Steps:**
  1. Run assess(12.5, "USD", "USD") and observe the baseline, doubled-amount and restored result strings.
  2. Independently determine whether changed text differs from baseline and restored text equals baseline.
  3. Inspect resultUpdatedOnChange and compare with the expected boolean.
  4. Confirm the original input amount and currencies are restored.
  5. Close the converter and discard this case's state.
- **Expected result:** resultUpdatedOnChange=true.

### TC-R21-03 - Different currencies
- **TC ID:** TC-R21-03
- **Title:** Different currencies
- **Requirement(s):** R21, R12
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=100; source=USD; target=EUR; probe=200; restore=100.
- **Steps:**
  1. Run assess(100, "USD", "EUR") and observe the baseline, doubled-amount and restored result strings.
  2. Independently determine whether changed text differs from baseline and restored text equals baseline.
  3. Inspect resultUpdatedOnChange and compare with the expected boolean.
  4. Confirm the original input amount and currencies are restored.
  5. Close the converter and discard this case's state.
- **Expected result:** resultUpdatedOnChange=true when changed text differs and restored text matches.

### TC-R21-04 - Frozen result
- **TC ID:** TC-R21-04
- **Title:** Frozen result
- **Requirement(s):** R21, R12
- **Type:** Negative
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=100; source=USD; target=USD; baseline="100.00"; rate="1.000000"; changed="100.00"; restored="100.00"; visible=true.
- **Steps:**
  1. Configure the exact baseline, changed and restored strings listed.
  2. Run the real assess(100, "USD", "USD") path through the fixture.
  3. Confirm the dynamic probe attempts 200 and restoration attempts 100.
  4. Inspect resultUpdatedOnChange and verify false is returned for the listed failed condition.
  5. Close the converter and discard this case's state.
- **Expected result:** resultUpdatedOnChange=false.

### TC-R21-05 - Change hidden by rounding
- **TC ID:** TC-R21-05
- **Title:** Change hidden by rounding
- **Requirement(s):** R21, R12
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** Converter is open in a clean state; dot-decimal locale is fixed; no prior scenario is running.
- **Test data:** amount=0.001; source=USD; target=USD; probe=0.002; restore=0.001.
- **Steps:**
  1. Run assess(0.001, "USD", "USD") and observe the baseline, doubled-amount and restored result strings.
  2. Independently determine whether changed text differs from baseline and restored text equals baseline.
  3. Inspect resultUpdatedOnChange and compare with the expected boolean.
  4. Confirm the original input amount and currencies are restored.
  5. Close the converter and discard this case's state.
- **Expected result:** resultUpdatedOnChange=false because displayed result never changes.

### TC-R21-06 - Restoration fails
- **TC ID:** TC-R21-06
- **Title:** Restoration fails
- **Requirement(s):** R21, R12
- **Type:** Negative
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=100; source=USD; target=USD; baseline="100.00"; rate="1.000000"; changed="200.00"; restored="150.00"; visible=true.
- **Steps:**
  1. Configure the exact baseline, changed and restored strings listed.
  2. Run the real assess(100, "USD", "USD") path through the fixture.
  3. Confirm the dynamic probe attempts 200 and restoration attempts 100.
  4. Inspect resultUpdatedOnChange and verify false is returned for the listed failed condition.
  5. Close the converter and discard this case's state.
- **Expected result:** resultUpdatedOnChange=false.

## R22 - Return a truthful completion flag

### TC-R22-01 - All conditions pass
- **TC ID:** TC-R22-01
- **Title:** All conditions pass
- **Requirement(s):** R22
- **Type:** Positive
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=100; source=USD; target=USD; rate="1"; baseline="100.00"; changed="200.00"; restored="100.00"; visible=true.
- **Steps:**
  1. Arrange the listed fixture responses to match this case, including its passing or failing conditions; keep all result strings parseable.
  2. Run the real assess(100, "USD", "USD") path; retain the returned record and observed selection/visibility.
  3. Independently verify accuracy, decimal count, update/restoration and actual selected currencies from fixture evidence.
  4. Inspect conversionComplete and compare with the expected result; record a requirement ambiguity or defect rather than modifying application behavior.
  5. Close the converter and discard this case's state.
- **Expected result:** conversionComplete=true.

### TC-R22-02 - Accuracy fails
- **TC ID:** TC-R22-02
- **Title:** Accuracy fails
- **Requirement(s):** R22
- **Type:** Negative
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=100; source=USD; target=USD; rate="1"; baseline="100.02"; changed="200.02"; restored="100.02"; visible=true.
- **Steps:**
  1. Arrange the listed fixture responses to match this case, including its passing or failing conditions; keep all result strings parseable.
  2. Run the real assess(100, "USD", "USD") path; retain the returned record and observed selection/visibility.
  3. Independently verify accuracy, decimal count, update/restoration and actual selected currencies from fixture evidence.
  4. Inspect conversionComplete and compare with the expected result; record a requirement ambiguity or defect rather than modifying application behavior.
  5. Close the converter and discard this case's state.
- **Expected result:** conversionComplete=false.

### TC-R22-03 - Precision fails
- **TC ID:** TC-R22-03
- **Title:** Precision fails
- **Requirement(s):** R22
- **Type:** Negative
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=100; source=USD; target=USD; rate="1"; baseline="100.0"; changed="200.0"; restored="100.0"; visible=true.
- **Steps:**
  1. Arrange the listed fixture responses to match this case, including its passing or failing conditions; keep all result strings parseable.
  2. Run the real assess(100, "USD", "USD") path; retain the returned record and observed selection/visibility.
  3. Independently verify accuracy, decimal count, update/restoration and actual selected currencies from fixture evidence.
  4. Inspect conversionComplete and compare with the expected result; record a requirement ambiguity or defect rather than modifying application behavior.
  5. Close the converter and discard this case's state.
- **Expected result:** conversionComplete=false.

### TC-R22-04 - Update fails
- **TC ID:** TC-R22-04
- **Title:** Update fails
- **Requirement(s):** R22
- **Type:** Negative
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=100; source=USD; target=USD; rate="1"; baseline="100.00"; changed="100.00"; restored="100.00"; visible=true.
- **Steps:**
  1. Arrange the listed fixture responses to match this case, including its passing or failing conditions; keep all result strings parseable.
  2. Run the real assess(100, "USD", "USD") path; retain the returned record and observed selection/visibility.
  3. Independently verify accuracy, decimal count, update/restoration and actual selected currencies from fixture evidence.
  4. Inspect conversionComplete and compare with the expected result; record a requirement ambiguity or defect rather than modifying application behavior.
  5. Close the converter and discard this case's state.
- **Expected result:** conversionComplete=false.

### TC-R22-05 - Visibility fails
- **TC ID:** TC-R22-05
- **Title:** Visibility fails
- **Requirement(s):** R22
- **Type:** Negative
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=100; source=USD; target=USD; rate="1"; baseline="100.00"; changed="200.00"; restored="100.00"; initial wait=false; update waits=true.
- **Steps:**
  1. Arrange the listed fixture responses to match this case, including its passing or failing conditions; keep all result strings parseable.
  2. Run the real assess(100, "USD", "USD") path; retain the returned record and observed selection/visibility.
  3. Independently verify accuracy, decimal count, update/restoration and actual selected currencies from fixture evidence.
  4. Inspect conversionComplete and compare with the expected result; record a requirement ambiguity or defect rather than modifying application behavior.
  5. Close the converter and discard this case's state.
- **Expected result:** conversionComplete=false.

### TC-R22-06 - Multiple failures
- **TC ID:** TC-R22-06
- **Title:** Multiple failures
- **Requirement(s):** R22
- **Type:** Negative
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor.
- **Test data:** amount=100; source=USD; target=USD; rate="1"; baseline="100.1"; changed="200.1"; restored="100.1"; visible=true.
- **Steps:**
  1. Arrange the listed fixture responses to match this case, including its passing or failing conditions; keep all result strings parseable.
  2. Run the real assess(100, "USD", "USD") path; retain the returned record and observed selection/visibility.
  3. Independently verify accuracy, decimal count, update/restoration and actual selected currencies from fixture evidence.
  4. Inspect conversionComplete and compare with the expected result; record a requirement ambiguity or defect rather than modifying application behavior.
  5. Close the converter and discard this case's state.
- **Expected result:** conversionComplete=false.

### TC-R22-07 - Incorrect returned field
- **TC ID:** TC-R22-07
- **Title:** Incorrect returned field
- **Requirement(s):** R22
- **Type:** Negative
- **Priority:** High
- **Preconditions:** A controlled test fixture can supply the specified result text, rate, visibility and update sequence to the real assessment path. This is a fixture-dependent design; mark Not Run if that fixture is unavailable. Do not construct a result record as a substitute for exercising the assessor. An approved fault-injection seam can make source selection disagree with the requested source before result creation; R22 field-correctness semantics require PD review.
- **Test data:** amount=100; requested source=USD; actual selected source=EUR; target=USD; controlled rate="1"; baseline="100.00"; changed="200.00"; restored="100.00"; visible=true.
- **Steps:**
  1. Arrange the listed fixture responses to match this case, including its passing or failing conditions; keep all result strings parseable.
  2. Run the real assess(100, "USD", "USD") path; retain the returned record and observed selection/visibility.
  3. Independently verify accuracy, decimal count, update/restoration and actual selected currencies from fixture evidence.
  4. Inspect conversionComplete and compare with the expected result; record a requirement ambiguity or defect rather than modifying application behavior.
  5. Close the converter and discard this case's state.
- **Expected result:** Under the full R22 requirement, completion must not be reported true; flag any contrary behavior as a defect.

## Traceability matrix

| Requirement | Dedicated cases |
|---|---|
| R1 | TC-R1-01 through TC-R1-09 |
| R2 | TC-R2-01 through TC-R2-08 |
| R3 | TC-R3-01 through TC-R3-07 |
| R4 | TC-R4-01 through TC-R4-09 |
| R5 | TC-R5-01 through TC-R5-09 |
| R6 | TC-R6-01 through TC-R6-06 |
| R7 | TC-R7-01 through TC-R7-07 |
| R8 | TC-R8-01 through TC-R8-08 |
| R9 | TC-R9-01 through TC-R9-06 |
| R10 | TC-R10-01 through TC-R10-06 |
| R11 | TC-R11-01 through TC-R11-06 |
| R12 | TC-R12-01 through TC-R12-06 |
| R13 | TC-R13-01 through TC-R13-06 |
| R14 | TC-R14-01 through TC-R14-08 |
| R15 | TC-R15-01 through TC-R15-08 |
| R16 | TC-R16-01 through TC-R16-06 |
| R17 | TC-R17-01 through TC-R17-06 |
| R18 | TC-R18-01 through TC-R18-06 |
| R19 | TC-R19-01 through TC-R19-06 |
| R20 | TC-R20-01 through TC-R20-06 |
| R21 | TC-R21-01 through TC-R21-06 |
| R22 | TC-R22-01 through TC-R22-07 |

## Assumptions and questions

### R1
Direct numeric validation only. R1 defines no positive minimum or upper limit. NaN and infinity require clarification; conversion overflow and GUI formatting are separate concerns.

### R2
Null is no value; an empty string has zero characters. Whitespace and unsupported codes need separate expectations.

### R3
Quotes identify text and are not typed. Text preservation is an assumption; R8 formats a separate input string. Keyboard editing is manual coverage; the supplied driver sets text directly.

### R4
All seven supported currencies are covered, including a same-currency pair. Keyboard navigation and focus persistence are manual checks; driver selection alone does not prove keyboard behavior.

### R5
All seven supported currencies are covered, including a same-currency pair. Keyboard navigation and focus persistence are manual checks; driver selection alone does not prove keyboard behavior.

### R6
Delayed visibility requires a controlled fixture beyond the current synchronous UI. Timeout failure is false, not an exception. Visibility does not guarantee current result contents.

### R7
R7 verifies extraction, not arithmetic accuracy. Numeric values do not retain trailing-zero formatting; preserve original strings for decimal-count tests.

### R8
Check exact strings and exactly two fractional digits. Formatting does not change the original numeric amount or require replacing GUI text. The original 0.001 passes R1.

### R9
Count characters after the decimal point, including trailing zeros. Fixtures use plain numeric strings; scientific notation, commas and malformed text are outside the stated contract.

### R10
Controlled fixtures isolate the predicate; they are not necessarily real UI conversions. The exact-boundary fixture avoids subtracting two nearly equal values. Use the displayed rate as required; rounded rates can cause larger errors for large amounts.

### R11
The real UI normally displays two decimals. Nonstandard precision strings require helper-level fixtures; no application changes are assumed.

### R12
The supplied verifyDynamicUpdate doubles the amount and checks result-text change plus restored result text. Decrease/repeated-change cases need separate driver sequences. Check restored input independently; the helper only verifies restored result text.

### R13
Compare the original double value exactly for this pass-through field. A false completion flag caused by rounded display does not justify changing inputAmount.

### R14
Check the dropdown selection independently, rather than only comparing the returned field with the argument passed to assess.

### R15
Check the dropdown selection independently, rather than only comparing the returned field with the argument passed to assess.

### R16
R16 checks the observed UI value, not a separately recomputed mathematical value. Numeric comparison may use a small floating-point delta appropriate to parsing.

### R17
Field counts the formatted input string, not the raw amount text or the double representation.

### R18
Nonstandard display strings are controlled tests, not ordinary UI inputs. R18 reports the count even when R11 fails.

### R19
Tests trace both the numeric predicate (R10) and its returned field (R19). Controlled full-assessment fixtures require a test seam; direct construction of a record does not test the assessor.

### R20
Tests trace both the precision rule (R11) and returned flag (R20). Nonstandard UI output requires controlled fixtures.

### R21
The current helper requires both visible text change and restoration. R21 wording emphasizes update, while the helper also incorporates R12 cleanup; confirm this interpretation with reviewers.

### R22
Current code computes complete = visible && accurate && precise && updated. It does not independently validate every returned field or restored input. The final case is a requirement-driven fault-injection design, not a passing claim about current code. Clarify whether R22 requires explicit field-correctness checks.

## Sources and AI disclosure

Project README.md supplies the required template, R1-R22 and assessment rules. ConversionAssessor.java and ConverterDriver.java supply helper behavior. Test ideas originate from the project discussion. OpenAI Codex assisted with preparation; disclose this in SOLUTION.md when that deliverable is written.
