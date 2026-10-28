package com.komatsu.currencyconverter.acceptance;

import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertNotNull;
import static org.testng.Assert.assertTrue;

import com.googlecode.lanterna.gui2.ComboBox;
import com.googlecode.lanterna.gui2.Component;
import com.googlecode.lanterna.gui2.Panel;
import com.googlecode.lanterna.input.KeyStroke;
import com.googlecode.lanterna.input.KeyType;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import java.util.ArrayList;
import java.util.List;

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

    @Given("the currency converter is open")
    public void openConverter() {
        if (context.driver == null) {
            context.driver = new ConverterDriver();
            context.assessor = new ConversionAssessor(context.driver);
        }
        assertNotNull(context.driver.window(), "The converter window should be open");
    }

    @When("I enter amount {string}")
    public void enterAmount(String amount) {
        context.amount = Double.parseDouble(amount);
        context.driver.enterAmount(amount);
    }

    @When("I select source currency {string} and target currency {string}")
    public void selectCurrencies(String source, String target) {
        context.driver.selectSource(source);
        context.driver.selectTarget(target);
    }

    @Then("the selected currencies should be {string} and {string}")
    public void verifySelectedCurrencies(String source, String target) {
        assertEquals(context.driver.window().getSourceCode(), source, "Selected source currency");
        assertEquals(context.driver.window().getTargetCode(), target, "Selected target currency");
    }

    @Then("the amount field should contain {string}")
    public void verifyAmountText(String amount) {
        assertEquals(context.driver.window().getAmountText(), amount, "Entered amount text should be preserved");
    }

    @Then("the amount field should have numeric value {double}")
    public void verifyAmountValue(double amount) {
        assertEquals(Double.parseDouble(context.driver.window().getAmountText()), amount, 1e-12,
                "Amount field should be restored to its original value");
    }

    @Then("the validation message should contain {string}")
    public void verifyValidationMessage(String message) {
        String actual = context.driver.window().getErrorText();
        assertTrue(actual.contains(message), "Expected validation message containing '" + message
                + "' but received '" + actual + "'");
    }

    @Then("the result container should be hidden")
    public void verifyResultHidden() {
        assertTrue(!context.driver.window().isResultVisible(), "Invalid input should hide the result container");
    }

    @When("I validate amount {double} with source {string} and target {string}")
    public void validateInputs(double amount, String source, String target) {
        context.thrown = null;
        try {
            ConversionAssessor.validate(amount, decodeMissingCode(source), decodeMissingCode(target));
        } catch (IllegalArgumentException exception) {
            context.thrown = exception;
        }
    }

    @Then("validation should throw IllegalArgumentException containing {string}")
    public void verifyValidationException(String message) {
        assertNotNull(context.thrown, "Invalid input should throw IllegalArgumentException");
        assertTrue(context.thrown instanceof IllegalArgumentException, "Unexpected validation exception type");
        assertTrue(context.thrown.getMessage().contains(message),
                "Unexpected validation exception message: " + context.thrown.getMessage());
    }

    @When("I try typing an invalid code and clearing each currency dropdown")
    public void tryInvalidDropdownInput() {
        for (ComboBox<?> dropdown : currencyDropdowns()) {
            Object selected = dropdown.getSelectedItem();
            dropdown.takeFocus();
            for (char letter : "XXX".toCharArray()) {
                dropdown.handleInput(new KeyStroke(letter, false, false));
            }
            dropdown.handleInput(new KeyStroke(KeyType.Backspace));
            dropdown.handleInput(new KeyStroke(KeyType.Delete));
            assertEquals(dropdown.getSelectedItem(), selected,
                    "Typing and deletion should preserve a valid currency selection");
            assertEquals(dropdown.getText(), selected,
                    "The dropdown should not display an invalid or empty currency code");
        }
    }

    @Then("neither currency dropdown should offer a blank option")
    public void verifyNoBlankCurrencyOptions() {
        for (ComboBox<?> dropdown : currencyDropdowns()) {
            assertTrue(dropdown.getItemCount() > 0, "Currency dropdown should have options");
            for (int index = 0; index < dropdown.getItemCount(); index++) {
                Object option = dropdown.getItem(index);
                assertNotNull(option, "Currency options should not be null");
                assertTrue(!option.toString().isBlank(), "Currency options should not be blank");
            }
        }
    }

    private String decodeMissingCode(String code) {
        return switch (code) {
            case "<null>" -> null;
            case "<empty>" -> "";
            default -> code;
        };
    }

    private List<ComboBox<?>> currencyDropdowns() {
        List<ComboBox<?>> dropdowns = new ArrayList<>();
        collectDropdowns(context.driver.window().getComponent(), dropdowns);
        assertEquals(dropdowns.size(), 2, "The form should have source and target currency dropdowns");
        return dropdowns;
    }

    private void collectDropdowns(Component component, List<ComboBox<?>> dropdowns) {
        if (component instanceof ComboBox<?> dropdown) {
            dropdowns.add(dropdown);
        } else if (component instanceof Panel panel) {
            for (Component child : panel.getChildrenList()) {
                collectDropdowns(child, dropdowns);
            }
        }
    }

}
