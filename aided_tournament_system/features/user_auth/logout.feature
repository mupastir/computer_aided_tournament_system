# Created by oleg at 30.10.19
Feature: Logout


  Scenario: Logout user
    Given Logged in user
    When Try to logout user
    Then I get successfully logout
    And Status code is 200
