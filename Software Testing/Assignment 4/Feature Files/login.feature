Feature: Login feature

	Scenario: Username/password
		Then I wait for 5 seconds
		Then I take a screenshot
		When I press view with id "login_button"
		Then I see "Login"
		Then I take a screenshot
		When I enter "username" into input field number 1
		And I enter "123456" into input field number 2
		And I press button number 1
		Then I see "Wrong username/password"
		Then I take a screenshot

		
		
