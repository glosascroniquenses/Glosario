import csv
import os

def generar_paginas_html(csv_file):
    # Leer el archivo CSV
    with open(csv_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]

    # Crear un directorio para almacenar las páginas HTML
    if not os.path.exists('paginas_html'):
        os.makedirs('paginas_html')

    # Iterar sobre los datos y generar una página HTML por cada valor único en la columna 'categorías'
    for row in data:
        categoria = row['categorias']
        link = row['WEB']

        # Generar el contenido HTML
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{categoria}</title>
        </head>
        <body>
            <h1>{categoria}</h1>
            <p>Enlace: <a href="{link}">{link}</a></p>
        </body>
        </html>
        """

        # Escribir el contenido HTML en un archivo
        file_name = f"paginas_html/{categoria.replace(' ', '_')}.html"
        with open(file_name, 'w') as html_file:
            html_file.write(html_content)

# Llamar a la función para generar las páginas HTML
generar_paginas_html("datos.csv")
