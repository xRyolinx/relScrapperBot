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
    
    # save page start
    start = int(params['page'])
    
    # scrap profiles
    for page in range(nb_pages):
        # get url
        params['page'] = start + page
        url = getUrl(params)
        print(f"Page - {params['page']}")
        
        # get to link
        driver.get(url)

        # get profiles
        newProfiles = getContacts(driver)
        for profile in newProfiles:
            print(f"{i}- {profile['name']}")
            i = i + 1
        
        # append to profiles
        profiles += newProfiles
        print()
    
    # save to excel
    saveToExcel(profiles)

# run script
main()