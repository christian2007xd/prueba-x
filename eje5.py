import sys

datos_usuario = {}
clave_unica = 1

while True:
    print("\n*** Menú de opciones ***")
    print("A. agregar")
    print("B. consultar")
    print("X. Salir")
    opcion = input("Seleccione una opción: ").strip().lower()

    try:
        if opcion == "a":
            Nombre = input("Ingrese el nombre del usuario: ")
            Apellido = input("Ingrese los apellidos del usuario: ")
            
            try:
                Antiguedad = int(input("Ingrese la antigüedad del usuario (número): "))
            except ValueError:
                print("⚠ El valor ingresado para antigüedad no es un número válido.")
                continue
            except Exception:
                print(f"Ocurrió un problema {sys.exc_info()[0]}")
                for elem in sys.exc_info():
                    print(elem)
                continue
            else:
                print("La antigüedad fue ingresada correctamente.")
                
            datos_usuario[clave_unica] = (Nombre, Apellido, Antiguedad)
            print(f"✅ Usuario guardado con éxito. Clave asignada: {clave_unica}")
            clave_unica += 1

        elif opcion == "b":
            if not datos_usuario:
                print("⚠ Todavía no hay registros en la agenda.")
            else:
                try:
                    clave_consulta = int(input("Ingrese la clave del usuario a consultar: "))
                    datos = datos_usuario[clave_consulta]
                except ValueError:
                    print("⚠ La clave ingresada no es válida, debe ser un número.")
                    continue
                except KeyError:
                    print("⚠ Esa clave no existe en la agenda.")
                    continue
                except Exception:
                    print(f"Ocurrió un problema {sys.exc_info()[0]}")
                    for elem in sys.exc_info():
                        print(elem)
                    continue
                else:
                    print("\n--- Datos del usuario ---")
                    print(f"Clave: {clave_consulta}")
                    print(f"Nombre: {datos[0]}")
                    print(f"Apellido: {datos[1]}")
                    print(f"Antigüedad: {datos[2]} años")
                    
        elif opcion == "x":
            print("👋 Fin del programa.")
            break
        
        else:
            print("⚠ Opción no válida, intenta de nuevo.")
            
    except Exception:
        print(f"Ocurrió un problema {sys.exc_info()[0]}")
        for elem in sys.exc_info():
            print(elem)
            
