ventas = [
("Ana", "Enero", "Laptop", 2, 15000),
("Luis", "Enero", "Mouse", 10, 250),
("Ana", "Febrero", "Laptop", 1, 15000),
("Luis", "Febrero", "Teclado", 5, 800),
("Ana", "Enero", "Mouse", 3, 250)
]

ingresos_empleado = {}
productos = set()
ingresos_mes = {}

for v in ventas:
    empleado, mes, producto, cantidad, precio = v
    total = cantidad * precio

    productos.add(producto)

    if empleado in ingresos_empleado:
        ingresos_empleado[empleado] += total
    else:
        ingresos_empleado[empleado] = total

    if mes in ingresos_mes:
        ingresos_mes[mes] += total
    else:
        ingresos_mes[mes] = total

mayor = ""
maximo = 0
for e in ingresos_empleado:
    if ingresos_empleado[e] > maximo:
        maximo = ingresos_empleado[e]
        mayor = e

print(ingresos_empleado)
print(productos)
print(ingresos_mes)
print("Mayor ingreso:", mayor)