from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import os
import time

edgedriver_path = os.path.abspath("msedgedriver.exe")
service = Service(executable_path=edgedriver_path)
driver = webdriver.Edge(service=service)

driver.get("https://www.allrecipes.com/")
time.sleep(2)
# cookies
accept_cookies_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
accept_cookies_button.click()

time.sleep(2)
# menu
menu = driver.find_element(By.CSS_SELECTOR, "#header_1-0 > div.mntl-header__menu-top > div.mntl-header__menu-button-container > button")
menu.click()

time.sleep(2)
# cuisines
cuisines = driver.find_element(By.XPATH, "//*[@id='mntl-fullscreen-nav_1-0']/ul/li[5]/a")
cuisines.click()
time.sleep(2)
view_all = driver.find_element(By.XPATH, "//*[@id='mntl-fullscreen-nav__sublist-cuisines-mntl-fullscreen-nav']/ul/li[9]/a")
view_all.click()

time.sleep(2)

cuisines_links = []
cuisines_list = driver.find_elements(By.CSS_SELECTOR, "a.mntl-link-list__link")
for c in cuisines_list:
        cuisine = c.get_attribute('href')
        cuisines_links.append(cuisine)
time.sleep(10)
driver.close()
driver.quit()

# continuar con beautiful soup y request


