import psutil

# el while true es "un bucle que envuelve el código principal"

while True:
    print("Menú de opciones:")
    print("1. Mostrar procesos")
    print("2. Terminar un proceso")
    print("0. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":

        # Creo un boolean para saber si el notepad esta en ejecución, porque no me deja imprimir dentro del for

        blocEjecutando = False

        # este for esta sacado de la documentación de la librería psutil https://psutil.readthedocs.io/en/latest/ procesos > funciones (primer ejemplo)
        # el if es para comprobar el bloc, pongo true si esta ejecutando para sacar el print fuera del for (preguntar por que no me deja meter el print dentro)

        for proc in psutil.process_iter(['pid', 'name', 'username']):
            print(proc.info['name'], '//', proc.info['pid'])
            if proc.info['name'] == 'Notepad.exe':
                blocEjecutando = True
        print("")

        if blocEjecutando:
            print("El Bloc de Notas está en ejecución")
        print("")

    elif opcion == "2":

        # almacenamos la entrada del usuario en PIDUsuario

        print("Ingresa el PID del proceso que deseas terminar: ")
        PIDUsuario = input()
        print("")

        # el try except es para el control de errores, los errores son de una IA
        # la primera linea sirve para convertir el PIDUsuario a int para poder leer bien el PID
        # la variable proceso sirve para leer el PIDUsuario y luego terminarlo

        try:
            PIDUsuario = int(PIDUsuario)
            proceso = psutil.Process(PIDUsuario)
            proceso.terminate()
            print("El proceso con PID", PIDUsuario, "ha sido terminado.")
        except psutil.NoSuchProcess:
            print("No se encontró ningún proceso con el PID", PIDUsuario)
        except psutil.AccessDenied:
            print(f"No tienes permisos para terminar el proceso con PID", PIDUsuario)
        except ValueError:
            print("Ingresa un número válido para el PID.")
        except Exception as e:
            print("Error al intentar terminar el proceso: {e}")

    elif opcion == "0":
        print("Has salido del programa")

        # el break es para cerrar el programa (preguntar si hay una opcion mas eficiente)

        break

    else:
        print("Selecciona una opción correcta")