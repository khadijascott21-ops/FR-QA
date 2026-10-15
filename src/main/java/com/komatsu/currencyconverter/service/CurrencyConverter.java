package com.komatsu.currencyconverter.service;

import com.komatsu.currencyconverter.model.Currency;

/**
 * Converts amounts between supported currencies.
 */
public class CurrencyConverter {

    /**
     * Computes the exchange rate {@code RATES[target] / RATES[source]}.
     *
     * @param source source currency code
     * @param target target currency code
     * @return the exchange rate
     * @throws IllegalArgumentException if a code is null, empty or unsupported
     */
    public double rate(String source, String target) {
        Currency from = parse(source, "source");
        Currency to = parse(target, "target");
        return to.getRateToUsd() / from.getRateToUsd();
    }

    /**
     * Converts an amount.
     *
     * @param amount amount in the source currency, must be greater than zero
     * @param source source currency code
     * @param target target currency code
     * @return the amount expressed in the target currency
     * @throws IllegalArgumentException if amount &lt;= 0 (or not finite) or a code is invalid
     */
    public double convert(double amount, String source, String target) {
        if (!Double.isFinite(amount) || amount <= 0) {
            throw new IllegalArgumentException("Amount must be greater than zero: " + amount);
        }
        return amount * rate(source, target);
    }

    private static Currency parse(String code, String role) {
        if (code == null || code.isBlank()) {
            throw new IllegalArgumentException("The " + role + " currency is required");
        }
        return Currency.fromCode(code)
                .orElseThrow(() -> new IllegalArgumentException("Unsupported " + role + " currency: " + code));
    }
}
