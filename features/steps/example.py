from behave import *
from lettuce import *

class Example:
    def __init__(self):
        self._counter = 0

    def count(self):
        self._counter += 1
        return self._counter

    def clear_counter(self):
        self._counter = 0
        return self._counter

    def get_value(self):
        return self._counter

    def set_counter(self, val):
        self._counter = int(val)

    def hello(self, name):
        return "Hello, " + name

    def hello_world(self):
        return "hello world"

counters = []

@step('a name')
@step('approached by others')
def step_pass(step):
    pass

@step('greet appropriately by saying hello')
def assertHello(step):
    example = Example()
    for row in step.hashes:
        assert example.hello(row['name']) == row['greeting']

@step('an initialized counter')
def setCounters(step):
    for row in step.hashes:
        counter = Example()
        counter.set_counter(row['val'])
        counters.append(counter)

@step('the counter is incremented')
def incrCounters(step):
    print "incr"
    for counter in counters:
        counter.count()

@step('the counter should be incremented')
def assertIncr(step):
    expected = []
    vals = []

    for row in step.hashes:
        expected.append(int(row['incr']))

    for counter in counters:
        vals.append(counter.get_value() )

    assert 0 is cmp(expected, vals)