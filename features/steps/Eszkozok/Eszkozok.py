from selenium.webdriver.common.by import By

from utils.selenium_utils.elements import Elements

class Eszkozok:

    @classmethod
    def open_add_device_modal(cls, c: object) -> None:
        add_btm_item = Elements.find_element(c.driver, (
            By.XPATH,
            "//div[@id='Grid_toolbarItems']//button[@aria-label='Add']")
        )

        add_btm_item.click()

    @classmethod
    def wait_for_device_modal(cls, c: object) -> None:
        Elements.wait_for_element_visibility(
            c.driver,
            (By.ID, "Grid_dialogEdit_wrapper_title")
        )

    @classmethod
    def insert_device_name_to_input(cls, c: object, device_name: str) -> None:
        Elements.insert_text_to_input(c.driver, (By.ID, "name"), device_name)

    @classmethod
    def insert_description_to_input(cls, c: object, ds: str) -> None:
        Elements.insert_text_to_input(c.driver, (By.ID, "Desc"), ds)

    @classmethod
    def insert_comment_to_input(cls, c: object, comm: str) -> None:
        Elements.insert_text_to_input(c.driver, (By.ID, "Comm"), comm)

    @classmethod
    def select_partner_from_combobox(cls, c: object, name: str) -> None:
        Elements.select_combobox_by_name(
            c.driver,
            (By.XPATH, "//input[@placeholder='Ügyfél']"),
            (By.XPATH, f"//li[contains(text(), '{name}')]"),
            name
        )

    @classmethod
    def select_site_from_combobox(cls, c: object, name: str) -> None:
        Elements.select_combobox_by_name(
            c.driver,
            (By.XPATH, "//input[@placeholder='Telephely']"),
            (By.XPATH, f"//li[contains(text(), '{name}')]"),
            name
        )

    @classmethod
    def save(cls, c: object) -> None:
        cancel_btn_item = Elements.find_element(
            c.driver,
            (By.XPATH, "//div[@class='e-footer-content']/button[contains(text(), 'Save')]")
        )

        cancel_btn_item.click()

    @classmethod
    def cancel(cls, c: object) -> None:
        cancel_btn_item = Elements.find_element(
            c.driver,
            (By.XPATH, "//div[@class='e-footer-content']/button[contains(text(), 'Cancel')]")
        )

        cancel_btn_item.click()
