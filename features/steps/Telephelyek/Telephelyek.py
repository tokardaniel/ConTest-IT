from selenium.webdriver.common.by import By

from utils.selenium_utils.elements import Elements


class Telephelyek:

    @classmethod
    def open_add_site_modal(cls, c: object) -> None:
        add_btn_element = Elements.find_element(
            c.driver, (By.XPATH, "//div[@id='Grid_add']/button")
        )

        add_btn_element.click()

    @classmethod
    def wait_for_site_modal(cls, c: object) -> None:
        Elements.wait_for_element_visibility(
            c.driver,
            (By.ID, "Grid_dialogEdit_wrapper_title")
        )

    @classmethod
    def insert_city_to_input(cls, c: object, city: str) -> None:
        Elements.insert_text_to_input(
            c.driver,
            (By.ID, "varos"),
            city
        )

    @classmethod
    def insert_zip_to_input(cls, c: object, zip: str) -> None:
        Elements.insert_text_to_input(
            c.driver,
            (By.ID, "zip"),
            zip
        )

    @classmethod
    def insert_street_name_to_input(cls, c: object, street_name: str) -> None:
        Elements.insert_text_to_input(
            c.driver,
            (By.ID, "utca"),
            street_name
        )

    @classmethod
    def insert_house_number_to_input(cls, c: object, house_number: str) -> None:
        Elements.insert_text_to_input(
            c.driver,
            (By.ID, "szam"),
            house_number
        )

    @classmethod
    def select_name_from_combobox(cls, c: object, name: str) -> None:
        Elements.select_combobox_by_name(c.driver,
                    (By.XPATH, "//input[@placeholder='Ügyfél']"),
                    (By.XPATH, f"//li[contains(text(), '{name}')]"),
                    name
        )

    @classmethod
    def save(cls, c: object) -> None:
        save_btn_item = Elements.find_element(
            c.driver,
            (By.XPATH, "//div[@class='e-footer-content']/button[contains(text(), 'Save')]")
        )

        save_btn_item.click()

    @classmethod
    def cancel(cls, c: object) -> None:
        cancel_btn_item = Elements.find_element(
            c.driver,
            (By.XPATH, "//div[@class='e-footer-content']/button[contains(text(), 'Cancel')]")
        )

        cancel_btn_item.click()
