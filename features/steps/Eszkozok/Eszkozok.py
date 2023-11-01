import time
from selenium.webdriver.common.by import By
from database.models import Partner
from database.models.Device import Device
from selenium.webdriver.remote import webelement

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

    @classmethod
    def find_device_from_table(cls, c: object, partner: Partner, device: Device) -> bool:
        partner_full_name = f"{partner.first_name} {partner.last_name}"
        Elements.insert_text_to_input_and_enter(c.driver, (By.ID, "Grid_ToolbarSearchBox"), partner_full_name)

        time.sleep(2)

        # feltételezzük, hogy lehetnek azonos nevű ügyfelek, ezért az összes találatot megvizsgáljuk soronként
        # legalább a név és az eszköz neve egyezik
        table_rows = Elements.find_element(
            c.driver,
            (By.XPATH, "//table[@class='e-table']/tbody")
        ).find_elements(By.TAG_NAME, "tr")

        for row in table_rows:
            if cls._finded_name_and_device_name_in_row(row, partner_full_name, f"{device.manufacturer} {device.model}"):
                return True

        return False

    @classmethod
    def clear_table_search(cls, c: object) -> None:
        clear_icon = Elements.find_element(c.driver, (By.CLASS_NAME, "e-clear-icon"))
        clear_icon.click()
        time.sleep(2)

    @classmethod
    def edit_selected_device(cls, c: object) -> None:
        # Előfeététel, hogy a grid le legyen szűrve

        # Kiválasztjuk a gridből szerkesztésre a leszűrt első elemet
        Elements.find_element(
            c.driver,
            (By.XPATH, "(//table[@class='e-table']/tbody/tr[@class='e-row e-altrow']/td)[1]")
        ).click()

        # Megnyomjuk az edit gombot
        Elements.find_element(c.driver, (By.ID, "Grid_add")).click()

        # checkbox bejelölése
        Elements.find_element(c.driver, (By.XPATH, "//span[@class='e-label' and contains(text(), 'Szervíz')]")).click()

    @classmethod
    def download(cls, c):
        downloand_btm_item = Elements.find_element(c.driver, (By.XPATH, "//div[@id='Grid_excelexport']/button"))

        downloand_btm_item.click()

    @classmethod
    def click_on_checkbox(cls, c):
        Elements.find_element(c.driver, (By.XPATH, "//input[@class='e-control e-checkbox e-lib']")).click()

    @classmethod
    def _finded_name_and_device_name_in_row(cls, row: webelement, name: str, device_name: str) -> bool:
        tds = row.find_elements(By.TAG_NAME, "td")

        finded_name: bool = False
        finded_device: bool = False
        for td in tds:
            if td.text == name:
                finded_name = True
            if td.text == device_name:
                finded_device = True

        if finded_device and finded_name:
            return True

        return False
