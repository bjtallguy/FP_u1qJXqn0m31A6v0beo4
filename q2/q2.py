__author__ = 'bj'

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
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions

# Test Data
start_page = "http://www.wikipedia.org/"
search_field_name = "search"
search_string = "London"
search_lang = "Deutsch"
# search_lang = "wiggle"

# Create a new instance of the Firefox driver.
driver = webdriver.Firefox()

try:
    # 1. Navigate to the Wikipedia home page, http://www.wikipedia.org/.
    driver.get(start_page)
    try:
        element = WebDriverWait(driver, 10).until(expected_conditions.title_contains("Wikipedia"))
    except:
        print("The %s page failed to load! FAIL" % start_page)
        raise


    # 2. Search for a given string in English:
    # (a) Type in a string given as parameter in the search input field.
    inputElement = driver.find_element_by_name(search_field_name)
    # type in the search
    inputElement.send_keys(search_string)
    # (b) Select English as the search language.
    select = Select(driver.find_element_by_name('language'))
    select.select_by_visible_text("English")
    # (c) Click the search button.
    driver.find_element_by_name("go").click()

    # 3. Validate that the first heading of the search results page matches the search string (ignoring case).
    if search_string.lower() not in driver.find_element_by_xpath("/html/body//h1").text.lower():
        raise AssertionError("Search string (%s) not found in first header" % search_string)

    # 4. Verify that the search results page is available in a language given as parameter.
    try:
        new_lang_page = driver.find_element_by_xpath("//div[@id='p-lang']").find_element_by_partial_link_text(search_lang)
    except NoSuchElementException:
        print("Page not available in %s. FAIL" % search_lang)
        raise
    else:
        print("Page is available in %s. PASS" % search_lang)

    # 5. Navigate to the search results page in that language.
    new_lang_page.click()

    # 6. Validate that the search results page in the new language includes a link to the version in English
    en_lang = "English"
    try:
        new_lang_page = driver.find_element_by_xpath("//div[@id='p-lang']").find_element_by_partial_link_text(en_lang)
    except NoSuchElementException:
        print("Page not available in %s. FAIL" % en_lang)
        raise
    else:
        print("Page is available in %s. PASS" % en_lang)

finally:
    driver.quit()
