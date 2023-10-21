import time
from behave import step

@step('Open the page')
def step_imp(c):
    c.browser.get('https://www.google.com')
    time.sleep(5)
    c.browser.save_screenshot('screenshots/loaded_page.png')
