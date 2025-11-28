
from logica import registrar_ingreso, registrar_nota, ver_promedio

def mostrar_menu():
    print("\n" + "="*40)
    print("      SISTEMA DE GESTIÓN DE NOTAS")
    print("="*40)
    print("1. Registrar Estudiante")
    print("2. Registrar Nota")
    print("3. Ver Promedio y Estado")
    print("4. Salir")
    print("-" * 40)

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ").strip()

        if opcion == '1':
            registrar_ingreso()
        
        elif opcion == '2':
            registrar_nota()
        
        elif opcion == '3':
            ver_promedio()
                
        elif opcion == '4':
            print("\nSaliendo de la aplicación. ¡Hasta luego!")
            break
            
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 4.")

if __name__ == "__main__":
    main()