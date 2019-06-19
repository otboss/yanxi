For Assignm




2-5, take the apk file and feature file and run each exercise to obtain the results. Please note that all of the points were not done, only minimum 50% of them

For exercises 6-9, install the gems that are listed in the slides (gem install bundle will not work) then run the files using the commands from the slides. Good luck explaining Cucumber/Gherkin/Ruby/Selenium for the extra 25% to make up the 50%

For exercise 9 webtest, go to features/step_definitions/search_steps.rb, open the file in a text editor and change 

------------------------------------------
driver = Selenium::WebDriver.for :firefox

to 

driver = Selenium::WebDriver.for :chrome
------------------------------------------

This will change the browser that the tests are ran in. Also remember to install the webdrivers for the respective browsers (excluding Safari that doesn't require this).


