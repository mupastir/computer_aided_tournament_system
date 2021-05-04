# Created by oleg at 05.11.19
Feature: Look participant
  Check if urls to look details about participants works properly

  Scenario: Check details about participants
    Given User with email: test and password: top_secure, superuser: True, staff: True.

    And Team with players
    |first_name|last_name|username      |email        |password   |beach_rating|
    |Masha     |Test     |test1         |test@test.com|top_secure1|5           |
    |Misha     |Test     |test2         |test@test.com|top_secure2|12          |

    And Referee with First name: Sergey, Last name: Pupkin, username: pupkin, email: test@test.com, password: top_secure3.

    When User check list of teams
    Then Get teams info correct
    Then Status code is 200

    When User check list of referees
    Then Get referee info correct
    Then Status code is 200

    When User check list of players
    Then Get users info correct
    Then Status code is 200

    When User check list of players for a Team
