__author__ = 'BJ'

from behave import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions


@given('I am browsing "{url}"')
def step_impl(context, url):
    context.driver.get(url)
    try:
        WebDriverWait(context.driver, 10).until(expected_conditions.title_contains("Wikipedia"))
    except TimeoutException:
        print("The %s page failed to load! FAIL" % url)
        context.failed = True


@given('The scenario has passed so far')
def step_impl(context):
    assert context.failed is False


@when('I search for "{search_criteria}"')
def step_impl(context, search_criteria):
    inputer_element = context.driver.find_element_by_name("search")
    inputer_element.send_keys(search_criteria)


@when('I select language "{language}"')
def step_impl(context, language):
    select = Select(context.driver.find_element_by_name('language'))
    select.select_by_visible_text(language)


@when('Click the search button')
def step_impl(context):
    context.driver.find_element_by_name("go").click()


@when('I select language_option "{language}"')
def step_impl(context, language):
    context.driver.find_element_by_xpath("//div[@id='p-lang']").find_element_by_partial_link_text(language).click()


@then('The first heading of the search results page matches "{search_topic}"')
def step_impl(context, search_topic):
    assert search_topic.lower() in context.driver.find_element_by_xpath("/html/body//h1").text.lower()
    assert context.failed is False


@then('The search results page is available in "{language}"')
def step_impl(context, language):
    context.driver.find_element_by_xpath("//div[@id='p-lang']")\
        .find_element_by_partial_link_text(language)
    assert context.failed is False
