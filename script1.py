# Lista de edades
edades = [18, 25, 36, 13, 4, 6, 7, 42, 56, 35, 5, 6, 44, 37, 21, 47, 32, 7, 33, 26, 23, 11, 14, 12, 15, 16, 17, 13, 12, 23]

# Función para clasificar las edades y contar las categorías
def clasificar_edades(edades):
    categorias = {
        'Infantiles': [],
        'Cadetes menores': [],
        'Cadetes mayores': [],
        'Activos': []
    }
    
    for edad in edades:
        if 4 <= edad <= 11:
            categorias['Infantiles'].append(edad)
        elif 12 <= edad <= 15:
            categorias['Cadetes menores'].append(edad)
        elif 16 <= edad <= 18:
            categorias['Cadetes mayores'].append(edad)
        else:
            categorias['Activos'].append(edad)
    
    # Contar las edades en cada categoría
    totales = {categoria: len(edades_en_categoria) for categoria, edades_en_categoria in categorias.items()}
    
    return categorias, totales

# Clasificar las edades y contar las categorías
resultado, totales = clasificar_edades(edades)

# Mostrar las edades en cada categoría
for categoria, edades_en_categoria in resultado.items():
    print(f'{categoria}: {edades_en_categoria}')

# Mostrar el total de edades en cada categoría
print("\nTotales:")
for categoria, total in totales.items():
    print(f'{categoria}: {total}')


