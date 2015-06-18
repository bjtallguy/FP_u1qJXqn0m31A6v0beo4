__author__ = '30070_VS'

"""
Q2 Web Front-End Test
Automate the following functional test using Selenium:
1. Navigate to the Wikipedia home page, http://www.wikipedia.org/.
2. Search for a given string in English:
(a) Type in a string given as parameter in the search input field.
(b) Select English as the search language.
(c) Click the search button.
3. Validate that the first heading of the search results page matches the
search string (ignoring case).
4. Verify that the search results page is available in a language given as
parameter.
5. Navigate to the search results page in that language.
6. Validate that the search results page in the new language includes a
link to the version in English.
"""

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# go to the google home page
driver.get("http://www.google.com")

# the page is ajaxy so the title is originally this:
print(driver.title)

# find the element that's name attribute is q (the google search box)
inputElement = driver.find_element_by_name("q")

# type in the search
inputElement.send_keys("cheese!")

# submit the form (although google automatically searches now without submitting)
inputElement.submit()

try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

    # You should see "cheese! - Google Search"
    print(driver.title)

finally:
    driver.quit()
