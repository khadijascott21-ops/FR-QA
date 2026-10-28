package com.komatsu.currencyconverter.acceptance;

import com.komatsu.currencyconverter.model.ConversionResult;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

import static org.testng.Assert.*;

/** Steps that perform conversions and verify the displayed result. */
public class ConversionSteps {

    private final ScenarioContext context;

    /**
     * Creates the steps.
     *
     * @param context shared scenario state
     */
    public ConversionSteps(ScenarioContext context) {
        this.context = context;
    }

    @Then("the result container should become visible")
    public void waitForResult() {
        assertTrue(context.driver.waitForResult(), "The conversion result should become visible");
    }

    @Then("the displayed result should be {string} with exchange rate {string}")
    public void verifyDisplayedResult(String result, String rate) {
        assertTrue(context.driver.window().isResultVisible(), "The displayed result should be visible");
        assertEquals(context.driver.window().getConvertedAmountText(), result, "Displayed converted amount");
        assertEquals(context.driver.window().getExchangeRateText(), rate, "Displayed exchange rate");
    }

    @When("I assess the current conversion")
    public void assessConversion() {
        String originalAmount = context.driver.window().getAmountText();
        context.amount = Double.parseDouble(originalAmount);
        String source = context.driver.window().getSourceCode();
        String target = context.driver.window().getTargetCode();
        context.conversionResult = context.assessor.assess(context.amount, source, target);
        assertEquals(Double.parseDouble(context.driver.window().getAmountText()), context.amount, 1e-12,
                "The assessor should restore the original amount after checking the dynamic update");
        context.driver.enterAmount(originalAmount);
        assertTrue(context.driver.waitForResult(), "The restored conversion should remain visible");
    }

    @Then("the assessment should record amount {double} from {string} to {string} with result {double}")
    public void verifyAssessmentValues(double amount, String source, String target, double result) {
        ConversionResult assessment = assessment();
        assertEquals(assessment.inputAmount(), amount, 1e-12, "Assessment inputAmount");
        assertEquals(assessment.sourceCurrency(), source, "Assessment sourceCurrency");
        assertEquals(assessment.targetCurrency(), target, "Assessment targetCurrency");
        assertEquals(assessment.conversionResult(), result, 1e-9, "Assessment conversionResult");
        assertEquals(assessment.conversionResult(),
                Double.parseDouble(context.driver.window().getConvertedAmountText()), 1e-9,
                "Assessment result should match the restored GUI result");
    }

    @Then("the assessment should record {int} input decimal places and {int} result decimal places")
    public void verifyDecimalCounts(int inputDecimals, int resultDecimals) {
        assertEquals(assessment().inputDecimalPlaces(), inputDecimals, "Assessment inputDecimalPlaces");
        assertEquals(assessment().resultDecimalPlaces(), resultDecimals, "Assessment resultDecimalPlaces");
    }

    @Then("the assessment flags should be accuracy {word}, precision {word}, update {word} and completion {word}")
    public void verifyAssessmentFlags(String accurate, String precise, String updated, String complete) {
        ConversionResult assessment = assessment();
        assertEquals(Boolean.toString(assessment.conversionAccurate()), accurate, "Assessment conversionAccurate");
        assertEquals(Boolean.toString(assessment.decimalPrecisionMaintained()), precise,
                "Assessment decimalPrecisionMaintained");
        assertEquals(Boolean.toString(assessment.resultUpdatedOnChange()), updated, "Assessment resultUpdatedOnChange");
        assertEquals(Boolean.toString(assessment.conversionComplete()), complete, "Assessment conversionComplete");
    }

    @Then("the formatted input should be {string} with {int} decimal places")
    public void verifyFormattedInput(String expected, int decimals) {
        String formatted = String.format("%.2f", context.amount);
        assertEquals(formatted, expected, "Input formatted using String.format to two decimal places");
        assertEquals(ConversionAssessor.countDecimalPlaces(formatted), decimals, "Formatted input decimal count");
        assertEquals(assessment().inputDecimalPlaces(), decimals, "Assessment formatted input decimal count");
    }

    @Then("the displayed conversion should be within 0.01 of the entered amount times the displayed rate")
    public void verifyAccuracy() {
        double error = accuracyError();
        assertTrue(error <= 0.01, "Conversion error should be <= 0.01 but was " + error);
    }

    @Then("the displayed conversion should exceed the 0.01 accuracy tolerance")
    public void verifyAccuracyLimitation() {
        double error = accuracyError();
        assertTrue(error > 0.01, "Expected the documented displayed-rate accuracy limitation; error was " + error);
    }

    @Then("the result should have at least {int} decimal places")
    public void verifyResultPrecision(int minimum) {
        String text = context.driver.window().getConvertedAmountText();
        assertTrue(ConversionAssessor.countDecimalPlaces(text) >= minimum,
                "Result '" + text + "' should show at least " + minimum + " decimal places");
    }

    @When("I remember the current conversion")
    public void rememberConversion() {
        assertTrue(context.driver.waitForResult(), "A result should be visible before the amount changes");
        context.amount = Double.parseDouble(context.driver.window().getAmountText());
        context.originalResultText = context.driver.window().getConvertedAmountText();
    }

    @When("I change the amount to {string}")
    public void changeAmount(String amount) {
        context.driver.enterAmount(amount);
    }

    @When("I restore the original amount")
    public void restoreAmount() {
        assertNotNull(context.originalResultText, "Remember the original conversion before restoring it");
        context.driver.enterAmount(String.valueOf(context.amount));
        assertTrue(context.driver.waitForResult(), "The restored result should become visible");
    }

    @Then("the displayed result should differ from the remembered result")
    public void verifyResultChanged() {
        assertNotNull(context.originalResultText, "Remember the original conversion before comparing results");
        assertNotEquals(context.driver.window().getConvertedAmountText(), context.originalResultText,
                "Changing the amount should change the displayed result");
    }

    @Then("the displayed result should match the remembered result")
    public void verifyResultUnchanged() {
        assertNotNull(context.originalResultText, "Remember the original conversion before comparing results");
        assertEquals(context.driver.window().getConvertedAmountText(), context.originalResultText,
                "The displayed result should match the remembered value");
    }

    private ConversionResult assessment() {
        assertNotNull(context.conversionResult, "Assess the current conversion before checking its fields");
        return context.conversionResult;
    }

    private double accuracyError() {
        double amount = Double.parseDouble(context.driver.window().getAmountText());
        double rate = Double.parseDouble(context.driver.window().getExchangeRateText());
        double result = Double.parseDouble(context.driver.window().getConvertedAmountText());
        return Math.abs(result - amount * rate);
    }
}
