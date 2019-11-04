# Created by oleg at 29.10.19
Feature: Login

  Scenario: Login user

    Given Existing user
    When I login existing user
    Then I get token of this user
    And Status code is 200

    When I login not existing user
    Then I get error message
