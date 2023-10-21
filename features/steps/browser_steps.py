from behave import step

from selenium_utils.elements import Elements

@step('Megjelent az oldal')
def step_imp(c):
    brand_item = Elements.find_element_by_xpath(c.driver, "//a[contains(text(), 'BWP nyilvántartó')]")
    c.driver.save_screenshot('screenshots/loaded_page.png')

    assert brand_item.is_displayed(), "Ha megjelent a 'BWP nyilvántartó felirat', akkor talán az oldal is"
