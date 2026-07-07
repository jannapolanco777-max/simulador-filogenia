# Matriz de distancias entre 4 especies
# Representa qué tan diferentes son genéticamente entre sí

distancias = {
    ("A", "B"): 2,
    ("A", "C"): 4,
    ("A", "D"): 6,
    ("B", "C"): 4,
    ("B", "D"): 6,
    ("C", "D"): 6,
}

print(distancias)
def encontrar_par_mas_cercano(distancias):
    # Buscamos el par de especies con la distancia mas chica
    par_mas_cercano = min(distancias, key=distancias.get)
    valor_mas_chico = distancias[par_mas_cercano]
    return par_mas_cercano, valor_mas_chico


par, distancia = encontrar_par_mas_cercano(distancias)
print(f"El par mas cercano es {par} con una distancia de {distancia}")

def unir_par(distancias, par):
    especie1, especie2 = par
    nuevo_grupo = f"({especie1},{especie2})"

    # Encontramos todas las especies que no son parte del par que se unio
    otras_especies = set()
    for a, b in distancias:
        otras_especies.add(a)
        otras_especies.add(b)
    otras_especies.discard(especie1)
    otras_especies.discard(especie2)

    nueva_distancias = {}

    # Copiamos las distancias que no involucran al par unido
    for (a, b), valor in distancias.items():
        if especie1 not in (a, b) and especie2 not in (a, b):
            nueva_distancias[(a, b)] = valor

    # Calculamos la distancia del grupo nuevo hacia cada especie restante
    for especie in otras_especies:
        d1 = distancias.get((especie1, especie)) or distancias.get((especie, especie1))
        d2 = distancias.get((especie2, especie)) or distancias.get((especie, especie2))
        promedio = (d1 + d2) / 2
        nueva_distancias[(nuevo_grupo, especie)] = promedio

    return nueva_distancias


nueva_matriz = unir_par(distancias, par)
print(f"Nueva matriz despues de unir {par}:")
print(nueva_matriz)

def construir_arbol(distancias):
    pasos = []

    while len(distancias) > 0:
        # Verificamos cuantas especies distintas quedan
        especies = set()
        for a, b in distancias:
            especies.add(a)
            especies.add(b)

        if len(especies) <= 1:
            break

        par, dist = encontrar_par_mas_cercano(distancias)
        pasos.append((par, dist))
        distancias = unir_par(distancias, par)

    return pasos


pasos = construir_arbol(distancias)

print("Orden de agrupamiento del arbol:")
for i, (par, dist) in enumerate(pasos, start=1):
    print(f"Paso {i}: se unieron {par} con una distancia de {dist}")