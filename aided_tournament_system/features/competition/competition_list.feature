# Created by oleg at 01.11.19
Feature: List of competitions
  Check url which shows list of existing competitions

  Scenario: Get competitions list
    Given Existing competitions
    When Send get request on url /competitions/detail/
    Then Get list of one existing competition
