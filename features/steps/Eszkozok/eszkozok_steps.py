import time
from behave import step

from features.steps.Eszkozok.Eszkozok import Eszkozok
from database.classes.Query import Query


@step('Add eszköz')
def step_impl(c):
    Eszkozok.open_add_site_modal(c)

@step("Eszközök rögzítése modal megnyitása")
def step_impl(c):
    Eszkozok.open_add_device_modal(c)


@step("Eszközök rögzítése")
def step_impl(c):
    q = Query()
    devices = q.get_all_devices()

    for device in devices:
        q = Query()
        partners = q.get_all_partners_full_join()
        for partner in partners:
            for site in partner.sites:
                for device in site.devices:
                    replaced_zip_code = site.zip_code.replace("-", "")
                    Eszkozok.open_add_device_modal(c)
                    Eszkozok.wait_for_device_modal(c)
                    Eszkozok.insert_device_name_to_input(c, f"{device.manufacturer} {device.model}")
                    Eszkozok.select_partner_from_combobox(c, name=f"{partner.first_name} {partner.last_name}")
                    time.sleep(2)
                    Eszkozok.select_site_from_combobox(c, name=f"{replaced_zip_code} {site.city}, {site.street_name} {site.house_number}")
                    Eszkozok.insert_description_to_input(c, ds=device.platform)
                    Eszkozok.insert_comment_to_input(c, comm=device.serial_number)
                    Eszkozok.save(c)
