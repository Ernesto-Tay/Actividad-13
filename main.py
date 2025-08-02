estudiantes = {}
def reprobado(notas):
    desaprobacion = False
    for nota in notas:
        if nota < 60:
            desaprobacion = True
            break
    return desaprobacion

def estudiantes_search():
    if not estudiantes:
        print("No hay estudiantes inscritos aún")
    else:
        while True:
            try:
                id_search = int(input("\nIngrese la ID del estudiante: "))
                break
            except ValueError:
                print("Ingrese una ID válida")
            except Exception as e:
                print("Error inesperado: ", e)

        if id_search not in estudiantes.keys():
            print("El estudiante no existe")
            id_search = False
        else:
            return id_search

def estudiantes_exist():
    if not estudiantes:
        print("No hay estudiantes inscritos aún")
        return False
    else:
        return True

def promedio(notas):
    if not notas:
        return 0
    else:
        total = 0
        cant = 0
        for nota in notas:
            total += nota
            cant += 1
        return round(total / cant,2)

while True:
    print("\n\n-------- SISTEMA DE ESTUDIANTES --------\n1. Agregares estudiante\n2. Agregar cursos a un estudiante\n3. Consultar estudiante\n4. Mostrar todos los estudiantes\n5. Salir")
    select = input("Seleccione una opción: ")
    match select:
        case 1:
            while True:
                try:
                    id = int(input("\nIngrese la ID del estudiante (5 dígitos): "))
                    name = input("Ingrese el nombre del estudiante: ")
                    carrera = input("Ingrese la carrera del estudiante: ")
                    cursos = []
                    id_ok = True
                    name_ok = True
                    if id <=0 or len(str(id)) != 5:
                        print("La ID debe ser positiva y de extactamente 5 dígitos")
                        id_ok = False
                    if not name.isalpha():
                        print("El nombre no puede contener números")
                        name_ok = False
                    if id_ok and name_ok:
                        break
                except ValueError:
                    print("Entrada de valores inválida, intente de nuevo")
                except Exception as e:
                    print("Error inesperado: ",e)
            estudiantes[id] = {
                "nombre": name,
                "carrera": carrera,
                "cursos": cursos
            }

        case 2:
            valid = estudiantes_exist()
            if valid:
                id_search = estudiantes_search()
                if id_search:
                    while True:
                        try:
                            name = input("Ingrese el nombre del curso: ")
                            note = int(input("Ingrese la nota del curso: "))
                            if note < 0 or note > 100:
                                print("La nota debe estar entre 0 y 100")
                            else:
                                break
                        except ValueError:
                            print("Ingrese un número entero en la nota")
                        except Exception as e:
                            print("Error inesperado: ",e)
                    estudiante = estudiantes[id_search]
                    curso = {
                        "nombre": name,
                        "nota": note
                    }
                    estudiante['cursos'].append(curso)


        case 3:
            valid = estudiantes_exist()
            if valid:
                id_search = estudiantes_search()
                if id_search:
                    estudiante = estudiantes[id_search]
                    print(f"\n\n----- DATOS DEL ESTUDIANTE -----\nID: {id_search}\nNombre: {estudiante['nombre']}\nCarrera: {estudiante['carrera']}\n----CURSOS-----")
                    notas = []
                    if not estudiante['cursos']:
                        print("El estudiante no tiene cursos")
                    else:
                        for curso in estudiante['cursos']:
                            print(f"\nNombre: {curso['nombre']}")
                            print(f"Nota: {curso['nota']}")
                            notas.append(curso['nota'])

                        prom = promedio(notas)
                        print(f"\nPromedio: {prom}")
                        rep = reprobado(notas)
                        if rep:
                            print("El estudiante ha reprobado")
                        else:
                            print("El estudiante ha aprobado")


        case 4:
            exist = estudiantes_exist()
            if exist:
                print("\n\n--------LISTA DE ESTUDIANTES--------")
                cont = 1
                for id,estudiante in estudiantes.items():
                    print(f"\n-----ESTUDIANTE {cont}-----")
                    cont += 1
                    print(f"ID: {id}")
                    print(f"Nombre: {estudiante['nombre']}")
                    print(f"Nota: {estudiante['nota']}")
                    print(f"Carrera: {estudiante['carrera']}")
                    print("Cursos: ")
                    for curso in estudiante['cursos']:
                        print(f"   Nombre: {curso['nombre']}")
                        print(f"   Nota: {curso['nota']}")

        case 5:
            print("Saliendo...")
            break
