package com.komatsu.currencyconverter.model;

/**
 * Immutable outcome of a conversion as observed through the user interface.
 *
 * @param inputAmount                exact amount entered
 * @param sourceCurrency             selected source currency code
 * @param targetCurrency             selected target currency code
 * @param conversionResult           converted amount shown by the UI
 * @param inputDecimalPlaces         decimal places of the formatted input amount
 * @param resultDecimalPlaces        decimal places of the displayed result
 * @param conversionAccurate         true if |result - amount * rate| &lt;= 0.01
 * @param decimalPrecisionMaintained true if the result shows two or more decimals
 * @param resultUpdatedOnChange      true if the result changed when the input changed
 * @param conversionComplete         true only if all the checks above hold
 */
public record ConversionResult(
        double inputAmount,
        String sourceCurrency,
        String targetCurrency,
        double conversionResult,
        int inputDecimalPlaces,
        int resultDecimalPlaces,
        boolean conversionAccurate,
        boolean decimalPrecisionMaintained,
        boolean resultUpdatedOnChange,
        boolean conversionComplete) {
}
