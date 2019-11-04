# Created by oleg at 01.11.19
Feature: Competition create

  Scenario: Test competition creation

    Given User with email: test and password: top_secure, superuser: True, staff: True .
    When User creates competition with valid data
    Then Competition is successfully created
    And Games are created for competition

    When User creates competition with invalid data
    Then Competition is not created
