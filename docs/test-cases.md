# Currency Converter - R1 Test Cases

Status: Draft manual test design. These cases have not been executed or approved by the PD Team.

## Scope

**R1:** Throw `IllegalArgumentException` if `amount <= 0`.

These nine cases exercise numeric validation directly through the provided
`ConversionAssessor.validate(amount, source, target)` method. Valid currency codes
keep R2 from interfering. Passing R1 means the amount is accepted by validation;
it does not guarantee that a later GUI conversion succeeds.

## Test cases

### TC-01 - Reject zero amount
- **Requirement(s):** R1
- **Type:** Boundary
- **Priority:** High
- **Preconditions:** Input validation is available.
- **Test data:** amount = `0.0`, source = `"USD"`, target = `"EUR"`
- **Steps:**
  1. Supply amount `0.0` and the valid currency codes.
  2. Run input validation.
  3. Check the exception thrown.
- **Expected result:** Validation throws `IllegalArgumentException` because the amount equals zero.

### TC-02 - Reject negative zero
- **Requirement(s):** R1
- **Type:** Edge
- **Priority:** Medium
- **Preconditions:** Input validation is available and accepts Java `double` values.
- **Test data:** amount = `-0.0`, source = `"USD"`, target = `"EUR"`
- **Steps:**
  1. Supply amount `-0.0` and the valid currency codes.
  2. Run input validation.
  3. Check the exception thrown.
- **Expected result:** Validation throws `IllegalArgumentException` because Java considers `-0.0 <= 0` true.

### TC-03 - Reject a negative whole amount
- **Requirement(s):** R1
- **Type:** Negative
- **Priority:** High
- **Preconditions:** Input validation is available.
- **Test data:** amount = `-100.0`, source = `"USD"`, target = `"EUR"`
- **Steps:**
  1. Supply amount `-100.0` and the valid currency codes.
  2. Run input validation.
  3. Check the exception thrown.
- **Expected result:** Validation throws `IllegalArgumentException` because the amount is below zero.

### TC-04 - Reject a negative fractional amount
- **Requirement(s):** R1
- **Type:** Negative
- **Priority:** High
- **Preconditions:** Input validation is available.
- **Test data:** amount = `-0.01`, source = `"USD"`, target = `"EUR"`
- **Steps:**
  1. Supply amount `-0.01` and the valid currency codes.
  2. Run input validation.
  3. Check the exception thrown.
- **Expected result:** Validation throws `IllegalArgumentException` because a negative fraction is still below zero.

### TC-05 - Reject the negative double value closest to zero
- **Requirement(s):** R1
- **Type:** Boundary
- **Priority:** Medium
- **Preconditions:** Input validation is available and accepts Java `double` values directly.
- **Test data:** amount = `-Double.MIN_VALUE`, source = `"USD"`, target = `"EUR"`
- **Steps:**
  1. Set the amount to `-Double.MIN_VALUE`, the negative representable `double` closest to zero.
  2. Supply the amount and valid currency codes to input validation.
  3. Check the exception thrown.
- **Expected result:** Validation throws `IllegalArgumentException` because the amount is below zero, despite its extremely small magnitude.

### TC-06 - Reject the largest finite negative magnitude
- **Requirement(s):** R1
- **Type:** Boundary
- **Priority:** Medium
- **Preconditions:** Input validation is available and accepts Java `double` values directly.
- **Test data:** amount = `-Double.MAX_VALUE`, source = `"USD"`, target = `"EUR"`
- **Steps:**
  1. Set the amount to `-Double.MAX_VALUE`.
  2. Supply the amount and valid currency codes to input validation.
  3. Check the exception thrown.
- **Expected result:** Validation throws `IllegalArgumentException` because the amount is below zero.

### TC-07 - Accept the smallest positive double value
- **Requirement(s):** R1
- **Type:** Boundary
- **Priority:** Medium
- **Preconditions:** Input validation is available and accepts Java `double` values directly.
- **Test data:** amount = `Double.MIN_VALUE`, source = `"USD"`, target = `"EUR"`
- **Steps:**
  1. Set the amount to `Double.MIN_VALUE`, the smallest positive representable `double`.
  2. Supply the amount and valid currency codes to input validation.
  3. Check whether validation accepts the amount.
- **Expected result:** Amount validation passes without throwing `IllegalArgumentException` because the amount is greater than zero.

### TC-08 - Accept a typical positive amount
- **Requirement(s):** R1
- **Type:** Positive
- **Priority:** High
- **Preconditions:** Input validation is available.
- **Test data:** amount = `100.0`, source = `"USD"`, target = `"EUR"`
- **Steps:**
  1. Supply amount `100.0` and the valid currency codes.
  2. Run input validation.
  3. Check whether validation accepts the amount.
- **Expected result:** Amount validation passes without throwing `IllegalArgumentException` because the amount is greater than zero.

### TC-09 - Accept the largest finite positive double value
- **Requirement(s):** R1
- **Type:** Boundary
- **Priority:** Medium
- **Preconditions:** Input validation is available and accepts Java `double` values directly.
- **Test data:** amount = `Double.MAX_VALUE`, source = `"USD"`, target = `"EUR"`
- **Steps:**
  1. Set the amount to `Double.MAX_VALUE`.
  2. Supply the amount and valid currency codes to input validation.
  3. Check whether validation accepts the amount.
- **Expected result:** Amount validation passes without throwing `IllegalArgumentException` because the amount is greater than zero and R1 specifies no upper limit.

## Traceability matrix

| Requirement | Test cases | Coverage status |
|-------------|------------|-----------------|
| R1 | TC-01, TC-02, TC-03, TC-04, TC-05, TC-06, TC-07, TC-08, TC-09 | Designed; not executed |
| R2-R22 | None in this document | Outside this R1 draft's scope |

## Assumptions and questions

1. R1 defines numeric validation only. Blank input, nonnumeric text, and parsing
   the string `"100"` need separate input-handling cases.
2. R1 specifies no minimum positive amount or maximum amount. Finite positive
   values therefore pass amount validation, including `Double.MIN_VALUE` and
   `Double.MAX_VALUE`.
3. `Double.MIN_VALUE` means the smallest positive nonzero `double`, not the most
   negative value. `-Double.MAX_VALUE` is the most negative finite `double`.
4. Extreme values are supplied directly to validation, without GUI formatting,
   conversion arithmetic, or rounding. Those later operations have separate risks.
5. Negative zero must be rejected because it satisfies `amount <= 0` in Java.
6. Expected handling of `NaN` and infinity requires clarification; these values
   are excluded from this draft.
7. The complete Phase 1 submission still needs cases and traceability for R2-R22.
   PD Team approval is required before Phase 3 automation begins.

## Use of AI

OpenAI Codex assisted with designing and formatting these test cases and preparing
the repository upload. This is a design document, not a record of test execution.
Include this assistance in `SOLUTION.md` when that deliverable is prepared.
