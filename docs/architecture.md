# Architecture

```
 App ──► ConverterWindow (Lanterna, implements ConversionView)
              │ events                  ▲ showResult/hideResult/showError
              ▼                         │
        ConverterPresenter ─────────────┘
              │
              ▼
        CurrencyConverter ──► Currency (rates)
```

Layers: `ui` → `service` → `model`; dependencies point inward only. The presenter depends on the `ConversionView` interface, not on Lanterna.

## Build and delivery
- Maven, Java 17 (`maven.compiler.release`), jar manifest declares the main class and `lib/` classpath.
- Default lifecycle: compile → `test` (surefire runs TestNG unit tests; `**/acceptance/**` excluded).
- Profile `acceptance`: surefire execution bound to `integration-test` runs `AcceptanceRunner` (Cucumber).
- Profile `distribution`: maven-assembly-plugin (`src/assembly/distribution.xml`) builds a zip containing the jar, `lib/`, `bin/` launch scripts and `docs/`.

## Source layout
```
src/main/java/com/komatsu/currencyconverter/{model,service,ui}, App.java
src/test/java/.../unit            TestNG unit tests
src/test/java/.../acceptance      Cucumber runner, steps, driver
src/test/resources/features       Gherkin feature
src/assembly/distribution.xml     Assembly descriptor
scripts/                          run.sh, run.bat
docs/                             documentation
```
