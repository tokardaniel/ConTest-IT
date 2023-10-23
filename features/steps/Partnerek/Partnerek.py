
from utils.selenium_utils.elements import Elements
from selenium.webdriver.common.by import By

class Partnerek:

    @classmethod
    def open_partner_modal(cls, c: object) -> None:
        add_btn_element = Elements.find_element(
            c.driver,
            (By.XPATH, "//div[@id='Grid_add']/button")
        )

        add_btn_element.click()

    @classmethod
    def partner_modal_showed(cls, c: object) -> None:
         Elements.wait_for_element_visibility(
            c.driver,
            (By.ID, "Grid_dialogEdit_wrapper_dialog-header")
        )

    @classmethod
    def wait_for_partner_modal(cls, c: object) -> None:
        Elements.wait_for_element_visibility(
            c.driver,
            (By.ID, "Grid_dialogEdit_wrapper_dialog-header")
        )

    @classmethod
    def partners_grid_is_showed(cls, c: object) -> None:
        grid_element = Elements.find_element(c.driver, (By.ID, "Grid"))

        assert grid_element.is_displayed(), "Megnézzük, hogy megjelent e az ügyfeleket tartalamzó grid"

    @classmethod
    def insert_name_to_input(cls, c: object, name: str) -> None:
        Elements.insert_text_to_input(c.driver, (By.ID, "name"), name)

    @classmethod
    def insert_email_to_input(cls, c: object, email: str) -> None:
        Elements.insert_text_to_input(c.driver, (By.ID, "email"), email)

    @classmethod
    def insert_phone_number_to_input(cls, c: object, p_number: str) -> None:
        Elements.insert_text_to_input(
            c.driver,
            (By.XPATH, "//td[@class='e-rowcell']//input[@placeholder='+36 xxxxxxxxx']"),
            p_number
        )

    @classmethod
    def insert_description_to_input(cls, c: object, description: str) -> None:
        Elements.insert_text_to_input(c.driver, (By.ID, "comment"), description)

    @classmethod
    def save(cls, c: object) -> None:
        save_btn_element = Elements.find_element(
            c.driver,
            (By.XPATH, "//div[@class='e-footer-content']/button[contains(text(), 'Save')]")
        )

        save_btn_element.click()

    @classmethod
    def cancel(cls, c: object) -> None:
        cancel_btn_element = Elements.find_element(
            c.driver,
            (By.XPATH, "//div[@class='e-footer-content']/button[contains(text(), 'Cancel')]")
        )

        cancel_btn_element.click()
