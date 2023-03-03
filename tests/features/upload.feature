@upload_file @web
Feature: Upload file feature
  As a web surfer,
  I want to upload file,
  So I can view it later.

  Background: 
    Given the Guru99 Demo home page is displayed

  @unhappy
  Scenario: Don't upload file
    When the user clicks on Submit file button
    Then error message should be shown

  @unhappy
  Scenario Outline: Upload file with size smaller than threshold & don't accept Terms Of Service
    When the user upload file <fileName>
    And the user clicks on Submit file button
    And the user click on I accept terms of service checkbox with "false"
    Then error message should be shown

    Examples: Files
      | fileName          |
      | data/file_1MB.pdf |

  # @unhappy
  # Scenario Outline: Upload file with size bigger than threshold
  #   When the user upload file <fileName>
  #   And the user click on I accept terms of service checkbox with "true"
  #   And the user clicks on Submit file button
  #   Then error message should be shown

  #   Examples: Files
  #     | fileName            |
  #     | data/file_250MB.avi |

  @happy
  Scenario Outline: Upload file with size smaller than threshold & accept Terms Of Service
    When the user upload file <fileName>
    And the user click on I accept terms of service checkbox with "true"
    And the user clicks on Submit file button
    Then success message should be shown

    Examples: Files
      | fileName          |
      | data/file_1MB.avi |
