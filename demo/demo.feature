Feature: Svenska Spel test
    Test some different use cases using gherkin
    and python and behave

    Scenario: Searching for one specific subject
      Given I can access Svenska spel
      When I search for "Oddset"
     Then I get a result for "Oddset"

    Scenario: Login as a user and check profile
      Given I can access Svenska spel
      Then I, "Fredrik" can login as user
      Then verify that I can access my profile data
      And  logout in a controlled way 

