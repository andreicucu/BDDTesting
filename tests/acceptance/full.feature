Feature: Authentication into Sytel CC and Campaign creation

  Scenario: Login using valid username and password should authenticate the user
    User is able to create a new campaign from scratch given the correct inputs
    Given I am presented with the login page
    And I click fill the tenant, username, password and hit enter
    And I am presented with the Sytel options
    And User is in the campaign manager web application
    When New button is pressed
    And Campaign name is filled
    And Campaign type is selected
    And Database Input is given
    And Database Fields are selected
    And Ok button is pressed
    Then Campaign should be visible
#    And Campaign can be started