# Lista de promedios de matemáticas
promedios = [4.33, 5, 7, 9.66, 10, 8, 6, 2, 1.33, 3, 4, 4.50, 7.50, 6.66, 5.50, 9, 4, 1, 10, 4.50, 7.33, 7, 8, 5.50, 6, 6, 2, 5]

# Función para clasificar los promedios y contar los intervalos
def clasificar_promedios(promedios):
    intervalos = {
        '[0, 2[': [],
        '[2, 4[': [],
        '[4, 6[': [],
        '[6, 8[': [],
        '[8, 10]': []
    }
    
    for promedio in promedios:
        if 0 <= promedio < 2:
            intervalos['[0, 2['].append(promedio)
        elif 2 <= promedio < 4:
            intervalos['[2, 4['].append(promedio)
        elif 4 <= promedio < 6:
            intervalos['[4, 6['].append(promedio)
        elif 6 <= promedio < 8:
            intervalos['[6, 8['].append(promedio)
        elif 8 <= promedio <= 10:
            intervalos['[8, 10]'].append(promedio)
    
    # Contar los promedios en cada intervalo
    totales = {intervalo: len(promedios_en_intervalo) for intervalo, promedios_en_intervalo in intervalos.items()}
    
    return intervalos, totales

# Clasificar los promedios y contar los intervalos
resultado, totales = clasificar_promedios(promedios)

# Mostrar los promedios en cada intervalo
for intervalo, promedios_en_intervalo in resultado.items():
    print(f'{intervalo}: {promedios_en_intervalo}')

# Mostrar el total de promedios en cada intervalo
print("\nTotales:")
for intervalo, total in totales.items():
    print(f'{intervalo}: {total}')

