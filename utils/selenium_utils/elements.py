from typing import Tuple
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class Elements:

    @classmethod
    def find_element(cls, driver: object, locator: Tuple[str, str]) -> object:
        return driver.find_element(*locator)

    @classmethod
    def wait_for_element_visibility(cls, driver: object, locator: Tuple[str, str], time: int = 20):
        WebDriverWait(driver, time).until(
            EC.visibility_of_element_located(locator=locator)
        )

    @classmethod
    def wait_for_element_invisibility(cls, driver: object, locator: Tuple[str, str], time: int = 20) -> None:
        WebDriverWait(driver, time).until(
            EC.invisibility_of_element_located(locator=locator)
        )

    @classmethod
    def insert_text_to_input(cls, driver: object, locator: Tuple[str, str], text: str) -> None:
        element = driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    @classmethod
    def insert_text_to_input_and_enter(cls, driver: object, locator: Tuple[str, str], text: str) -> None:
        element = driver.find_element(*locator)
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.ENTER)
