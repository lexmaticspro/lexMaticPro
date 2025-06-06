
# LexMatic Pro IA - Abogado Virtual con Búsqueda Inteligente y Aproximada

import pandas as pd
from fuzzywuzzy import fuzz

# Cargar modelos
modelos = pd.read_csv('modelos.csv')

print("🔍 LexMatic Pro IA - Abogado Virtual (Búsqueda Inteligente)")

# Pregunta inicial: área del derecho
categoria = input("¿En qué área estás? (Salud / Familia / Laboral / Discapacidad / Cautelares): ").capitalize()

# Filtramos por categoría
filtrados = modelos[modelos['categoria'] == categoria]

if filtrados.empty:
    print("❌ No tenemos modelos en esa área todavía.")
else:
    # Mostramos los títulos disponibles
    print("\nModelos disponibles:")
    for index, row in filtrados.iterrows():
        print(f"- {row['titulo']}")

    # Preguntar palabra clave
    palabra = input("\nEscribe una palabra clave o concepto para buscar: ").lower()

    resultados = []

    for index, row in filtrados.iterrows():
        # Evaluamos similitud
        score_titulo = fuzz.partial_ratio(palabra, row['titulo'].lower())
        score_contenido = fuzz.partial_ratio(palabra, row['contenido'].lower())
        max_score = max(score_titulo, score_contenido)

        # Si el score es alto, lo consideramos relevante
        if max_score > 60:  # Umbral de 60%
            resultados.append((row, max_score))

    # Ordenar resultados por mejor coincidencia
    resultados = sorted(resultados, key=lambda x: x[1], reverse=True)

    if not resultados:
        print("❌ No se encontraron modelos relevantes.")
    else:
        for row, score in resultados:
            print(f"\n📚 Modelo encontrado: {row['titulo']}")
            print(f"Contenido: {row['contenido']}")
            print(f"Fundamento jurídico: {row['fundamento']}")
            print(f"🔎 Nivel de coincidencia: {score}%")
