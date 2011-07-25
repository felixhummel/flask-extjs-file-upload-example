Feature: Upload File
    The only thing
    this thing can do
    is enabling the user
    to upload a file.

    Scenario: Check out this nice UI!
        When I go to the file upload page
        Then I see a nice UI

    Scenario: Upload a file.
        When I go to the file upload page
        And I select the file "/tmp/bridge.jpg"
        And I press the "Save" button
        Then I should be redirected to "/uploads/bridge.jpg"
        And should see my image

