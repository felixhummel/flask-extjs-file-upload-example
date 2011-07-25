from lettuce import before, world
from splinter.browser import Browser

@before.all
def initial_setup():
    world.browser = Browser()
