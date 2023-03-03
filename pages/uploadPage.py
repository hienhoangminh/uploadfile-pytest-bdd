from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
from pages.basePage import BasePage

class UploadPage(BasePage):
    
    TERMS_CHECKBOX = (By.ID, 'terms')
    SUBMIT_FILE_BUTTON = (By.ID, 'submitbutton') 
    FILE_INPUT = (By.ID, 'uploadfile_0')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'h3#res')
    
    def __init__(self, browser):
        super().__init__(browser)
    
    def go_to(self, url):
        self._browser.get(url)
        
    def click_on_terms_checkbox(self, isClickable):
        if isClickable:
            self._wait.until(EC.presence_of_element_located(self.TERMS_CHECKBOX))
            checkbox = self._browser.find_element(*self.TERMS_CHECKBOX)
            checkbox.click()
            
    def enter_file_path(self, name):
        input = self._browser.find_element(*self.FILE_INPUT)
        input.send_keys(os.path.abspath(name))    
 
    def click_on_submit_file_button(self):
        self._wait.until(EC.presence_of_element_located(self.SUBMIT_FILE_BUTTON))
        submit_button = self._browser.find_element(*self.SUBMIT_FILE_BUTTON)  
        submit_button.click()
        self._wait.until(EC.element_to_be_clickable(self.SUBMIT_FILE_BUTTON))

        
    def get_message_text(self):
        message = self._browser.find_element(*self.SUCCESS_MESSAGE)
        print(message.is_displayed())
        return message.get_attribute("textContent")
                
    def __isAt__(self):
        assert self._browser.title == 'File Upload Demo'   
             