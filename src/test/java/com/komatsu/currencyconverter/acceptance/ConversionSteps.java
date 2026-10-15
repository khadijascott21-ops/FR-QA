package com.komatsu.currencyconverter.acceptance;

import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertNotEquals;
import static org.testng.Assert.assertTrue;

import com.komatsu.currencyconverter.model.ConversionResult;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

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

    //Add your step definitions here
}
