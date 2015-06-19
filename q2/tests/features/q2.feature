# Created by BJ at 19/06/2015

Feature: Q2 Web Front-End Test
  Automate the following functional test using Selenium
  Denonstrating Gherkin BDD is just a bonus

  Scenario Outline: Search for a given string in English and check it in another Language
     Given I am browsing "http://www.wikipedia.org/"
      When I search for "<search_topic>"
       And I select language "English"
       And Click the search button
      Then The first heading of the search results page matches "<search_topic>"
       And The search results page is available in "<language>"

    Given The scenario has passed so far
      When I select language_option "<language>"
      Then The search results page is available in "English"

   Examples: Q2 Examples
     | search_topic      | language  |
     | London            | Deutsch   |
     | Tokyo             | Esperanto |