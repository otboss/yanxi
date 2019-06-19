Feature: Start the App

	Scenario: When you start the app you should see version info
		Then I wait for 5 seconds
		Then I take a screenshot
		Then I see "Software version update"
		Then I see "Later"
		When I press "Later"
		Then I don't see "Later"
		Then I take a screenshot
