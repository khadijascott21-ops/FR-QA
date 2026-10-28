Feature: Currency conversion
  As a user I want to convert an amount between currencies and see an accurate result

  Background:
    Given the currency converter is open

  @TC-01 @positive @R3 @R4 @R5 @R6 @R7 @R8 @R9 @R10 @R11 @R12 @R13 @R14 @R15 @R16 @R17 @R18 @R19 @R20 @R21 @R22
  Scenario: Convert USD to EUR and collect a complete assessment
    When I enter amount "100"
    And I select source currency "USD" and target currency "EUR"
    Then the result container should become visible
    And the displayed result should be "86.26" with exchange rate "0.862623"
    When I assess the current conversion
    Then the assessment should record amount 100 from "USD" to "EUR" with result 86.26
    And the assessment should record 2 input decimal places and 2 result decimal places
    And the assessment flags should be accuracy true, precision true, update true and completion true
    And the displayed conversion should be within 0.01 of the entered amount times the displayed rate
    And the result should have at least 2 decimal places

  @TC-02 @boundary @R1
  Scenario: Reject zero and hide the previous valid result
    When I enter amount "100"
    And I select source currency "USD" and target currency "EUR"
    Then the result container should become visible
    When I enter amount "0"
    Then the validation message should contain "Amount must be greater than zero"
    And the result container should be hidden
    When I validate amount 0 with source "USD" and target "EUR"
    Then validation should throw IllegalArgumentException containing "amount must be greater than zero"

  @TC-03 @negative @R1
  Scenario Outline: Reject negative amounts
    When I select source currency "USD" and target currency "EUR"
    And I enter amount "<amount>"
    Then the validation message should contain "Amount must be greater than zero"
    And the result container should be hidden
    When I validate amount <amount> with source "USD" and target "EUR"
    Then validation should throw IllegalArgumentException containing "amount must be greater than zero"

    Examples:
      | amount |
      | -100.0 |
      | -0.01  |

  @TC-04 @negative @R2
  Scenario: Currency dropdowns prevent invalid or empty selections
    Then the selected currencies should be "USD" and "EUR"
    When I enter amount "100"
    And I try typing an invalid code and clearing each currency dropdown
    Then the selected currencies should be "USD" and "EUR"
    And neither currency dropdown should offer a blank option

  # Null and empty codes cannot be selected in the GUI; exercise the supplied validator.
  @TC-04 @negative @code-level @R2
  Scenario Outline: Reject missing currency codes before conversion
    When I validate amount 100 with source "<source>" and target "<target>"
    Then validation should throw IllegalArgumentException containing "currency codes must not be null or empty"

    Examples:
      | source  | target  |
      | <null>  | EUR     |
      | <empty> | EUR     |
      | USD     | <null>  |
      | USD     | <empty> |
      | <null>  | <null>  |
      | <empty> | <empty> |
      | <null>  | <empty> |
      | <empty> | <null>  |

  @TC-05 @positive @R3 @R4 @R5
  Scenario Outline: Select every supported currency in either dropdown
    When I enter amount "100"
    And I select source currency "<currency>" and target currency "EUR"
    Then the selected currencies should be "<currency>" and "EUR"
    And the amount field should contain "100"
    When I select source currency "USD" and target currency "<currency>"
    Then the selected currencies should be "USD" and "<currency>"
    And the amount field should contain "100"

    Examples:
      | currency |
      | USD      |
      | EUR      |
      | GBP      |
      | JPY      |
      | CAD      |
      | AUD      |
      | CHF      |

  @TC-06 @edge @R3 @R4 @R5 @R7 @R10 @R11
  Scenario: Convert to the same currency
    When I enter amount "100"
    And I select source currency "USD" and target currency "USD"
    Then the result container should become visible
    And the displayed result should be "100.00" with exchange rate "1.000000"
    And the displayed conversion should be within 0.01 of the entered amount times the displayed rate
    And the result should have at least 2 decimal places

  @TC-07 @positive @R7 @R10 @R11
  Scenario Outline: Convert currencies with very different rates
    When I enter amount "1000"
    And I select source currency "<source>" and target currency "<target>"
    Then the result container should become visible
    And the displayed result should be "<result>" with exchange rate "<rate>"
    And the displayed conversion should be within 0.01 of the entered amount times the displayed rate
    And the result should have at least 2 decimal places

    Examples:
      | source | target | result    | rate       |
      | JPY    | GBP    | 4.71      | 0.004707   |
      | GBP    | JPY    | 212440.76 | 212.440758 |

  @TC-08 @boundary @R3 @R8 @R9 @R11 @R13 @R16 @R17 @R18 @R20
  Scenario Outline: Display two decimal places while preserving the entered amount
    When I enter amount "<amount>"
    And I select source currency "USD" and target currency "USD"
    Then the result container should become visible
    And the displayed result should be "<result>" with exchange rate "1.000000"
    And the amount field should contain "<amount>"
    When I assess the current conversion
    Then the formatted input should be "<result>" with 2 decimal places
    And the assessment should record amount <amount> from "USD" to "USD" with result <result>
    And the assessment should record 2 input decimal places and 2 result decimal places
    And the assessment flags should be accuracy true, precision true, update true and completion true
    And the amount field should contain "<amount>"

    Examples:
      | amount | result |
      | 100.0  | 100.00 |
      | 12.3   | 12.30  |
      | 1.234  | 1.23   |
      | 1.236  | 1.24   |

  @TC-09 @boundary @R1 @R3 @R10 @R11
  Scenario: Accept a small positive amount
    When I enter amount "0.01"
    And I select source currency "USD" and target currency "USD"
    Then the result container should become visible
    And the displayed result should be "0.01" with exchange rate "1.000000"
    And the displayed conversion should be within 0.01 of the entered amount times the displayed rate
    And the result should have at least 2 decimal places
    When I assess the current conversion
    Then the assessment flags should be accuracy true, precision true, update true and completion true

  @TC-10 @edge @R3 @R7 @R10 @R11
  Scenario: Display a large amount without truncation
    When I enter amount "1000000"
    And I select source currency "USD" and target currency "USD"
    Then the result container should become visible
    And the displayed result should be "1000000.00" with exchange rate "1.000000"
    And the displayed conversion should be within 0.01 of the entered amount times the displayed rate
    And the result should have at least 2 decimal places

  @TC-11 @positive @R12 @R21 @R22
  Scenario: Update the result and restore the original amount
    When I enter amount "100"
    And I select source currency "USD" and target currency "EUR"
    Then the result container should become visible
    When I remember the current conversion
    And I change the amount to "200"
    Then the result container should become visible
    And the displayed result should be "172.52" with exchange rate "0.862623"
    And the displayed result should differ from the remembered result
    When I restore the original amount
    Then the amount field should have numeric value 100
    And the selected currencies should be "USD" and "EUR"
    And the displayed result should be "86.26" with exchange rate "0.862623"
    And the displayed result should match the remembered result
    When I assess the current conversion
    Then the assessment flags should be accuracy true, precision true, update true and completion true
    And the amount field should have numeric value 100
    And the displayed result should match the remembered result

  @TC-12 @positive @R3 @R4 @R5 @R6 @R7 @R10 @R11 @R13 @R14 @R15 @R16
  Scenario: Replace the previous conversion after changing the amount and currency
    When I enter amount "100"
    And I select source currency "USD" and target currency "EUR"
    Then the result container should become visible
    And the displayed result should be "86.26" with exchange rate "0.862623"
    When I enter amount "250.75"
    And I select source currency "USD" and target currency "GBP"
    Then the result container should become visible
    And the amount field should contain "250.75"
    And the selected currencies should be "USD" and "GBP"
    And the displayed result should be "187.97" with exchange rate "0.749624"
    And the displayed conversion should be within 0.01 of the entered amount times the displayed rate
    And the result should have at least 2 decimal places
    When I assess the current conversion
    Then the assessment should record amount 250.75 from "USD" to "GBP" with result 187.97
    And the assessment flags should be accuracy true, precision true, update true and completion true

  # Observation: the six-decimal displayed rate loses precision for this amount.
  @TC-13 @edge @known-limitation @R7 @R10 @R19 @R22
  Scenario: Report an accuracy failure for a large cross-currency conversion
    When I enter amount "1000000.0"
    And I select source currency "JPY" and target currency "GBP"
    Then the result container should become visible
    And the displayed result should be "4707.19" with exchange rate "0.004707"
    And the displayed conversion should exceed the 0.01 accuracy tolerance
    When I assess the current conversion
    Then the assessment should record amount 1000000 from "JPY" to "GBP" with result 4707.19
    And the assessment flags should be accuracy false, precision true, update true and completion false
    And the amount field should contain "1000000.0"

  # Observation: both positive amounts round to the same visible result.
  @TC-14 @edge @known-limitation @R12 @R21 @R22
  Scenario: Report no visible update for sub-cent amounts and restore the input
    When I enter amount "0.001"
    And I select source currency "USD" and target currency "USD"
    Then the result container should become visible
    When I remember the current conversion
    And I change the amount to "0.002"
    Then the result container should become visible
    And the displayed result should be "0.00" with exchange rate "1.000000"
    And the displayed result should match the remembered result
    When I restore the original amount
    Then the amount field should contain "0.001"
    And the displayed result should match the remembered result
    When I assess the current conversion
    Then the assessment should record amount 0.001 from "USD" to "USD" with result 0.00
    And the assessment flags should be accuracy true, precision true, update false and completion false
    And the amount field should contain "0.001"
    And the displayed result should match the remembered result
