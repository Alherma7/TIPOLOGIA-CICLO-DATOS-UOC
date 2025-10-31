#preprocessing

def extract_country(list_of_urls):
    """
    Extrae el nombre del país desde una lista de URLs y construye un diccionario con el país como clave.

    Args:
        list_of_urls (list): Lista de URLs que contienen el nombre del país en la última parte del path.

    Returns:
        dict: Diccionario con nombres de países como claves y sus URLs como valores.
    """
    urls = {}
    for url in list_of_urls:
        parts = url.strip("/").split("/")
        country = parts[-1]
        name = country.replace("-", " ").capitalize()
        urls[name] = url
    return urls

def clean_autor(texto):
    """
    Limpia el texto del autor, extrayendo las primeras cuatro palabras.

    Args:
        texto (str): Cadena de texto con el nombre del autor.

    Returns:
        str: Nombre del autor limpio o 'NA' si no hay información válida.
    """
    if texto == "NA":
        return "NA"
    return " ".join(texto.strip().split()[0:4])
