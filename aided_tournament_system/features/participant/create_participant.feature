# Created by oleg at 05.11.19
Feature: Create participants
  Check if teams, players and referee are created

  Scenario: Create player
    Given User with email: test and password: top_secure, superuser: True, staff: True .
    When User add player role
    Then User got success status code
    And User become a player

  Scenario: Create team
    Given User with email: test and password: top_secure, superuser: True, staff: True .
    When User create BestTeam
    Then User got success status code

  Scenario: Create referee
    Given User with email: test and password: top_secure, superuser: True, staff: True .
    When User add referee role
    Then User got success status code
    And User become a referee

  Scenario: Add players to team
    Given User with email: test@test.com and password: extra_strong, superuser: True, staff: True.
    And Player
    |first_name|last_name|username      |email        |password   |
    |Masha     |Test     |test1         |test@test.com|top_secure1|
    And The TEAM
    When User add TEST_PLAYER to TEAM
    Then User got success status code
    And TEAM has TEST_PLAYER