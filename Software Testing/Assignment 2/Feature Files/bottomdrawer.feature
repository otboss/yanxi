Feature: Touch feature

	Scenario: As a valid user I can touch my app
		When I press "Dashboard"
			Then I wait for 5 seconds
			Then I see "Dashboard"
			Then I wait for 5 seconds
		When I press "Discover"
			Then I wait for 5 seconds
			Then I see "Discover"
			Then I wait for 5 seconds
		When I press "Notifications"
			Then I wait for 5 seconds
			Then I see "Notifications"
			Then I wait for 5 seconds
		When I press "My Account"
			Then I wait for 5 seconds
			Then I see "My Account"
			Then I wait for 5 seconds
		When I press "Home"
			Then I wait for 5 seconds
			Then I see "Home"
