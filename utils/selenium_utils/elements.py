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
    def insert_text_to_input_and_tab(cls, driver: object, locator: Tuple[str, str], text: str) -> None:
        element = driver.find_element(*locator)
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.TAB)

    @classmethod
    def insert_text_to_input_and_enter(cls, driver: object, locator: Tuple[str, str], text: str) -> None:
        element = driver.find_element(*locator)
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

    @classmethod
    def select_combobox_by_name(cls,
                        driver: object,
                        text_input_locator: Tuple[str, str],
                        list_items_locator: Tuple[str, str],
                        name: str,
                        wait_time: int = 10
    ):
        text_input_element = driver.find_element(*text_input_locator)
        text_input_element.clear()
        text_input_element.send_keys(name)
        # megvárjuk, hogy lenyíljon rendesen a lista
        WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located(locator=list_items_locator)
        )
        list_element = driver.find_element(*list_items_locator)
        list_element.click()

    @classmethod
    def wait_for_spinner(cls, driver: object, time: int = 10):
        WebDriverWait(driver, time).until(
            EC.invisibility_of_element((By.CLASS_NAME, "e-spin-bootstrap5"))
        )
