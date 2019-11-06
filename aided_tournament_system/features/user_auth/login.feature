# Created by oleg at 29.10.19
Feature: Login

  Scenario: Login user

    Given Existing user
    When User login existing user
    Then User get token of this user
    And Status code is 200

    When User login not existing user
    Then User get error message
