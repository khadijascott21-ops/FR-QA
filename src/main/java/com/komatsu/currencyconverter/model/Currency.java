package com.komatsu.currencyconverter.model;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;

/**
 * Supported currencies together with their rate relative to USD.
 */
public enum Currency {
    /** United States dollar (base currency). */
    USD(1.0),
    /** Euro. */
    EUR(0.862623),
    /** British pound. */
    GBP(0.749624),
    /** Japanese yen. */
    JPY(159.250691),
    /** Canadian dollar. */
    CAD(1.371967),
    /** Australian dollar. */
    AUD(1.421005),
    /** Swiss franc. */
    CHF(0.787974);

    private final double rateToUsd;

    Currency(double rateToUsd) {
        this.rateToUsd = rateToUsd;
    }

    /**
     * Returns how many units of this currency equal one USD.
     *
     * @return rate relative to USD
     */
    public double getRateToUsd() {
        return rateToUsd;
    }

    /**
     * Finds a currency by its ISO code.
     *
     * @param code the code, case-insensitive, surrounding blanks ignored
     * @return the matching currency, or empty when null, blank or unsupported
     */
    public static Optional<Currency> fromCode(String code) {
        if (code == null || code.isBlank()) {
            return Optional.empty();
        }
        String normalized = code.trim();
        return Arrays.stream(values()).filter(c -> c.name().equalsIgnoreCase(normalized)).findFirst();
    }

    /**
     * Lists the supported currency codes in declaration order.
     *
     * @return immutable list of codes
     */
    public static List<String> codes() {
        return Arrays.stream(values()).map(Enum::name).toList();
    }
}
