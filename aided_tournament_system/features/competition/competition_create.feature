# Created by oleg at 01.11.19
Feature: Competition create

  Scenario: Test competition creation

    Given Admin user
    And Logged in admin
    When I create competition with valid data
    Then Competition is successfully created
    And Games are created for competition

    When I create competition with invalid data
    Then Competition is not created
