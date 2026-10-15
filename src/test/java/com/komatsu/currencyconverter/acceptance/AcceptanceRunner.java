package com.komatsu.currencyconverter.acceptance;

import io.cucumber.testng.AbstractTestNGCucumberTests;
import io.cucumber.testng.CucumberOptions;

/** Cucumber entry point executed by the {@code acceptance} profile. */
@CucumberOptions(
        features = "src/test/resources/features",
        glue = "com.komatsu.currencyconverter.acceptance",
        plugin = {"pretty", "html:target/cucumber-report.html"})
public class AcceptanceRunner extends AbstractTestNGCucumberTests {
}
