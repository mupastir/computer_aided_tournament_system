# Created by oleg at 29.10.19
Feature: Register

  Scenario: Registration user
	When User entered a valid user data
	Then User got success status code

	When User entered invalid user data
	Then User am got fail status code
