require 'watir'
require 'webdrivers'
require 'faker'

# Initalize the Browser
chromedriver_path = File.join(File.absolute_path('./', File.dirname(__FILE__)),"chromedriver")
Selenium::WebDriver::Chrome::Service.driver_path = chromedriver_path
browser = Watir::Browser.new :chrome


serviceURL = "http://127.0.0.1:5000/";
username = "";
browser.goto serviceURL+'todo/api/v1.0/tasks/?username='+username+'&password=password';
sleep(4);

