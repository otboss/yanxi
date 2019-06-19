Feature: Picker feature

	Scenario: Date and Time Picker with Spinner
		When I press view with id "dateButton"
		Given I set the "datePicker" date to "09-09-2019" 
		Then I press "OK"
		When I press view with id "timeButton"
		Given I set the "timePicker" time to "13:00"
		Then I press "OK"
		Then I select "Reddit" from "spinner"
		
		
		
		