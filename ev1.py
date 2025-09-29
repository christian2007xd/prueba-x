import datetime

def main():
    Clientes = {}
    Salas = {}
    Reservaciones = {}
    
    clave_cliente = 1
    clave_sala = 1
    No_folio = 1
    
    TURNOS = ["Mañana", "Tarde", "Noche"]
    
    Clientes[clave_cliente] = ["Ana", "García López"]
    clave_cliente += 1  
    
    Salas[clave_sala] = ["Auditorio Principal", 150]
    clave_sala += 1
    
    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar reservación")
        print("2. Editar nombre del evento")
        print("3. Consultar reservaciones")
        print("4. Registrar cliente")
        print("5. Registrar sala")
        print("6. Salir")
        opcion = input("Opción: ")
        
        if opcion == "4":
                try:
                    Nombre = input("Ingrese el nombre del cliente: ").strip()
                    if Nombre == "" or not Nombre.replace(" ", "").isalpha():
                        raise Exception("El nombre no puede estar vacío ni contener números")
                    
                    Apellido = input("Ingrese los apellidos del cliente: ").strip()
                    if Apellido == "" or not Apellido.replace(" ", "").isalpha():
                        raise Exception("Los apellidos no pueden estar vacíos ni contener números")
                    
                    Clientes[clave_cliente] = (Nombre, Apellido)
                    print(f"Cliente guardado con éxito. Clave asignada: {clave_cliente}")
                    clave_cliente += 1
                    
                except Exception as e:
                    print("Error:", e)
        elif opcion == "1":
            if not Clientes:
                print("No tiene agendado ningúna reserva.")
            else:
                clientes_ordenados = sorted(Clientes.items(), key=lambda x: (x[1][1], x[1][0]))
                for clave, (Nombre, Apellido) in clientes_ordenados:
                    print("-" * 50)
                    print(f"{'Clave':<10}{'Apellido':<20}{'Nombre':<15}")
                    print(f"{clave:<10}{Apellido:<20}{Nombre:<15}")
                    print("-" * 50)
                
                try:
                    clave_cliente_input = int(input("Ingrese la clave del cliente: "))
                except ValueError:
                    print("La clave ingresada no es válida, debe ser un número.")
                    continue
                
                if clave_cliente_input not in Clientes:
                    print("Esa clave no existe en la agenda.")
                    continue
                
                try:
                    fecha_reservacion = input("Ingrese la fecha de la reservación (DD/MM/YYYY): ")
                    fecha_reservacion = datetime.datetime.strptime(fecha_reservacion, "%d/%m/%Y").date()
                    fecha_actual = datetime.date.today()
                    
                    if (fecha_reservacion - fecha_actual).days < 2:
                        print("Las reservaciones solo se pueden hacer 2 días después de la fecha actual.")
                        continue
                except ValueError:
                    print("La fecha ingresada no es válida.")
                    continue
                
                print("******** Salas disponibles ********")
                print(f"{'Clave':<10}{'Nombre':<30}{'Cupo':<8}")
                disponibles = False
                for clave, (nombre, cupo) in Salas.items():
                    if cupo > 0:
                        print(f"{clave:<10}{nombre:<30}{cupo:<8}")
                        disponibles = True
                
                if not disponibles:
                    print("No hay salas disponibles con cupo.")
                    continue
                
                try:
                    clave_sala_input = int(input("Ingrese la clave de la sala: "))
                except ValueError:
                    print("La clave ingresada no es válida, debe ser un número.")
                    continue
                
                if clave_sala_input not in Salas:
                    print("Esa sala no existe.")
                    continue
                if Salas[clave_sala_input][1] <= 0:
                    print("Esta sala no tiene cupo disponible.")
                    continue
                
                # Turno
                turno_reservacion = input("Ingrese el turno de la reservación (Mañana, Tarde, Noche): ").strip()
                if turno_reservacion not in TURNOS:
                    print("El turno ingresado no es válido.")
                    continue
                
                # Nombre del evento
                Nombre_evento = input("Ingrese el nombre del evento: ").strip()
                if Nombre_evento == "" or not Nombre_evento.replace(" ", "").isalpha():
                    print("El nombre del evento no puede estar vacío ni contener números")
                    continue
                
                Reservaciones[No_folio] = (clave_sala_input, Nombre_evento, turno_reservacion,)
                print(f"Reservación guardada con éxito. Su número de folio es: {No_folio}")
                No_folio += 1
                
                nombre_sala, cupo_sala = Salas[clave_sala_input]
                Salas[clave_sala_input] = (nombre_sala, cupo_sala - 1)
                
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "5":
            try:
                nombre_sala = input("Ingresa el nombre de la sala: ")
                if nombre_sala == "" or not nombre_sala.replace(" ", "").isalpha():
                    raise Exception("El nombre de la sala no puede estar vacío ni contener números")
            except Exception as e:
                print(f"Error: {e}")
                continue

            try:
                cupo_sala =  input("Ingrese el cupo de la sala: ").strip()
                if not cupo_sala.isdigit():
                    raise Exception("El cupo debe ser un número entero .")
                cupo_sala = int(cupo_sala)
                if cupo_sala <= 0:
                    raise Exception("El cupo debe ser mayor que cero.")
                
                Salas[clave_sala] = (nombre_sala, cupo_sala)
                print(f"Sala registrada con éxito. Clave asignada: {clave_sala}")
                clave_sala += 1
            except Exception as e:
                print(f"Error: {e}")
                continue
        elif opcion == "6":
            break

if __name__ == "__main__":
    main()