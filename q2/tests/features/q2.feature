# Created by BJ at 19/06/2015

Feature: Q2 Web Front-End Test
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