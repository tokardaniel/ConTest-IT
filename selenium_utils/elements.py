from selenium.webdriver.common.by import By

class Elements:

    @classmethod
    def find_element_by_xpath(cls, driver: object, xpath: str) -> object:
        return driver.find_element(By.XPATH, xpath)
