# Created by oleg at 06.11.19
Feature: Protocolize games
  Test of protocolizing games

  Scenario: Game is successfully protocolized by referee
    Given Referee with role scr
    And Final game for competition Base_women_4x4
    |team          |status|
    |gang_of_four  |home  |
    |Pavels_mussels|away  |
    When User protocolized score 2 - 1
    Then Status code is 200

  Scenario: Game is successfully protocolized by admin
    Given User with email: admin@admin.com and password: strong_password, superuser: True, staff: True.

    And Final game for competition Base_women_4x4
    |team          |status|
    |gang_of_four  |home  |
    |Pavels_mussels|away  |
    When User protocolized score 2 - 1
    Then Status code is 200

  Scenario: Game is unsuccessfully protocolized by player
    Given Player
    And Final game for competition Base_women_4x4
    |team          |status|
    |gang_of_four  |home  |
    |Pavels_mussels|away  |
    When User protocolized score 2 - 1
    Then Error user doesn't have permission
