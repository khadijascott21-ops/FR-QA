package com.komatsu.currencyconverter.unit;

import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertThrows;

import com.komatsu.currencyconverter.model.Currency;
import com.komatsu.currencyconverter.service.CurrencyConverter;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

/** Unit tests for {@link CurrencyConverter}. */
public class CurrencyConverterTest {

    private final CurrencyConverter converter = new CurrencyConverter();

    @Test
    public void usdToEurUsesRate() {
        assertEquals(converter.convert(100, "USD", "EUR"), 86.2623, 1e-9);
    }

    @Test
    public void sameCurrencyIsIdentity() {
        assertEquals(converter.convert(42.5, "JPY", "JPY"), 42.5, 1e-9);
    }

    @DataProvider
    public Object[][] pairs() {
        return Currency.codes().stream()
                .flatMap(s -> Currency.codes().stream().map(t -> new Object[] {s, t}))
                .toArray(Object[][]::new);
    }

    @Test(dataProvider = "pairs")
    public void rateMatchesFormula(String source, String target) {
        double expected = Currency.valueOf(target).getRateToUsd() / Currency.valueOf(source).getRateToUsd();
        assertEquals(converter.rate(source, target), expected, 1e-12);
        assertEquals(converter.convert(10, source, target), 10 * expected, 1e-9);
    }

    @DataProvider
    public Object[][] invalidAmounts() {
        return new Object[][] {{0.0}, {-1.0}, {Double.NaN}, {Double.POSITIVE_INFINITY}};
    }

    @Test(dataProvider = "invalidAmounts")
    public void invalidAmountIsRejected(double amount) {
        assertThrows(IllegalArgumentException.class, () -> converter.convert(amount, "USD", "EUR"));
    }

    @DataProvider
    public Object[][] invalidCodes() {
        return new Object[][] {{null, "EUR"}, {"", "EUR"}, {"  ", "EUR"}, {"USD", null}, {"USD", ""}, {"USD", "XXX"}};
    }

    @Test(dataProvider = "invalidCodes")
    public void invalidCodeIsRejected(String source, String target) {
        assertThrows(IllegalArgumentException.class, () -> converter.convert(1, source, target));
    }

    @Test
    public void codesAreCaseInsensitive() {
        assertEquals(converter.rate("usd", " eur "), Currency.EUR.getRateToUsd(), 1e-12);
    }
}
