# Created by oleg at 29.10.19
Feature: Register

  Scenario: Registration user
	When I entered a valid user data
	Then I got success status code

	When I entered invalid user data
	Then I am got fail status code
