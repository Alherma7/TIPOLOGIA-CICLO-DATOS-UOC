import requests
from bs4 import BeautifulSoup
from config import HEADERS
from preprocessing import clean_autor
import time

def find_element_and_click(driver, by, selector):
    """
    Encuentra un elemento en la página usando Selenium y hace clic en él.

    Args:
        driver: Instancia del navegador Selenium.
        by: Tipo de selector (By.ID, By.CSS_SELECTOR, etc.).
        selector: Valor del selector.

    Returns:
        None
    """
    return driver.find_element(by, selector).click()

def extract_elements(driver, by, selector):
    """
    Extrae los atributos 'href' de los elementos encontrados con Selenium.

    Args:
        driver: Instancia del navegador Selenium.
        by: Tipo de selector.
        selector: Valor del selector.

    Returns:
        list: Lista de enlaces (href) encontrados.
    """
    elements = driver.find_elements(by, selector)
    return [el.get_attribute("href") for el in elements]

def get_links_from_elements(elements):
    """
    Extrae los enlaces 'href' de una lista de elementos BeautifulSoup, con pausa entre cada uno.

    Args:
        elements: Lista de elementos BeautifulSoup.

    Returns:
        list: Lista de enlaces válidos.
    """
    links = []
    for el in elements:
        links.append(el.get("href"))
        time.sleep(1)
    return links

def build_recipes_links(dict_url, headers, target_country=None):
    """
    Construye un diccionario de enlaces de recetas por país a partir de las URLs base.

    Args:
        dict_url: Diccionario con países como claves y URLs como valores.
        headers: Cabeceras HTTP para la petición.
        target_country: País específico a filtrar (opcional).

    Returns:
        dict: Diccionario con países y sus enlaces de recetas.
    """
    recipes_links = {}

    if target_country:
        dict_url = {target_country: dict_url[target_country]}

    for country, url in dict_url.items():
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        recetas = soup.select('a.mntl-card-list-items')
        recipes_links[country] = get_links_from_elements(recetas)
    return recipes_links

def scrape_recipes(url, pais):
    """
    Extrae los datos de una receta individual desde su URL.

    Args:
        url: Enlace de la receta.
        pais: País de origen de la receta.

    Returns:
        dict: Diccionario con los datos extraídos de la receta.
    """
    html = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(html, 'lxml')
    errores = 0

    def scrape_find(tag, clase):
        """
        Busca un elemento por etiqueta y clase, devuelve texto o 'NA' si falla.
        """
        nonlocal errores
        try:
            return soup.find(tag, class_=clase).text.strip()
        except:
            errores += 1
            return "NA"

    def scrape_select_one(selector):
        """
        Busca un elemento por selector CSS, devuelve texto o 'NA' si falla.
        """
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
        "calificacion_media": scrape_find("div", "comp mm-recipes-review-bar__rating mntl-text-block text-label-300"),
        "num_reviews": scrape_find("div", "comp mm-recipes-review-bar__comment-count mntl-text-block text-label-300 global-link"),
        "preparacion": scrape_find("div", "comp mm-recipes-details"),
        "ingredientes": scrape_find("ul", "mm-recipes-structured-ingredients__list"),
        "categoria_principal": scrape_select_one("#mntl-universal-breadcrumbs_1-0"),
        "realizado_casa": scrape_select_one("#mm-recipes-made-it__count_1-0"),
        "nutrition": scrape_find("table", "mm-recipes-nutrition-facts-summary__table"),
        "errores": errores
    }

def get_recipe(dict_recipes, max_recipes_per_country=None):
    """
    Procesa todas las recetas por país, aplicando filtros de calidad.

    Args:
        dict_recipes: Diccionario con países y listas de URLs de recetas.
        max_recipes_per_country: Número máximo de recetas por país (opcional).

    Returns:
        list: Lista de recetas válidas procesadas.
    """
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
