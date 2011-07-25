from lettuce import *

@step('I go to the file upload page')
def i_go_to(step):
    world.response = world.browser.visit('http://localhost:5000')

@step('I see a nice UI')
def see_ui(step):
    world.browser.is_element_present_by_css('.x-panel-header-text')
    assert world.browser.is_text_present('File Upload Form')
