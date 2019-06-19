require 'watir'
require 'webdrivers'
require 'faker'

# Initalize the Browser
chromedriver_path = File.join(File.absolute_path('./', File.dirname(__FILE__)),"chromedriver")
Selenium::WebDriver::Chrome::Service.driver_path = chromedriver_path
browser = Watir::Browser.new :chrome

browser.goto 'http://watir.com/examples/forms_with_input_elements.html'

#TIP: USE JAVASCRIPT TO FILL IN FORM
browser.execute_script('');
browser.execute_script('');
browser.execute_script('');

browser.text_field(id: 'new_user_first_name').set Faker::Name.first_name
browser.text_field(id: 'new_user_last_name').set Faker::Name.last_name
email = Faker::Internet.email;
browser.text_field(id: 'new_user_email').set email
browser.text_field(id: 'new_user_email_confirm').set email
browser.text_field(id: 'new_user_occupation').set Faker::Job.title;
browser.execute_script('');

browser.execute_script('');
browser.text_field(id: 'unknown_text_field').set Faker::Code.npi;

#PATH THE FILE TO UPLOAD
filePath = "";

browser.file_field(id: "new_user_portrait").set(filePath);
browser.file_field(id: "new_user_teeth").set(filePath);
browser.file_field(id: "new_user_resume").set(filePath);

browser.execute_script('');

browser.text_field(id: "new_user_username").set("user");
browser.text_field(id: "new_user_password").set("password");

browser.button(id: 'new_user_submit').click