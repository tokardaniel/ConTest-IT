import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

from database.models.Partner import Partner
from database.models.Site import Site
from database.models.Device import Device
from features.steps.Excel.Excel import Excel
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

    @classmethod
    def find_site_from_table(cls, c: object, partner: Partner, site: Site) -> bool:
        partner_full_name = f"{partner.first_name} {partner.last_name}"
        Elements.insert_text_to_input_and_enter(c.driver, (By.ID, "Grid_ToolbarSearchBox"), partner_full_name)

        time.sleep(2)

        # feltételezzük, hogy lehetnek azonos nevű ügyfelek, ezért az összes találatot megvizsgáljuk soronként
        # legalább az a név a város és az irányítószám egyezik
        table_rows = Elements.find_element(
            c.driver,
            (By.XPATH, "//table[@class='e-table']/tbody")
        ).find_elements(By.TAG_NAME, "tr")

        for row in table_rows:
            if cls._finded_name_and_city_and_zip_in_row(row, partner_full_name, site.city, site.zip_code):
                return True

        return False

    @classmethod
    def open_site_link(cls, c: object) -> None:
        link_item = Elements.find_element(
            c.driver,
            (By.XPATH, "//table[@id='Grid_content_table']/tbody/tr/td/div/div/a[@class='nav-link']")
        )
        link_item.click()

    @classmethod
    def compare_with_excel(cls, c: object) -> None:
        excel_full_path = os.path.join(os.getcwd(), f"{os.getenv('DOWNLOADS_PATH')}/{os.getenv('EXCEL_FILE_NAME')}")
        excel = Excel(excel_full_path)

        # soronként megyünk a táblázatban, gondolva arra, hogy több eszköz is lehet
        rows = Elements.find_element(
            c.driver,
            (By.XPATH, "//table[@id='toolList_content_table']/tbody")
        ).find_elements(By.TAG_NAME, "tr")

        for row in rows:
            tds = row.find_elements(By.TAG_NAME, "td")
            azon = int(tds[0].text)
            device_name = tds[1].text

            assert excel.find_value_in_column("Azonosító", azon).empty is False
            assert excel.find_value_in_column("Neve", device_name).empty is False

    @classmethod
    def compare_with_db(cls, c: object, device: Device) -> None:
        rows = Elements.find_element(
            c.driver,
            (By.XPATH, "//table[@id='toolList_content_table']/tbody")
        ).find_elements(By.TAG_NAME, "tr")

        for row in rows:
            tds = row.find_elements(By.TAG_NAME, "td")
            if tds[0].text == "No records to display":
                return None
            device_name = tds[1].text

            db_device_name = f"{device.manufacturer} {device.model}"
            if device_name == db_device_name:
                raise Exception("Megjelent a szervíz státuszban lévő eszköz a telepheyek oldalon")

    @classmethod
    def site_profile_showed(cls, c: object) -> None:
        Elements.wait_for_element_visibility(
            c.driver,
            (By.XPATH, "//h6[contains(text(), 'Telephely adatok')]")
        )

    @classmethod
    def _finded_name_and_city_and_zip_in_row(cls, row: webelement, name: str, city: str, zip: str) -> bool:
        tds = row.find_elements(By.TAG_NAME, "td")

        finded_name: bool = False
        finded_city: bool = False
        finded_zip: bool = False
        for td in tds:
            if td.text == name:
                finded_name = True
            if td.text == city:
                finded_city = True
            if td.text == zip:
                finded_zip = True

        if finded_city and finded_name and finded_zip:
            return True

        return False
