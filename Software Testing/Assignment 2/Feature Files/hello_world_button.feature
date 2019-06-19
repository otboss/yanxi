Feature: Touch feature

	Scenario: As a valid user I can touch my app
		When I press "Button"
			Then I see "Hello World"
			Then I wait for 5 seconds
