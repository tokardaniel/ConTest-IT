from behave import step
from database.models.Partner import Partner
from database.models.Site import Site

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
        Telephelyek.select_name_from_combobox(c, name=f"{partner.first_name} {partner.last_name}")
        Telephelyek.insert_city_to_input(c, site.city)
        Telephelyek.insert_zip_to_input(c, site.zip_code)
        Telephelyek.insert_street_name_to_input(c, site.street_name)
        Telephelyek.insert_house_number_to_input(c, site.house_number)
        Telephelyek.save(c)
        Telephelyek.find_site_from_table(c, partner=partner, site=site)

@step('Utoljára rögzített telephely visszakeresése')
def step_imppl(c):
    q = Query()
    partner: Partner = q.get_all_partners_full_join()[0]

    Telephelyek.find_site_from_table(c, partner=partner, site=partner.sites[0])

@step('Telephely adatok oldal megnyitása')
def step_impl(c):
    Telephelyek.open_site_link(c)

@step('Eszköz adatok összehasolítása az excelben lévő adatokkal')
def step_impl(c):
    # kiveszünk egy partnert a db-ből, rákeresünk és megnézzük, az eszköz adatokat,
    # hogy egyeznek e a db-ben lévőkkel
    q = Query()
    partner: Partner = q.get_all_partners_full_join()[0]
    site: Site = partner.sites[0]

    Telephelyek.find_site_from_table(c, partner=partner, site=site)

    Telephelyek.open_site_link(c)

    # Explicit wait
    Telephelyek.site_profile_showed(c)

    Telephelyek.compare_with_excel(c)

@step('Telephelyek adatlap megjelent')
def step_impl(c) -> None:
    Telephelyek.site_profile_showed(c)
