package com.komatsu.currencyconverter.acceptance;

import io.cucumber.java.After;
import io.cucumber.java.Before;
import java.util.Locale;

/** Scenario lifecycle hooks. */
public class Hooks {

    private final ScenarioContext context;

    /**
     * Creates the hooks.
     *
     * @param context shared scenario state
     */
    public Hooks(ScenarioContext context) {
        this.context = context;
    }

    /** Fixes the locale so formatting is deterministic. */
    @Before
    public void fixLocale() {
        Locale.setDefault(Locale.US);
    }

    /** Releases the GUI after each scenario. */
    @After
    public void closeGui() {
        if (context.driver != null) {
            context.driver.close();
        }
    }
}
