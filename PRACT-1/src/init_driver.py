#init_driver
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import os

def create_driver(path):
    edgedriver_path = os.path.abspath(path)
    service = Service(executable_path=edgedriver_path)
    return webdriver.Edge(service=service)

def open_url(driver, url):
    driver.get(url)

