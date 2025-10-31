#save.py
import csv

def save_recipes(recipes, csv_path="Recetas.csv"):
    """
    Guarda una lista de recetas en un archivo CSV con formato delimitado por punto y coma.

    Args:
        recipes (list): Lista de diccionarios, donde cada diccionario representa una receta con campos.
        csv_path (str): Ruta y nombre del archivo CSV de salida. Por defecto es "Recetas01.csv".

    Returns:
        None
    """
    
    with open(csv_path, "w", encoding="utf-8", newline="") as f_csv:
        writer = csv.writer(f_csv, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([
            "url", "pais", "titulo", "fecha", "autor", "calificacion_media", "num_reviews",
            "realizado_casa","preparacion", "ingredientes", "categoria_principal", "nutrition"
        ])
        for recipe in recipes:
            writer.writerow([
                recipe["url"], recipe["pais"], recipe["titulo"], recipe["fecha"], recipe["autor"],
                recipe["calificacion_media"], recipe["num_reviews"],recipe["realizado_casa"],recipe["preparacion"],
                recipe["ingredientes"], recipe["categoria_principal"], recipe["nutrition"]
            ])



