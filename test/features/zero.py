from lettuce import *

@step('I go to the file upload page')
def i_go_to(step):
    world.response = world.browser.visit('http://localhost:5000')

@step('I see a nice UI')
def see_ui(step):
    world.browser.is_element_present_by_css('.x-panel-header-text')
    assert world.browser.is_text_present('File Upload Form')

@step('I select the file "(.*)"')
def upload_img(step, filename):
    input_field_name = 'file'
    world.browser.attach_file(input_field_name, filename)

@step('I press the "(.*)" button')
def click_btn(step, txt):
    world.browser.find_by_css('button')[1].click()

@step('I should be redirected to "(.*)"')
def check_img(step, path):
    import time
    time.sleep(1)
    assert world.browser.status_code.is_success()
    path in world.browser.url

@step('should see my image')
def see_img(step):
    assert world.browser.find_by_css('img[src]').first
