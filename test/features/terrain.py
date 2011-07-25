from lettuce import before, after, world
from splinter.browser import Browser

@before.all
def initial_setup():
    world.browser = Browser()

@after.all
def teardown(wtf):
    world.browser.quit()
