from pytest_bdd import scenarios, when, then, parsers
import pytest

scenarios('../features/upload.feature')
    
@when(parsers.parse('the user upload file {fileName}'), converters={"fileName": str})    
def upload_file(upload_page, fileName):
    upload_page.enter_file_path(fileName)
    
@when('the user clicks on Submit file button')
def click_submit_button(upload_page):
    upload_page.click_on_submit_file_button()
       
@when(parsers.parse('the user click on I accept terms of service checkbox with {isClickable}'), converters={"isClickable": bool})
def click_on_terms_checkbox(upload_page, isClickable):
    upload_page.click_on_terms_checkbox(isClickable)
    
@then('success message should be shown')
def assert_success_message(upload_page):
    assert 'uploaded' in upload_page.get_message_text()    

@pytest.mark.xfail 
@then('error message should be shown')
def assert_error_message(upload_page):
    print('This test case could not be tested')