package com.komatsu.currencyconverter.acceptance;

import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertNotNull;
import static org.testng.Assert.assertTrue;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

/** Steps that operate the form: validation, amount entry, dropdown selection. */
public class InputSteps {

    private final ScenarioContext context;

    /**
     * Creates the steps.
     *
     * @param context shared scenario state
     */
    public InputSteps(ScenarioContext context) {
        this.context = context;
    }

    // Add your step definitions here

}
