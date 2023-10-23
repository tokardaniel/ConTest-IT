import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(os.path.join(os.getcwd(), ".env"))
timestamp = datetime.timestamp(datetime.now())
path_dir = f"screenshots/{timestamp}"
os.mkdir(path_dir)

def before_all(context):
    context.driver = _get_driver()
    context.driver.get(os.getenv("BWPOOL_URL"))

def after_step(context, step):
    filename = f"{step.name.replace(' ', '_')}.png"
    context.driver.get_screenshot_as_file(os.path.join(path_dir, filename))

def after_all(context):
    context.driver.quit()

def _get_driver() -> object:
    options = Options()
#    options.add_argument("--headless")
#    options.add_argument("--window-size=1920x1080")
#    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)

    return driver
