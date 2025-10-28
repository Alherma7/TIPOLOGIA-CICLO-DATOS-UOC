#scrap_elements.py
import requests
from bs4 import BeautifulSoup
from config import HEADERS
from preprocessing import clean_autor


def find_element_and_click(driver, by, selector):
    return driver.find_element(by, selector).click()

def extract_elements(driver, by, selector):
    return driver.find_elements(by, selector)

def get_links_from_elements(elements, mode="selenium"):
    if mode == "selenium":
        return [el.get_attribute("href") for el in elements if el.get_attribute("href")]
    elif mode == "bs4":
        return [el.get("href") for el in elements if el.get("href")]

def build_recipes_links(dict_url, headers, target_country=None):
    recipes_links = {}

    if target_country:
        if target_country not in dict_url:
            print(f"Country '{target_country}' not found.")
            return {}
        dict_url = {target_country: dict_url[target_country]}

    for country, url in dict_url.items():
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        recetas = soup.select('a.mntl-card-list-items')
        recipes_links[country] = get_links_from_elements(recetas,mode="bs4")
    return recipes_links



def scrape_recipes(url, pais):
    html = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(html, 'lxml')
    errores = 0

    def scrape_find(tag, clase):
        nonlocal errores
        try:
            return soup.find(tag, class_=clase).text.strip()
        except:
            errores += 1
            return "NA"

    def scrape_select_one(selector):
        nonlocal errores
        try:
            return soup.select_one(selector).text.strip()
        except:
            errores += 1
            return "NA"

    return {
        "url": url,
        "pais": pais,
        "titulo": scrape_find("h1", "article-heading text-headline-400"),
        "fecha": scrape_find("div", "mntl-attribution__item-date"),
        "autor_raw": scrape_find("div", "comp mntl-bylines__item mntl-attribution__item mntl-attribution__item--has-date"),
        "descripcion_corta": scrape_find("p", "article-subheading text-utility-300"),
        "calificacion_media": scrape_find("div", "comp mm-recipes-review-bar__rating mntl-text-block text-label-300"),
        "num_reviews": scrape_find("div", "comp mm-recipes-review-bar__comment-count mntl-text-block text-label-300 global-link"),
        "preparacion": scrape_find("div", "comp mm-recipes-details"),
        "ingredientes": scrape_find("ul", "mm-recipes-structured-ingredients__list"),
        "categoria_principal": scrape_select_one("#mntl-text-link_10-0 > span"),
        "nutrition": scrape_find("table", "mm-recipes-nutrition-facts-summary__table"),
        "errores": errores
    }


def get_recipe(dict_recipes, max_recipes_per_country=None):
    recipes = []

    for country, urls in dict_recipes.items():
        valid_recipe = 0

        for url in urls:
            if max_recipes_per_country is not None and valid_recipe >= max_recipes_per_country:
                break

            recipe = scrape_recipes(url, country)
            if recipe["errores"] <= 4:
                recipe["autor"] = clean_autor(recipe["autor_raw"])
                del recipe["autor_raw"]
                recipes.append(recipe)
                valid_recipe += 1

    return recipes
