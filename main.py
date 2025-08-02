estudiantes = {}
def aprobado(nota):
    aprobacion = False
    if nota >=60:
        aprobacion = True
    return aprobacion

def promedio(notas):
    if not notas:
        return 0
    else:
        total = 0
        cant = 0
        for nota in notas:
            total += nota
            cant += 1
        return total / cant

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
                    cursos = {}
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
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            print("Saliendo...")
            break
