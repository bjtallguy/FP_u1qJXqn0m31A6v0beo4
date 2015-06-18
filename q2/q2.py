__author__ = '30070_VS'

"""
Q2 Web Front-End Test
Automate the following functional test using Selenium:
1. .
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
# from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions

# Test Data
start_page = "http://www.wikipedia.org/"
search_field_name = "search"
search_string = "London"
search_lang = "Deutsch"

# Create a new instance of the Firefox driver.
driver = webdriver.Firefox()

# Navigate to the Wikipedia home page, http://www.wikipedia.org/.
driver.get(start_page)

# the page is ajaxy so the title is originally this:
print(driver.title)

# 2. Search for a given string in English:
# (a) Type in a string given as parameter in the search input field.
inputElement = driver.find_element_by_name(search_field_name)
# type in the search
inputElement.send_keys(search_string)
# (b) Select English as the search language.
select = Select(driver.find_element_by_name('language'))
select.select_by_visible_text("English")

# submit the form (although google automatically searches now without submitting)
driver.find_element_by_name("go").click()

try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(expected_conditions.title_contains(search_string))

    print(driver.title)

finally:
    driver.quit()
