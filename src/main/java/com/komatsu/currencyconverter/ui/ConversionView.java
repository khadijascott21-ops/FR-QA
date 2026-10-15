package com.komatsu.currencyconverter.ui;

/**
 * Output port the {@link ConverterPresenter} uses to display state; implemented by the Lanterna window.
 */
public interface ConversionView {

    /**
     * Shows a successful conversion.
     *
     * @param convertedAmount converted amount formatted for display
     * @param exchangeRate    exchange rate formatted for display
     */
    void showResult(String convertedAmount, String exchangeRate);

    /** Hides the result container. */
    void hideResult();

    /**
     * Shows a validation message.
     *
     * @param message the message
     */
    void showError(String message);
}
