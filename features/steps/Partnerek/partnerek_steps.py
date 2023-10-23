from behave import step
from faker import Faker
from selenium.webdriver.common.by import By

from utils.selenium_utils.elements import Elements

@step('Partner modal megjelenítése')
def step_impl(c):
    add_btn_element = Elements.find_element(
        c.driver,
        (By.XPATH, "//div[@id='Grid_add']/button")
    )

    add_btn_element.click()

@step('Megjelent az ügyfelek grid')
def step_impl(c):
    grid_element = Elements.find_element(c.driver, (By.ID, "Grid"))

    assert grid_element.is_displayed(), "Megnézzük, hogy megjelent e az ügyfeleket tartalamzó grid"

@step('Add partner modal megjelent')
def step_impl(c):
    Elements.wait_for_element_visibility(
        c.driver,
        (By.ID, "Grid_dialogEdit_wrapper_dialog-header")
    )

@step('Fake név megadása')
def step_impl(c):
    fake = Faker()
    Elements.insert_text_to_input(c.driver, (By.ID, "name"), fake.name())

@step('Email megadása: "{email}"')
def step_impl(c, email: str):
    Elements.insert_text_to_input(c.driver, (By.ID, "email"), email)

@step('Telefonszám megadása: "{telszam}"')
def step_impl(c, telszam: str):
    Elements.insert_text_to_input(
        c.driver,
        (By.XPATH, "//td[@class='e-rowcell']//input[@placeholder='+36 xxxxxxxxx']"),
        telszam
    )

@step('Megjegyzés megadása: "{megjegyzes}"')
def step_impl(c, megjegyzes: str):
    Elements.insert_text_to_input(c.driver, (By.ID, "comment"), megjegyzes)

@step('Mentés')
def step_impl(c):
    save_btn_element = Elements.find_element(
        c.driver,
        (By.XPATH, "//div[@class='e-footer-content']/button[contains(text(), 'Save')]")
    )

    save_btn_element.click()
