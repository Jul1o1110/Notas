
datos_estudiantes = {}

def registrar_ingreso():
    nombre = input("Ingresa el nombre del estudiante a registrar: ").strip().title()
    if not nombre:
        print("El nombre del estudiante no puede estar vacío.")
        return

    if nombre not in datos_estudiantes:
        datos_estudiantes[nombre] = []
        print(f"Estudiante '{nombre}' registrado con éxito.")
    else:
        print(f"El estudiante '{nombre}' ya se encuentra registrado.")

def registrar_nota():
    nombre = input("Ingresa el nombre del estudiante: ").strip().title()
    if not nombre or nombre not in datos_estudiantes:
        print(f"Estudiante '{nombre}' no encontrado.")
        return

    while True:
        nota_str = input("Ingresa la nota a registrar (ej: 4.5): ").strip()
        try:
            nota = float(nota_str)
            if 0.0 <= nota <= 5.0:
                datos_estudiantes[nombre].append(nota)
                print(f"Nota {nota:.2f} registrada para '{nombre}'.")
                break
            else:
                print("La nota debe estar entre 0.0 y 5.0.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número para la nota.")

def ver_promedio():
    nombre = input("Ingresa el nombre del estudiante para ver su promedio: ").strip().title()
    if not nombre or nombre not in datos_estudiantes:
        print(f"Estudiante '{nombre}' no encontrado.")
        return

    notas = datos_estudiantes[nombre]
    
    if not notas:
        print(f"El estudiante '{nombre}' aún no tiene notas registradas.")
        return
    
    promedio = sum(notas) / len(notas)
    print(f"Promedio de '{nombre}': {promedio:.2f}")

    if promedio >= 3.0:
        print("ESTUDIANTE APRUEBA (Corte 3.0)")
    else:
        print("ESTUDIANTE NO APRUEBA (Corte 3.0)")
    
    print(f"Notas registradas: {notas}")
