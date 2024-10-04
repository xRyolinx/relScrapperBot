from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



def getContacts(driver):    
    contacts = []
    profiles = []
    time.sleep(1)
    
    # check if elements loaded and return
    profiles = driver.find_elements(By.XPATH, "(//ul[@role='list'])[1]/li")
    print(f"Potentiel profiles: {len(profiles)}")
    
    # get infos
    for profile in profiles:
        contact = getInfos(profile)
        if contact:
            contacts.append(contact)
    
    # end
    return contacts
    


def getInfos(profile):
    infos = {}
    try:
        # get name
        name = profile.find_element(By.XPATH, ".//span[@dir='ltr']/span[1]").text
        
        # get details
        details = profile.find_element(By.XPATH, "(.//div)[1]/div[1]/div[1]/div[2]/*[2]").text
        
        # get link
        link = profile.find_element(By.XPATH, ".//a[contains(@class, 'app-aware-link')]").get_attribute('href').split('?', 1)[0]
        
        # get poste
        poste = profile.find_element(By.XPATH, ".//div[contains(@class, 'entity-result__primary-subtitle')]").text
        
        # get place
        place = profile.find_element(By.XPATH, ".//div[contains(@class, 'entity-result__secondary-subtitle')]").text

        # assemble
        infos = {
            'name': name,
            'details': details,
            'link': link,
            'poste': poste,
            'place': place,
        }
    except:
        pass
    
    return infos
