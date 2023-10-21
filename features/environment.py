import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

load_dotenv(os.path.join(os.getcwd(), ".env"))

def before_all(context):
    context.driver = get_driver()
    context.driver.get(os.getenv("BWPOOL_URL"))

def after_all(context):
    context.driver.quit()

def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)

    return driver
