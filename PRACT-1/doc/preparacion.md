# Proyectos de Web Scraping

## Ejemplos de repositorios

1. [Web scraping a una web de espectáculos](https://github.com/jonortizabalia/Web_Scraping_PR1_UOC/blob/master/espectaculos.csv)
2. [Web scraping a Filmin](https://github.com/jonortizabalia/Web_Scraping_PR1_UOC/blob/master/espectaculos.csv)
3. [Web scraping a Filmaffinity](https://github.com/ldetorreUOC/Practica1-Web-scraping/blob/main/best_films.csv)
4. [Web scraping de hidrografía](https://github.com/rsalamanquesb/web-scraping/tree/master/csv)
5. [Web scraping de libros](https://github.com/iboda001/PRA1-WebScraping/tree/master/Informe)
6. [Productos de ferretería](https://github.com/dcanete/PRA1WebScraping)
7. [Subastas de pisos](https://github.com/anderestebanez/Practica-1-Web-scraping)
8. [Blog scraping](https://github.com/obachiller/WebScraping)
9. [Datos sobre COVID](https://github.com/SevillaFe/UOC_Web-Scraping)
10. [Nanosatélites](https://github.com/beejeke/nanosat-scraping)

---

## Recursos para Web Scraping

- [Más de 50 ejemplos con Requests, Scrapy, Selenium, LXML, BeautifulSoup](https://github.com/lkuffo/web-scraping)
- [Idealista (Scrapy)](https://github.com/David-Carrasco/Scrapy-Idealista/blob/master/README.md)
- [Indeed scraper](https://github.com/Ram-95/Indeed_Job_Scraper/blob/master/Indeed_Job_Scraper.py)
- [Carrefour scraper (Selenium)](https://github.com/carlosvertiz/Carrefour_WebScraping/blob/main/Carrefour_WebScraping.py)
- [CarrefourTracker PDF](https://github.com/equipoUOC/CarrefourTracker/blob/main/pdf/PRAC1_WebScraping.pdf)
- [PC Componentes PDF](https://github.com/mtldevai/scrapper-pccomponentes/blob/master/PRAC1%20Web%20Scrapping.pdf)

---

## Allrecipes: Web de interés

- [Scraping A Recipe Website | Analytics Vidhya](https://medium.com/analytics-vidhya/scraping-a-recipe-website-with-python-selenium-9e5f3f4e3c3d)
- [Scrapy spider para recetas y nutrición](https://github.com/shaansubbaiah/allrecipes-scraper)
- [Paquete Python para scraping de recetas](https://github.com/hhursev/recipe-scrapers)
- [Proyecto con más de 13,000 recetas](https://github.com/phuongdtrn/Python-Web-Scraping-Allrecipes)
- [Scrapers para webs populares de cocina](https://github.com/anand-07-a/recipe_scraper)

> ⚠️ Esta web puede bloquear scrapers tras 10–15 descargas rápidas.

---

## Nota técnica

No acabo de entender lo del uso de `user-agent`, si ya indicamos en Selenium cuál estamos usando.

---

# Memoria técnica

## 1. Contexto

El objetivo principal es construir un conjunto de datos estructurado que permita estudiar qué recetas tienen más éxito en cada país. Es una fuente fiable debido a que se puede justificar usando la sección “About Us” del sitio web.

## 2. Título

**Recetas de diferentes países**

## 3. Descripción del dataset

*(Pendiente de completar)*

## 4. Representación gráfica

Esto se realizará con **Tableau**.

## 5. Contenido

Se puede incluir la fecha en que se subió cada receta. Los campos propuestos son:

- `url_receta`: Enlace permanente (texto)
- `titulo`: Nombre descriptivo (texto)
- `fecha`
- `autor`
- `descripcion_corta`: Resumen inicial (texto)
- `calificacion_media`: Puntuación promedio (float)
- `num_reviews`: Número de valoraciones (int)
- `tiempo_preparacion`: Tiempo estimado (texto)
- `tiempo_coccion`: Tiempo de cocción/reposo (texto)
- `tiempo_total`
- `ingredientes`: Lista estandarizada (texto o lista)
- `porciones`: Número de personas (int)
- `categoria_principal`: Clasificación general (texto)
- `calorias`
- `grasas`
- `carbohidratos`
- `proteínas`

## 6. Propietario

Utilizar el repositorio de GitHub del enlace o trabajos similares de análisis de recetas.

## 7. Inspiración

Podríamos enfocarlo en el objetivo de montar un restaurante y analizar qué recetas o platos son los más populares.

## 8. Licencia

La que sea más adecuada (por ejemplo, CC0, CC BY-NC-SA 4.0, etc.)

## 9. Código

Implementado en **Python**.

## 10. Dataset

Definir los datos a obtener. Ejemplo de estructura:

| Nombre       | Autor       | Valoración | n_val | Reviews | Publicado   | Prep time | Total time | Ingredientes | Nutrition facts | Comentarios | n_home_cooks |
|--------------|-------------|------------|-------|---------|-------------|-----------|------------|---------------|------------------|-------------|---------------|
| Chimichurri  | John Mitze  | 4.5        | 230   | 174     | 21/03/2024  | 15        | 15         | So yummy      | 525              |             |               |

## 11. Vídeo

*(Pendiente de grabar y subir a Google Drive)*
