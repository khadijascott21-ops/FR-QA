# Design

## Goals
Correct conversion, strict validation, and a GUI that is testable headlessly.

## Classes
| Class | Responsibility |
|---|---|
| `model.Currency` | Enum of supported currencies and their USD rates; lookup by code |
| `model.ConversionResult` | Immutable record of a conversion as observed in the UI (10 fields) |
| `service.CurrencyConverter` | Validates input (`IllegalArgumentException` when amount <= 0 or codes null/empty/unsupported) and applies `RATES[target] / RATES[source]` |
| `ui.ConversionView` | Output interface (show result / hide / show error) |
| `ui.ConverterPresenter` | Parses form input, calls the service, drives the view; contains no Lanterna code |
| `ui.ConverterWindow` | Lanterna window: amount `TextBox`, two `ComboBox` dropdowns, result container panel, Quit button |
| `App` | Entry point; creates the terminal screen and shows the window |

## Behaviour decisions
- Results are recomputed on every amount or dropdown change (no Convert button).
- The result container is hidden until a valid conversion exists.
- Formatting uses `Locale.ROOT` so output is deterministic.
- Dependencies are injected by constructor (service into window/presenter, view into presenter).

## Test design
- Unit tests (TestNG, `src/test/.../unit`) run in the `test` phase.
- Acceptance tests (Cucumber + TestNG, `.../acceptance`): one scenario (or outline) per requirement in `currency_conversion.feature`. `ConverterDriver` operates the real `ConverterWindow` on a Lanterna `DefaultVirtualTerminal`; `ConversionAssessor` performs the end-to-end check and builds the `ConversionResult`; step classes are split by concern and share a `ScenarioContext` through PicoContainer.
- Accuracy check `Math.abs(result - amount * rate) <= 0.01` uses the displayed (rounded) values.

## Dependency policy
All versions are Maven properties. Runtime: Lanterna only. Test: TestNG, Cucumber. A scan of all 24 resolved artifacts with OSV (2026-10-02) reported no known vulnerabilities.
