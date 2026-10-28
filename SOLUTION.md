# Currency converter automation

## Approach

The feature file follows the 14 cases currently documented in `docs/test-cases.md`.
Scenario outlines cover repeated amounts, both directions of the JPY/GBP conversion,
all seven supported currencies, and null/empty source and target codes. The outlines
expand to 33 executable scenarios. Each scenario is tagged with its case ID, type,
and requirements.

Expected result and exchange-rate strings come from the documented fixed-rate cases.
Accuracy assertions use the rate displayed in the GUI and keep the required 0.01
tolerance. Exact text assertions check rounding, trailing zeroes and large amounts;
numeric assertions use a delta.

## Coverage

| Requirements | Automated cases and checks |
|---|---|
| R1 | TC-02/03 check visible rejection and the validator's exception; TC-09 accepts a positive boundary amount. |
| R2 | TC-04 checks GUI prevention and directly validates null/empty codes in both positions. |
| R3-R7 | Conversion scenarios enter amounts, select both currencies, wait for visibility and read the displayed amount/rate; TC-05 covers all dropdown choices. |
| R8-R9 | TC-01/08 check formatted input and the returned decimal counts; TC-08 explicitly checks `String.format("%.2f", amount)`. |
| R10-R11 | Conversion scenarios check accuracy and displayed precision; TC-13 checks the documented accuracy failure. |
| R12 | TC-11 compares changed/restored results; TC-14 checks the rounded-display limitation and restoration. |
| R13-R18 | TC-01 checks all six value/count fields; TC-08/12/13/14 add rounding, changed-input and edge-case values. |
| R19-R22 | TC-01/08/09/11/12 expect all flags true; TC-13/14 check accuracy/update failures and incomplete results. |

The null/empty-code scenarios exercise the supplied `ConversionAssessor.validate`
method because those values cannot be selected in the GUI. `<null>` and `<empty>`
are explicit data tokens decoded by `InputSteps`. Existing service unit tests also
verify invalid currency codes. A GUI prevention check alone does not demonstrate an
exception, so it is kept separate from these code-level checks.

## Automation design

`InputSteps` opens the real GUI on the supplied virtual terminal, enters amounts,
selects currencies and verifies validation. TC-04 traverses the public component
tree to find the two dropdowns, sends character/Backspace/Delete events, and checks
the available options without reflection or changes to application code.

`ConversionSteps` checks displayed results, captures assessments, asserts every
`ConversionResult` field, and compares results before/after changing the amount.
The assessor must restore the original numeric amount after its dynamic check;
the step then restores the original text too, preserving inputs such as `100`.

Both classes share state only through the existing `ScenarioContext`. Setup creates
the driver/assessor lazily and the existing hooks fix the locale and close each GUI.
Step definitions use the driver's waiting instead of adding sleeps.

One supplied helper required a correction: `ConverterDriver.render()` now calls
`gui.getGUIThread().processEventsAndUpdate()`. The old input/draw calls did not
execute queued dropdown listeners, so selecting a different pair left the displayed
rate at the prior pair until another amount edit. The event-loop call processes
those listeners before returning. Conversion scenarios caught this problem and
passed after the correction. Application code, dependencies and the other supplied
helpers are unchanged.

## Run and validation

Run with Java 17+ and Maven from the repository root:

```sh
mvn verify -P acceptance
```

The HTML report is `target/cucumber-report.html`; TestNG/Surefire results are in
`target/surefire-reports/`.

Validated on October 24, 2026: 67 unit tests and 33 acceptance scenarios passed,
with zero failures, errors or skipped scenarios. The command used in this restricted
session was:

```sh
mvn -o -Daether.syncContext.named.factory=noop verify -P acceptance
```

Offline mode uses cached dependencies; the lock setting avoids writes to the
read-only shared Maven cache for this single build. A separate `clean verify`
attempt could not start because Maven's selected clean plugin 3.5.0 was not cached.
The successful `verify` run recompiled the changed test sources.

A subsequent verification reran all 67 unit tests and 33 acceptance scenarios
successfully. A separate temporary Java audit, `target/AccuracyAudit.java`, checked
all 49 currency pairs at seven amounts (`0.001`, `0.01`, `1.234`, `100`, `250.75`,
`1000`, `1000000`) against an independent `BigDecimal` DECIMAL128 reference using
the project's fixed rates. All 343 displayed conversion amounts and rates matched
the independently rounded reference, and state restoration checks passed. The
largest unrounded service calculation difference was approximately `3.04e-8`.

The audit found one additional boundary sensitivity affecting two assessment fields,
described below; its nonzero exit status records that discrepancy. The full outputs
are `target/accuracy-verification.log` and `target/independent-accuracy-audit.txt`.

## Defects and observations

- **TC-13:** 1,000,000 JPY to GBP displays `4707.19` at rate `0.004707`. The
  displayed-rate calculation differs by approximately `0.19`, exceeding R10's
  `0.01` tolerance. The assessment correctly returns `conversionAccurate=false`
  and `conversionComplete=false`.
- **TC-14:** `0.001` and `0.002` USD both display `0.00` when converted to USD.
  The visible result cannot demonstrate an update. The assessment correctly
  returns `resultUpdatedOnChange=false` and `conversionComplete=false`, and the
  original amount is restored.
- **Additional tolerance boundary:** 1,000,000 JPY to CHF displays `4948.01` at
  rate `0.004948`. Exact decimal arithmetic gives an error of `0.01`, which is
  within the inclusive tolerance. Java double subtraction produces
  `0.010000000000218279`, so the supplied assessor reports both
  `conversionAccurate=false` and `conversionComplete=false`. This follows the
  README's literal Java expression but disagrees with the exact decimal boundary.
  No application or assessor behavior was changed to hide this difference.

TC-13 and TC-14 carry `@known-limitation` and assert the documented observations
and false flags. Their passing status verifies detection of those limitations;
it does not mean R10/R12 are satisfied for those inputs. If either behavior changes,
its scenario will fail and should be reviewed against the requirements.

## AI and external resources

OpenAI Codex reviewed the repository and manual cases, wrote the feature scenarios
and step definitions, corrected the driver's event processing, and ran Maven checks.
Lanterna APIs were inspected from the locally installed dependency using `javap`.
No external websites or additional dependencies were used.

## Further improvements

Resolve whether accuracy should use the full exchange rate or the rounded displayed
rate, and whether sub-cent changes must produce a visibly different amount. Extend
the design for nonnumeric/nonfinite inputs and add CI execution after those cases
and the known-limitations policy are agreed with the reviewing team.
