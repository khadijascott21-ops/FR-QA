# User Manual

## Requirements
Java 17+ and a terminal of at least 60x15 characters. Building needs Maven 3.8.1+.

## Running
- From source: `mvn package` then `scripts/run.sh` (macOS/Linux) or `scripts\run.bat` (Windows).
- From the distribution zip: unzip, then run `bin/run.sh` or `bin\run.bat`.

## Using the converter
1. Type the **Amount** (a number greater than zero).
2. Pick the **From** currency; press Enter on the dropdown and use the arrow keys.
3. Pick the **To** currency the same way.
4. The **Converted amount** and **Exchange rate** appear automatically and update on every change.
5. Use Tab / Shift+Tab to move between fields; choose **Quit** to exit.

Supported currencies: USD, EUR, GBP, JPY, CAD, AUD, CHF.

Result = `amount * (RATES[target] / RATES[source])`, shown with 2 decimals; the rate is shown with 6.

## Messages
| Message | Meaning |
|---|---|
| Amount must be a number | The amount is not numeric |
| Amount must be greater than zero | Zero or negative amount |

## Build, test, package
| Command | Purpose |
|---|---|
| `mvn test` | TestNG unit tests |
| `mvn verify -Pacceptance` | Build, then run Cucumber acceptance tests (report: `target/cucumber-report.html`) |
| `mvn package -Pdistribution` | Create `target/currency-converter-1.0.0-dist.zip` |
