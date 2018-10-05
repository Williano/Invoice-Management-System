### Run Functional test with Selenium

- Download selenium for chrome, firefox and Safari.
 
 
    -- For Firefox:
     https://github.com/mozilla/geckodriver/releases/tag/v0.23.0       
    
    -- For Chrome:
      https://sites.google.com/a/chromium.org/chromedriver/
      
    -- For Safari follow this guide:
        https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari
        https://stackoverflow.com/questions/46103589/usr-bin-safaridriver-for-safari-10-1-2-12603-3-8-on-mac-os-sierra-10-12-6-pro

- Google how to install it for your Operating system.

      
- Install requirements.txt to install selenium for Python.

    
    pip install -r requirements.txt
 
-  Run the functional test with:


    python manage.py test tests.functional 
    
###### Note
If you use Firefox, open the functional test file and comment
the chrome() in the SetUp method and uncomment the Firefox()

Remember to change the username and password to a user in your
database.

Make sure your server is running on port 8000.