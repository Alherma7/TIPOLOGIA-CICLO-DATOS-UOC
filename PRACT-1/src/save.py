#save.py
import csv

def save_recipes(recipes, csv_path="Recetas.csv"):

    with open(csv_path, "w", encoding="utf-8", newline="") as f_csv:
        writer = csv.writer(f_csv, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([
            "url", "pais", "titulo", "fecha", "autor", "descripcion_corta", "calificacion_media", "num_reviews",
            "preparacion", "ingredientes", "categoria_principal", "nutrition"
        ])
        for recipe in recipes:
            writer.writerow([
                recipe["url"], recipe["pais"], recipe["titulo"], recipe["fecha"], recipe["autor"],
                recipe["descripcion_corta"], recipe["calificacion_media"], recipe["num_reviews"],
                recipe["preparacion"], recipe["ingredientes"], recipe["categoria_principal"],
                recipe["nutrition"]
            ])

