from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from const import params, link, PATH, nb_pages, FILENAME
from helper.urlHelper import getUrl
from helper.chromedriver import launchBrowser
from helper.search import getContacts
from helper.excel import saveToExcel


def main():
    # start driver
    driver = launchBrowser(PATH)
    
    # loop
    profiles = []
    i = 1
    
    # scrap profiles
    for page in range(nb_pages):
        # get url
        params['page'] = int(params['page']) + page
        url = getUrl(params)
        
        # get to link
        driver.get(url)

        # get profiles
        profiles += getContacts(driver)
        for profile in profiles:
            print(f"{i}- {profile}")
            i = i + 1
    
    # save to excel
    saveToExcel(profiles)

# run script
main()