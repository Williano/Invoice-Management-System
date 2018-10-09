# Standard Library imports.
import time

# Third party imports.
from django.test import LiveServerTestCase
from selenium import webdriver


class LoginTest(LiveServerTestCase):

    def setUp(self):
        """
        Create a user to for logging in.

        Instantiate the selenium webdriver and load the browser.
        """
        self.selenium = webdriver.Chrome()
        # self.selenium = webdriver.Firefox()
        # self.selenium = webdriver.Safari()
        self.selenium.maximize_window()
        super(LoginTest, self).setUp()

    def tearDown(self):
        """
        Closes the web browser when called.
        """
        self.selenium.quit()
        super(LoginTest, self).tearDown()

    def test_user_login_is_successful_with_valid_credentials(self):
        """
        Selenium gets the url of the application.

        It then searches for username and password from the login form
         with it's ids.

        It then send the data for the two fields using the send_keys.

        It then looks for the submit button of the login form and clicks
        on it to submit the data.

        After it submits the data to the database,
        it waits for thirty seconds before quitting.

        DjangoLiveServerTestCase provides a live server url attribute
        to access the base url in tests
        """

        self.selenium.get('http://localhost:8000')
        username_input = self.selenium.find_element_by_id("id_username")
        username_input.send_keys('shoemaker')
        password_input = self.selenium.find_element_by_id("id_password")
        password_input.send_keys('B3Pjv224Urjp8TC')
        self.selenium.find_element_by_xpath('//button[@type="submit"]').click()

        # Wait for a minute before quitting.
        time.sleep(5)

    def test_login_credentials_required_for_user_login(self):
        self.selenium.get('http://localhost:8000')
        username_input = self.selenium.find_element_by_id("id_username")
        username_input.send_keys('')
        password_input = self.selenium.find_element_by_id("id_password")
        password_input.send_keys('')
        self.selenium.find_element_by_xpath('//button[@type="submit"]').click()

        # Wait for a minute before quitting.
        time.sleep(5)

    def test_user_login_fails_with_invalid_credentials(self):
        self.selenium.get('http://localhost:8000')
        username_input = self.selenium.find_element_by_id("id_username")
        username_input.send_keys('killmonger')
        password_input = self.selenium.find_element_by_id("id_password")
        password_input.send_keys('erikstevens')
        self.selenium.find_element_by_xpath('//button[@type="submit"]').click()

        # Wait for a minute before quitting.
        time.sleep(5)