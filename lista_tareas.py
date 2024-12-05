tareas=["estudiar","leer","nadar","cocinar","dormir"]

def listar_tareas():
    if not tareas:
        print("No hay tareas pendientes")

    else:
        print("Lista de tareas:")
        for i, tarea in enumerate(tareas,1):
            print(f"{i}. {tarea}")

def eliminar_tarea():
    listar_tareas()
    try:
        index= int(input("Selecciona el numero de la tarea a eliminar"))-1
        if 0<=index<len(tareas):
            tarea_eliminada= tareas.pop(index)
            print(f"Tarea '{tarea_eliminada}' eliminada")
        else:
            print("Numero de tarea no valido")
    except ValueError:
        print("Entrada no valida")

if __name__ == "__main__":
    print("Bienvenidos a la aplicacion de lista de tareas")
    while True:
        print("\n1. Listar tareas")
        print("2. eliminar tarea")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            listar_tareas()
        elif opcion == "2":
            eliminar_tarea()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")