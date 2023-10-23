from behave import step
from selenium.webdriver.common.by import By

from utils.selenium_utils.elements import Elements

@step('Megjelent az oldal')
def step_imp(c):
    brand_item = Elements.find_element(c.driver, (By.XPATH, "//a[contains(text(), 'BWP nyilvántartó')]"))

    assert brand_item.is_displayed(), "Ha megjelent a 'BWP nyilvántartó felirat', akkor talán az oldal is"

@step('Megvárjuk, hogy eltűnjön a táblázatból a következő szöveget tartalmazó element: "{text}"')
def step_imp(c, text: str):
    Elements.wait_for_element_invisibility(
        c.driver,
        (By.XPATH, f"//table[@class='e-table']/tbody/tr/td[contains(text(), '{text}')]")
    )
