partidas = [
("Bryan", "Bosque", 120),
("Omar", "Desierto", 90),
("Gaby", "calle", 150),
("Cristian", "Ciudad", 200),
("Eder", "Bosque", 110)
]

puntos = {}
mapas = set()

for p in partidas:
    jugador = p[0]
    mapa = p[1]
    pts = p[2]

    mapas.add(mapa)

    if jugador in puntos:
        puntos[jugador] = puntos[jugador] + pts
    else:
        puntos[jugador] = pts

print(puntos)
print()
print(mapas)
print()

