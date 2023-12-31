from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

from utils.selenium_utils.elements import Elements
from utils.data_source_utils.load_data import LoadData

@step('Megjelent az oldal')
def step_imp(c):
    brand_item_locator = (By.XPATH, "//a[contains(text(), 'BWP nyilvántartó')]")

    Elements.wait_for_element_visibility(c.driver, brand_item_locator)

    brand_item = Elements.find_element(c.driver, brand_item_locator)

    assert brand_item.is_displayed(), "Ha megjelent a 'BWP nyilvántartó felirat', akkor talán az oldal is"

@step('"{size}" db új adat betöltése API-n keresztül')
def step_impl(c, size: int):
    l = LoadData()
    l.load(size)

@step('Legyen egy partner a következő id-val "{id}", akinek van egy random eszköze')
def step_impl(c, id: int):
    l = LoadData()
    l.load(size=1, test_id=int(id))
