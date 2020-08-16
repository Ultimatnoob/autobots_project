import py
import re


def test_submit_form(py, fake):
    # 1. Visit url
    py.visit('https://demoqa.com/text-box')
    # 2. Submit form
    py.get('#userName').type('Dan Matheson')
    py.get('#userEmail').type('Dan@dan.com')
    address = fake.address()
    address = re.sub("\s+", '', address)
    py.get('#currentAddress').type(address)
    py.get('#permanentAddress').type('456 DIY street')
    # 3. assert something
    py.get('#submit').click()
    output = py.get('#output')
    assert 'Dan Matheson' in output.text()
    assert 'Dan@dan.com' in output.text()
    assert address in output.text()

def test_submit_form_refactored(py, fake):
    url = 'https://demoqa.com/text-box'
    name = fake.name()
    email = fake.email()
    current_address = fake.address().replace("\n", " ")
    permanent_address = fake.address().replace("\n", " ")

    py.visit(url)
    py.get('#userName').type(name)
    py.get('#userEmail').type(email)
    py.get('#currentAddress').type(current_address)
    py.get('#permanentAddress').type(permanent_address)
    py.get('#submit').click()
    output = py.get('#output').text()

    assert name in output
    assert email in output
    assert current_address in output
    assert permanent_address in output
