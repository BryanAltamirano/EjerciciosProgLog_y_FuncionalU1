asistencias = [
("Ecuaciones Diferenciales", "Bryan", "2024-09-01"),
("Aplicaciones web", "Gaby", "2024-09-01"),
("Taller de investigación 2", "Eder", "2024-09-01"),
("Programación logica y funcional", "Cristian", "2024-09-02"),
("Física", "Ana", "2024-09-02")
]

materias = {}
dias = {}

for m, a, f in asistencias:

    if m not in materias:
        materias[m] = set()
    materias[m].add(a)

    if a not in dias:
        dias[a] = set()
    dias[a].add(f)

mayor = ""
maximo = 0

for a in dias:
    if len(dias[a]) > maximo:
        maximo = len(dias[a])
        mayor = a

print(materias)
print({a: len(dias[a]) for a in dias})
print("Mayor asistencia:", mayor)
