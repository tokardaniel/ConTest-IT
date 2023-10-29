import os
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from datetime import datetime
from database.migration import Migration

load_dotenv(os.path.join(os.getcwd(), ".env"))
timestamp = datetime.timestamp(datetime.now())
path_dir = f"screenshots/{timestamp}"
os.mkdir(path_dir)

def before_all(context):
    context.driver = _get_driver()
    context.driver.get(os.getenv("BWPOOL_URL"))
    # migrate memory database
    migration = Migration()
    migration.run()

def after_step(context, step):
    filename = f"{step.name.replace(' ', '_')}.png"
    context.driver.get_screenshot_as_file(os.path.join(path_dir, filename))

def after_all(context):
    context.driver.quit()

def _get_driver() -> object:
    options = Options()
    if bool(int(os.getenv("RUN_HEADLESS"))):
        options.add_argument("--headless")
        options.add_argument("--window-size=1920x1080")
        options.add_argument('--no-sandbox')

    # download setup
    download_path = os.path.join(os.getcwd(), "downloads")
    _clear_download_folder(download_path)
    prefs = {"download.default_directory" : download_path}
    options.add_experimental_option("prefs", prefs)

    return webdriver.Chrome(options=options)

def _clear_download_folder(folder: str):
    for filename in os.listdir(folder):
        if not filename.endswith("xlsx"):
            continue
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
