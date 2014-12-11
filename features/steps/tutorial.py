from lettuce import *

@step('we have behave installed')
def step_impl(step):
    pass

@step('we implement a test')
def step_impl(step):
    assert True is not False

@step('lettuce will test it for us!')
def step_impl(step):
    assert True is True