import time
from utils.selenium_utils.elements import Elements
from database.models.Partner import Partner
from selenium.webdriver.common.by import By

class Partnerek:

    @classmethod
    def wait_for_partner_grid_placeholder_text(cls, c: object, text: str) -> None:
        Elements.wait_for_element_invisibility(
            c.driver,
            (By.XPATH, f"//table[@class='e-table']/tbody/tr/td[contains(text(), '{text}')]")
        )

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

    @classmethod
    def find_partner_from_table(cls, c: object, partner: Partner) -> bool:
        partner_full_name = f"{partner.first_name} {partner.last_name}"
        Elements.insert_text_to_input_and_enter(c.driver, (By.ID, "Grid_ToolbarSearchBox"), partner_full_name)

        time.sleep(2)

        # feltételezzük, hogy lehetnek azonos nevű ügyfelek, ezért az összes találatot megvizsgáljuk soronként
        # legalább az email ás a név egyezik
        table_rows = Elements.find_element(
            c.driver,
            (By.XPATH, "//table[@class='e-table']/tbody")
        ).find_elements(By.TAG_NAME, "tr")

        for row in table_rows:
            if cls._finded_name_and_email_in_row(row, partner_full_name, partner.email):
                return True

        return False

    @classmethod
    def _finded_name_and_email_in_row(cls, row, name, email) -> bool:
        tds = row.find_elements(By.TAG_NAME, "td")

        finded_email: bool = False
        finded_name: bool = False
        for td in tds:
            if td.text == name:
                finded_name = True
            if td.text == email:
                finded_email = True

        if finded_email and finded_name:
            return True

        return False
