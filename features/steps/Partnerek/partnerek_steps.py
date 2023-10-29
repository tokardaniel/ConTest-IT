from behave import step

from database.classes.Query import Query
from steps.Partnerek.Partnerek import Partnerek

@step('Partner modal megjelenítése')
def step_impl(c):
    Partnerek.open_partner_modal(c)

@step('Megvárjuk, hogy eltűnjön a táblázatból a következő szöveget tartalmazó element: "{text}"')
def step_imp(c, text: str):
    Partnerek.wait_for_partner_grid_placeholder_text(c, text)

@step('Megjelent az ügyfelek grid')
def step_impl(c):
    Partnerek.partners_grid_is_showed(c)

@step('Add partner modal megjelent')
def step_impl(c):
    Partnerek.partners_grid_is_showed(c)

@step('Név megadása: "{nev}"')
def step_impl(c, nev: str):
    Partnerek.insert_name_to_input(c, nev)

@step('Email megadása: "{email}"')
def step_impl(c, email: str):
    Partnerek.insert_email_to_input(c, email)

@step('Telefonszám megadása: "{telszam}"')
def step_impl(c, telszam: str):
    Partnerek.insert_phone_number_to_input(c, telszam)

@step('Megjegyzés megadása: "{megjegyzes}"')
def step_impl(c, megjegyzes: str):
    Partnerek.insert_description_to_input(c, megjegyzes)

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
        Partnerek.save(c)
        assert Partnerek.find_partner_from_table(c, partner=partner)
