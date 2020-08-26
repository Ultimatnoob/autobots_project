import py


def test_yes_radio_button(py):
    py.visit('https://demoqa.com/radio-button')
    py.get('#yesRadio').click(force=True)
    assert py.get('.text-success').should().have_text('Yes')


def test_impressive_radio(py):
    py.visit('https://demoqa.com/radio-button')
    py.get('#impressiveRadio').click(force=True)
    assert py.get('.text-success').should().have_text('Impressive')


def test_no_radio(py):
    py.visit('https://demoqa.com/radio-button')
    no_radio = py.get('#noRadio')
    enable_no_javascript(py, no_radio)
    no_radio.click(force=True)
    assert no_radio.is_selected()


def enable_no_javascript(py, element):
    py.execute_script('arguments[0].disabled = false', element.webelement)


