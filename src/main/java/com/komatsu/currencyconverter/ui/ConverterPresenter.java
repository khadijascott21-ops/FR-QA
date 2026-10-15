package com.komatsu.currencyconverter.ui;

import com.komatsu.currencyconverter.service.CurrencyConverter;
import java.util.Locale;

/**
 * UI-agnostic logic: turns the raw form inputs into a displayed result.
 */
public class ConverterPresenter {

    private final CurrencyConverter converter;
    private final ConversionView view;
    private String amountText = "";
    private String source;
    private String target;

    /**
     * Creates a presenter.
     *
     * @param converter conversion service
     * @param view      view to update
     */
    public ConverterPresenter(CurrencyConverter converter, ConversionView view) {
        this.converter = converter;
        this.view = view;
    }

    /**
     * Updates the amount text and refreshes the result.
     *
     * @param text raw amount text
     */
    public void onAmountChanged(String text) {
        this.amountText = text == null ? "" : text;
        refresh();
    }

    /**
     * Updates the source currency and refreshes the result.
     *
     * @param code currency code
     */
    public void onSourceChanged(String code) {
        this.source = code;
        refresh();
    }

    /**
     * Updates the target currency and refreshes the result.
     *
     * @param code currency code
     */
    public void onTargetChanged(String code) {
        this.target = code;
        refresh();
    }

    private void refresh() {
        if (amountText.isBlank()) {
            view.hideResult();
            view.showError("");
            return;
        }
        try {
            double amount = Double.parseDouble(amountText.trim());
            double result = converter.convert(amount, source, target);
            double rate = converter.rate(source, target);
            view.showError("");
            view.showResult(String.format(Locale.ROOT, "%.2f", result),
                    String.format(Locale.ROOT, "%.6f", rate));
        } catch (NumberFormatException e) {
            view.hideResult();
            view.showError("Amount must be a number");
        } catch (IllegalArgumentException e) {
            view.hideResult();
            view.showError(e.getMessage());
        }
    }
}
