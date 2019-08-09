Feature: Asker and Expert can enter session
  @fixture.browser.asker
  @fixture.browser.expert
  Scenario: Asker and Expert can enter session and send chat message
    Given Expert is on Landing Page
    When Expert logs in by email and password successfully
    Then Expert should be able to skip Intro Modal
    And Expert should enter Homepage
    When Expert clicks Start Working button
    Then Expert should be in Connecting Area

    Given Asker is on Landing Page
#    When Asker logs in by Google account
    When Asker logs in by email and password successfully
    Then Asker should enter Homepage

    When Asker posts a question with description and type successfully
    Then Asker should see Matching Modal
    When Expert claims Asker's question
    Then Asker should be able to close Problem Expert Intro Modal
    And Asker should enter Workspace
    And Expert should enter on Workspace

    When Asker sends a chat message
    Then Expert should see Asker's chat message
