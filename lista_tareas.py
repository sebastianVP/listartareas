tareas=["estudiar","leer","nadar","cocinar","dormir"]

def listar_tareas():
    if not tareas:
        print("No hay tareas pendientes")

    else:
        print("Lista de tareas:")
        for i, tarea in enumerate(tareas,1):
            print(f"{i}. {tarea}")

if __name__ == "__main__":
    print("Bienvenidos a la aplicacion de lista de tareas")
    listar_tareas()