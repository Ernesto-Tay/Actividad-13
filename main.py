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
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            print("Saliendo...")
            break
