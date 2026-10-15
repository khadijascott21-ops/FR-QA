package com.komatsu.currencyconverter.acceptance;

import com.komatsu.currencyconverter.model.ConversionResult;

/**
 * Runs the end-to-end conversion check through the GUI and builds a {@link ConversionResult}.
 */
public class ConversionAssessor {

    private static final double TOLERANCE = 0.01;

    private final ConverterDriver driver;

    /**
     * Creates an assessor.
     *
     * @param driver GUI driver
     */
    public ConversionAssessor(ConverterDriver driver) {
        this.driver = driver;
    }

    /**
     * Validates inputs.
     *
     * @param amount amount, must be greater than zero
     * @param source source code, must not be null/empty
     * @param target target code, must not be null/empty
     * @throws IllegalArgumentException if any input is invalid
     */
    public static void validate(double amount, String source, String target) {
        if (amount <= 0) {
            throw new IllegalArgumentException("amount must be greater than zero");
        }
        if (source == null || source.isEmpty() || target == null || target.isEmpty()) {
            throw new IllegalArgumentException("currency codes must not be null or empty");
        }
    }

    /**
     * Counts digits after the decimal point.
     *
     * @param number numeric text
     * @return number of decimal places
     */
    public static int countDecimalPlaces(String number) {
        int dot = number.indexOf('.');
        return dot < 0 ? 0 : number.length() - dot - 1;
    }

    /**
     * Performs a conversion through the GUI and evaluates every acceptance condition.
     *
     * @param amount amount to convert
     * @param source source currency code
     * @param target target currency code
     * @return fully populated result
     */
    public ConversionResult assess(double amount, String source, String target) {
        validate(amount, source, target);
        String formattedInput = String.format("%.2f", amount);

        driver.enterAmount(String.valueOf(amount));
        driver.selectSource(source);
        driver.selectTarget(target);
        boolean visible = driver.waitForResult();

        String resultText = driver.window().getConvertedAmountText();
        double rate = Double.parseDouble(driver.window().getExchangeRateText());
        double result = Double.parseDouble(resultText);

        int inputDecimals = countDecimalPlaces(formattedInput);
        int resultDecimals = countDecimalPlaces(resultText);
        boolean accurate = Math.abs(result - amount * rate) <= TOLERANCE;
        boolean precise = resultDecimals >= 2;
        boolean updated = verifyDynamicUpdate(amount, resultText);

        boolean complete = visible && accurate && precise && updated;
        return new ConversionResult(amount, source, target, result, inputDecimals, resultDecimals,
                accurate, precise, updated, complete);
    }

    /**
     * Changes the amount, checks the result changed, then restores the original amount.
     *
     * @param amount     original amount
     * @param beforeText result text before the change
     * @return true if the result changed and the original state was restored
     */
    public boolean verifyDynamicUpdate(double amount, String beforeText) {
        driver.enterAmount(String.valueOf(amount * 2));
        driver.waitForResult();
        String changedText = driver.window().getConvertedAmountText();
        driver.enterAmount(String.valueOf(amount));
        driver.waitForResult();
        String restoredText = driver.window().getConvertedAmountText();
        return !changedText.equals(beforeText) && restoredText.equals(beforeText);
    }
}
