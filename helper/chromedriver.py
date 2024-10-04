from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from const import PROFILE_PATH


def launchBrowser(path):
    service = webdriver.ChromeService(executable_path=path)
    options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # options.add_argument('--headless=new')
    
    options.add_argument("--start-maximized")
    options.add_argument("--log-level=3")

    # chrome profile
    options.add_argument(f"--user-data-dir={PROFILE_PATH}")
    driver = webdriver.Chrome(service=service, options=options)
    return driver

