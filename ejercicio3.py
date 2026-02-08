inventario = [
{"producto": "Laptop", "categoria": "Electrónica", "stock": 5},
{"producto": "PC", "categoria": "Electrónica", "stock": 25},
{"producto": "Silla", "categoria": "Muebles", "stock": 2},
{"producto": "Escritorio", "categoria": "Muebles", "stock": 0}
]

categorias = {}
agotados = set()
bajo = []

for item in inventario:

    cat = item["categoria"]
    prod = item["producto"]
    stock = item["stock"]

    if cat not in categorias:
        categorias[cat] = []

    categorias[cat].append(prod)

    if stock == 0:
        agotados.add(prod)

    if stock < 5:
        bajo.append(prod)

print(categorias)
print(agotados)
print(tuple(bajo))