from init_driver import create_driver, open_url
from scrap_elements import (find_element_and_click, extract_elements, get_links_from_elements, build_recipes_links,
                            get_recipe)
from config import DRIVER_NAME, BASE_URL, SELECTORS, HEADERS
from preprocessing import extract_country
from save import save_recipes
import pandas as pd
from selenium.webdriver.common.by import By
import time
import csv


def main():
    driver = create_driver(DRIVER_NAME)
    open_url(driver, BASE_URL)
    accept_cookies = find_element_and_click(driver, By.ID, SELECTORS["cookies"])
    time.sleep(3)
    menu = find_element_and_click(driver, By.CSS_SELECTOR, SELECTORS["menu"])
    time.sleep(3)
    cuisines = find_element_and_click(driver, By.XPATH, SELECTORS["cuisines"])
    time.sleep(3)
    view_all = find_element_and_click(driver, By.XPATH, SELECTORS["view_all"])
    time.sleep(3)
    cuisines_list = extract_elements(driver, By.CSS_SELECTOR, SELECTORS["cuisines_list"])
    time.sleep(3)
    cuisines_links = get_links_from_elements(cuisines_list)
    driver.close()
    driver.quit()
    country_url = extract_country(cuisines_links)
    recipes_links = build_recipes_links(country_url, HEADERS, target_country="Spanish")
    recipes = get_recipe(recipes_links, max_recipes_per_country=3)
    save_recipes(recipes)
    recipes_df = pd.read_csv("Recetas.csv", delimiter=";")
    print(recipes_df.head())

if __name__ == "__main__":
    main()


