# Created by oleg at 05.11.19
Feature: Create participants
  Check if teams, players and referee are created

  Scenario: Create player
    Given User with email: test and password: top_secure, superuser: True, staff: True .
    When User add player role
    Then User got success status code
    And User become a player

  Scenario: Create referee
    Given User with email: test and password: top_secure, superuser: True, staff: True .
    When User add referee role
    Then User got success status code
    And User become a referee

  Scenario: Create team
    Given User with email: test and password: top_secure, superuser: True, staff: True .
    When User create BestTeam
    Then User got success status code

  Scenario: Add user to team
    Given User with email: test@test.com and password: extra_strong, superuser: True, staff: True.
    And Player is user
    And The TEAM
    When User try to join to TEAM
    Then Status code is 200
    And TEAM has TEST_PLAYER
