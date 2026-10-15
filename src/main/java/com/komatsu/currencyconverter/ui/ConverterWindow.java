package com.komatsu.currencyconverter.ui;

import com.googlecode.lanterna.gui2.BasicWindow;
import com.googlecode.lanterna.gui2.Button;
import com.googlecode.lanterna.gui2.ComboBox;
import com.googlecode.lanterna.gui2.GridLayout;
import com.googlecode.lanterna.gui2.Label;
import com.googlecode.lanterna.gui2.Panel;
import com.googlecode.lanterna.gui2.TextBox;
import com.komatsu.currencyconverter.model.Currency;
import com.komatsu.currencyconverter.service.CurrencyConverter;
import java.util.List;

/**
 * Lanterna window hosting the converter form: amount, source and target dropdowns and a result container.
 */
public class ConverterWindow extends BasicWindow implements ConversionView {

    private final TextBox amountField = new TextBox("");
    private final ComboBox<String> sourceCombo = new ComboBox<>(Currency.codes());
    private final ComboBox<String> targetCombo = new ComboBox<>(Currency.codes());
    private final Panel resultContainer = new Panel(new GridLayout(2));
    private final Label convertedAmountLabel = new Label("");
    private final Label rateLabel = new Label("");
    private final Label errorLabel = new Label("");
    private final ConverterPresenter presenter;

    /**
     * Builds the window and wires it to a new presenter.
     *
     * @param converter conversion service
     */
    public ConverterWindow(CurrencyConverter converter) {
        super("Currency Converter");
        this.presenter = new ConverterPresenter(converter, this);
        setHints(List.of(Hint.CENTERED));

        Panel form = new Panel(new GridLayout(2));
        form.addComponent(new Label("Amount:"));
        form.addComponent(amountField);
        form.addComponent(new Label("From:"));
        form.addComponent(sourceCombo);
        form.addComponent(new Label("To:"));
        form.addComponent(targetCombo);

        resultContainer.addComponent(new Label("Converted amount:"));
        resultContainer.addComponent(convertedAmountLabel);
        resultContainer.addComponent(new Label("Exchange rate:"));
        resultContainer.addComponent(rateLabel);
        resultContainer.setVisible(false);

        Panel root = new Panel();
        root.addComponent(form);
        root.addComponent(errorLabel);
        root.addComponent(resultContainer);
        root.addComponent(new Button("Quit", this::close));
        setComponent(root);

        amountField.setTextChangeListener((text, byUser) -> presenter.onAmountChanged(text));
        sourceCombo.addListener((sel, prev, byUser) -> presenter.onSourceChanged(sourceCombo.getSelectedItem()));
        targetCombo.addListener((sel, prev, byUser) -> presenter.onTargetChanged(targetCombo.getSelectedItem()));

        sourceCombo.setSelectedItem(Currency.USD.name());
        targetCombo.setSelectedItem(Currency.EUR.name());
        presenter.onSourceChanged(sourceCombo.getSelectedItem());
        presenter.onTargetChanged(targetCombo.getSelectedItem());
    }

    /**
     * Enters text in the amount field.
     *
     * @param text the text
     */
    public void setAmount(String text) {
        amountField.setText(text);
    }

    /**
     * Selects the source currency.
     *
     * @param code currency code
     */
    public void selectSource(String code) {
        sourceCombo.setSelectedItem(code);
    }

    /**
     * Selects the target currency.
     *
     * @param code currency code
     */
    public void selectTarget(String code) {
        targetCombo.setSelectedItem(code);
    }

    /**
     * Returns the text currently in the amount field.
     *
     * @return amount text
     */
    public String getAmountText() {
        return amountField.getText();
    }

    /**
     * Returns the selected source currency.
     *
     * @return currency code
     */
    public String getSourceCode() {
        return sourceCombo.getSelectedItem();
    }

    /**
     * Returns the selected target currency.
     *
     * @return currency code
     */
    public String getTargetCode() {
        return targetCombo.getSelectedItem();
    }

    /**
     * Tells whether the result container is visible.
     *
     * @return true if visible
     */
    public boolean isResultVisible() {
        return resultContainer.isVisible();
    }

    /**
     * Returns the displayed converted amount.
     *
     * @return converted amount text
     */
    public String getConvertedAmountText() {
        return convertedAmountLabel.getText();
    }

    /**
     * Returns the displayed exchange rate.
     *
     * @return exchange rate text
     */
    public String getExchangeRateText() {
        return rateLabel.getText();
    }

    /**
     * Returns the displayed validation message.
     *
     * @return message text (empty if none)
     */
    public String getErrorText() {
        return errorLabel.getText();
    }

    @Override
    public void showResult(String convertedAmount, String exchangeRate) {
        convertedAmountLabel.setText(convertedAmount);
        rateLabel.setText(exchangeRate);
        resultContainer.setVisible(true);
    }

    @Override
    public void hideResult() {
        resultContainer.setVisible(false);
    }

    @Override
    public void showError(String message) {
        errorLabel.setText(message);
    }
}
