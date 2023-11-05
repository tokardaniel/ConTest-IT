import time
from behave import step
from database.models import Device, Partner

from features.steps.Eszkozok.Eszkozok import Eszkozok
from database.classes.Query import Query
from utils.selenium_utils.elements import Elements

@step('Add eszköz')
def step_impl(c):
    Eszkozok.open_add_site_modal(c)

@step("Eszközök rögzítése modal megnyitása")
def step_impl(c):
    Eszkozok.open_add_device_modal(c)


@step("Eszközök rögzítése")
def step_impl(c):
    q = Query()
    partners = q.get_all_partners_full_join()
    for partner in partners:
        for site in partner.sites:
            for device in site.devices:
                Eszkozok.open_add_device_modal(c)
                Eszkozok.wait_for_device_modal(c)
                Eszkozok.insert_device_name_to_input(c, f"{device.manufacturer} {device.model}")
                Eszkozok.select_partner_from_combobox(c, name=f"{partner.first_name} {partner.last_name}")
                time.sleep(2)
                Eszkozok.select_site_from_combobox(c, name=site.street_name)
                Eszkozok.insert_description_to_input(c, ds=device.platform)
                Eszkozok.insert_comment_to_input(c, comm=device.serial_number)
                Eszkozok.save(c)
                Eszkozok.find_device_from_table(c, partner=partner, device=device)
                Eszkozok.clear_table_search(c)

    Eszkozok.download(c)

@step("Egy eszköz szervízstátuszának módosítása")
def step_impl(c):
    q = Query()
    partner: Partner = q.get_all_partners_full_join()[0]
    device: Device = partner.sites[0].devices[0]

    Eszkozok.find_device_from_table(c, partner=partner, device=device)
    Eszkozok.edit_selected_device(c)
    Eszkozok.wait_for_device_modal(c)
    Eszkozok.click_on_checkbox(c)
    Eszkozok.update_service_status_in_db(device=device)
    Eszkozok.save(c)

    # visszakeressük az eszközt

    Eszkozok.find_device_from_table(c, partner=partner, device=device)
    assert Eszkozok.service_checkbox_is_displayed(c)
