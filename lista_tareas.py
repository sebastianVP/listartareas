tareas=["estudiar","leer","nadar","cocinar","dormir"]

def listar_tareas():
    if not tareas:
        print("No hay tareas pendientes")

    else:
        print("Lista de tareas:")
        for i, tarea in enumerate(tareas,1):
            print(f"{i}. {tarea}")

def agregar_tarea():
    tarea = input("Escribe una nueva tarea:")
    tareas.append(tarea)
    print(f"Tarea '{tarea}' añadidad exitosamente ")


if __name__ == "__main__":
    print("Bienvenidos a la aplicacion de lista de tareas")
    while True:
        print("\n1. Listar tareas")
        print("2. Agregar tarea")
        print("3. Salir")
        opcion = input("Selecciona una opcion:  ")
        if opcion=="1":
            listar_tareas()
        elif opcion=="2":
            agregar_tarea()
        elif opcion=="3":
            print("Salud, hasta luego!")
            break
        else:
            print("Opción no valida")