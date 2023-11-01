from behave import step
from selenium.webdriver.common.by import By

from utils.selenium_utils.elements import Elements

@step('Navigálás a bal menüben a következő menüpontra: "{menupont_neve}"')
def step_impl(c, menupont_neve: str):
    nav_element = Elements.find_element(
        c.driver, (By.XPATH , f"//div/a[contains(@class, 'nav-link') and contains(text(), '{menupont_neve}')]")
    )

    nav_element.click()
