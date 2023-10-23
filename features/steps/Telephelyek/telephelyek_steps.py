import time
from behave import step

from features.steps.Telephelyek.Telephelyek import Telephelyek
from database.classes.Query import Query


@step('Add telephely')
def step_impl(c):
    Telephelyek.open_add_site_modal(c.driver)

@step('Telephelyek rögzítése')
def step_impl(c):
    q = Query()
    sites = q.get_all_sites()

    for site in sites:
        partner = q.get_partner_by_id(site.partner_id)

        Telephelyek.open_add_site_modal(c)
        Telephelyek.wait_for_site_modal(c)
        Telephelyek.insert_name_to_input(c, f"{partner.first_name} {partner.last_name}")
        Telephelyek.insert_city_to_input(c, site.city)
        Telephelyek.insert_zip_to_input(c, site.zip_code)
        Telephelyek.insert_street_name_to_input(c, site.street_name)
        Telephelyek.insert_house_number_to_input(c, site.house_number)
        Telephelyek.cancel(c)
