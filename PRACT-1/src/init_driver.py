#init_driver
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import os

def create_driver(path):
    """
    Crea una instancia del navegador Microsoft Edge utilizando Selenium.

    Args:
        path (str): Ruta al ejecutable del driver de Edge (por ejemplo, 'msedgedriver.exe').

    Returns:
        webdriver.Edge: Instancia del navegador Edge lista para usar.
    """
    edgedriver_path = os.path.abspath(path)
    service = Service(executable_path=edgedriver_path)
    return webdriver.Edge(service=service)

def open_url(driver, url):
    """
    Abre una URL específica en el navegador Selenium.

    Args:
        driver: Instancia del navegador Selenium.
        url (str): Dirección web que se desea abrir.

    Returns:
        None
    """
    driver.get(url)
