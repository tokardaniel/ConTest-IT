from behave import step
from database.models.Partner import Partner
from database.models.Site import Site
from database.models.Device import Device

from features.steps.Telephelyek.Telephelyek import Telephelyek
from database.classes.Query import Query


@step('Add telephely')
def step_impl(c) -> None:
    Telephelyek.open_add_site_modal(c.driver)

@step('Telephelyek rögzítése')
def step_impl(c) -> None:
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

@step('Telephelyek rögzítése a következő azonosítóval rendelkező pernerhez: "{id}"')
def step_impl(c, id: int) -> None:
    q = Query()
    partner = q.get_partner_by_test_id(id=int(id))
    sites = partner.sites

    for site in sites:
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
def step_imppl(c) -> None:
    q = Query()
    partner: Partner = q.get_all_partners_full_join()[0]

    Telephelyek.find_site_from_table(c, partner=partner, site=partner.sites[0])

@step('Telephely adatok oldal megnyitása')
def step_impl(c) -> None:
    Telephelyek.open_site_link(c)

@step('Eszköz adatok összehasolítása az excelben lévő adatokkal')
def step_impl(c) -> None:
    # kiveszünk egy partnert a db-ből, rákeresünk és megnézzük, az eszköz adatokat,
    # hogy egyeznek e a excel-ben lévőkkel
    q = Query()
    partner: Partner = q.get_all_partners_full_join()[0]
    site: Site = partner.sites[0]

    Telephelyek.find_site_from_table(c, partner=partner, site=site)

    Telephelyek.open_site_link(c)

    # Explicit wait
    Telephelyek.site_profile_showed(c)

    Telephelyek.compare_with_excel(c)

@step('A következő id-val rendelkező partner: "{id}" eszköz adatinak összehasolítása az excelben lévő adatokkal')
def step_impl(c, id: int) -> None:
    # kiveszünk egy partnert a db-ből, rákeresünk és megnézzük, az eszköz adatokat,
    # hogy egyeznek e a excel-ben lévőkkel
    q = Query()
    partner: Partner = q.get_partner_by_test_id(id=int(id))
    site: Site = partner.sites[0]

    Telephelyek.find_site_from_table(c, partner=partner, site=site)

    Telephelyek.open_site_link(c)

    # Explicit wait
    Telephelyek.site_profile_showed(c)

    Telephelyek.compare_with_excel(c)

@step('Telephelyek adatlap megjelent')
def step_impl(c) -> None:
    Telephelyek.site_profile_showed(c)

@step('A következő id-val rendelkező "{id}" partnerhez tartozó telephely esetén nem jelennek meg a szervízben lévő eszközök')
def step_impl(c, id: int) -> None:
    q = Query()
    partner: Partner = q.get_all_service_devices_of_partner_by_test_id(id=int(int))[0]
    site: Site = partner.sites[0]
    device: Device = site.devices[0]

    Telephelyek.find_site_from_table(c, partner=partner, site=site)

    Telephelyek.open_site_link(c)

    # Explicit wait
    Telephelyek.site_profile_showed(c)

    Telephelyek.compare_with_db(c, device=device)

@step('Egy telephely esetén nem jelennek meg a szervízben lévő eszközök')
def step_impl(c) -> None:
    # keresünk egy olyan partnert, akinek van szervízben lévő eszköze
    q = Query()
    partner: Partner = q.get_all_service_devices_of_partner()[0]
    site: Site = partner.sites[0]
    device: Device = site.devices[0]

    Telephelyek.find_site_from_table(c, partner=partner, site=site)

    Telephelyek.open_site_link(c)

    # Explicit wait
    Telephelyek.site_profile_showed(c)

    Telephelyek.compare_with_db(c, device=device)
