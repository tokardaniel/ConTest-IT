import random
import time
from behave import step
from faker import Faker
from database.models import Partner

from utils.data_source_utils.load_data import LoadData

from utils.selenium_utils.elements import Elements
from database.classes.Query import Query
from steps.Partnerek.Partnerek import Partnerek

@step('Partner modal megjelenítése')
def step_impl(c):
    Partnerek.open_partner_modal(c)

@step('Megjelent az ügyfelek grid')
def step_impl(c):
    Partnerek.partners_grid_is_showed(c)

@step('Add partner modal megjelent')
def step_impl(c):
    Partnerek.partners_grid_is_showed(c)

@step('Fake név megadása')
def step_impl(c):
    fake = Faker()
    Partnerek.insert_name_to_input(c, fake.name)

@step('Email megadása: "{email}"')
def step_impl(c, email: str):
    Partnerek.insert_email_to_input(c. email)

@step('Telefonszám megadása: "{telszam}"')
def step_impl(c, telszam: str):
    Partnerek.insert_phone_number_to_input(c, telszam)

@step('Megjegyzés megadása: "{megjegyzes}"')
def step_impl(c, megjegyzes: str):
    Partnerek.insert_description_to_input(megjegyzes)

@step('Mentés')
def step_impl(c):
    Partnerek.save(c)

@step('Letöltött partnerek rögzítése')
def step_impl(c):
    q = Query()
    partners = q.get_all_partners()

    for partner in partners:
        Partnerek.open_partner_modal(c)
        Partnerek.wait_for_partner_modal(c)
        Partnerek.insert_name_to_input(c, name=f"{partner.first_name} {partner.last_name}")
        Partnerek.insert_email_to_input(c, email=partner.email)
        Partnerek.insert_description_to_input(c, description=partner.data_id)
        Partnerek.cancel(c)


