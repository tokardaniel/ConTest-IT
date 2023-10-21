from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    context.browser =  get_driver_path()

def after_all(context):
    context.browser.quit()

def get_driver_path():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)

    return driver
