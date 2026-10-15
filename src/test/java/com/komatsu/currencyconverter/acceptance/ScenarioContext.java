package com.komatsu.currencyconverter.acceptance;

import com.komatsu.currencyconverter.model.ConversionResult;

/**
 * State shared between the step definition classes of a single scenario.
 */
public class ScenarioContext {

    /** GUI driver, created lazily by the first step. */
    ConverterDriver driver;
    /** Assessor bound to the driver. */
    ConversionAssessor assessor;
    /** Amount used by the scenario. */
    double amount;
    /** Result text before any dynamic change. */
    String originalResultText;
    /** Result collected from a full assessment. */
    ConversionResult conversionResult;
    /** Exception captured during input validation. */
    Throwable thrown;
}
