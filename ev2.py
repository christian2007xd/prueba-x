import datetime
import random

def main():
    Clientes = {}
    Salas = {}
    Reservaciones = {}

    TURNOS = ["Matutino", "Vespertino", "Nocturno"]

    clave_cliente = f"C{random.randint(1, 999):03d}"
    while clave_cliente in Clientes:
        clave_cliente = f"C{random.randint(1, 999):03d}"
    Clientes[clave_cliente] = ("Pablo", "García López")

    clave_sala = f"S{random.randint(1, 999):03d}"
    while clave_sala in Salas:
        clave_sala = f"S{random.randint(1, 999):03d}"
    Salas[clave_sala] = ("Auditorio Principal", 150)


    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar reservación")
        print("2. Editar nombre del evento")
        print("3. Consultar reservaciones")
        print("4. Registrar cliente")
        print("5. Registrar sala")
        print("6. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            if not Clientes:
                print("No hay clientes registrados.")
                continue

            while True:
                try:
                    clientes_ordenados = sorted(Clientes.items(), key=lambda x: (x[1][1], x[1][0]))
                    print("\n--- Clientes Registrados ---")
                    print(f"{'Clave':<10}{'Apellido':<20}{'Nombre':<15}")
                    for clave, (nombre, apellido) in clientes_ordenados:
                        print(f"{clave:<10}{apellido:<20}{nombre:<15}")

                    clave_cliente_input = input("Ingrese la clave del cliente o escriba 'CANCELAR' para salir: ").strip().upper()
                    if clave_cliente_input == "CANCELAR":
                        print("Operación cancelada. Regresando al menú principal.")
                        break
                    if clave_cliente_input not in Clientes:
                        print("La clave ingresada no existe. Intente de nuevo o escriba 'CANCELAR' para salir.")
                        continue
                    break
                except Exception as e:
                    print(f"Error: {e}")
            if clave_cliente_input == "CANCELAR":
                continue

            while True:
                fecha_reservacion = input("Ingrese la fecha de la reservación (DD/MM/YYYY) o 'CANCELAR' para salir: ").strip()
                if fecha_reservacion.upper() == "CANCELAR":
                    print("Operación cancelada. Regresando al menú principal.")
                    break
                try:
                    fecha_dt = datetime.datetime.strptime(fecha_reservacion, "%d/%m/%Y").date()
                    if (fecha_dt - datetime.date.today()).days < 2:
                        print("La reservación debe ser al menos con 2 días de anticipación.")
                        continue
                    break
                except ValueError:
                    print("Formato de fecha inválido. Intente de nuevo.")

            if fecha_reservacion.upper() == "CANCELAR":
                continue

            if not Salas:
                print("No hay salas registradas.")
                continue

            print("\n--- Salas Disponibles ---")
            print(f"{'Clave':<10}{'Nombre':<30}{'Cupo':<8}")
            for clave, (nombre, cupo) in Salas.items():
                print(f"{clave:<10}{nombre:<30}{cupo:<8}")

            while True:
                try: 
                    clave_sala_input = input("Ingrese la clave de la sala o 'CANCELAR' para salir: ").strip().upper()
                    if clave_sala_input == "CANCELAR":
                        print("Operación cancelada. Regresando al menú principal.")
                        break
                    if clave_sala_input not in Salas:
                        print("La clave ingresada no existe. Intente de nuevo.")
                        continue
                    break
                except Exception as e:
                    print(f"Error: {e}")
                
            if clave_sala_input == "CANCELAR":
                continue
            try:
                turnos_ocupados = [r[3] for r in Reservaciones.values() if r[1] == clave_sala_input and r[4] == fecha_dt.strftime("%d/%m/%Y")]
                if len(turnos_ocupados) >= 3:
                    print("Esa sala ya tiene los 3 turnos ocupados para esa fecha.")
                    continue
            except Exception as e:
                print(f"Error: {e}")
                continue
            
            while True:
                try:
                    turno = input("Ingrese el turno (Matutino, Vespertino, Nocturno) o 'CANCELAR' para salir: ").strip().capitalize()
                    if turno.upper() == "CANCELAR":
                        print("Operación cancelada. Regresando al menú principal.")
                        break
                    if turno not in TURNOS:
                        print("Turno inválido. Intente de nuevo.")
                        continue
                    if turno in turnos_ocupados:
                        print(f"La sala ya está reservada en el turno {turno} para esa fecha.")
                        continue
                    break
                except Exception as e:
                    print(f"Error: {e}")
                    
            if turno.upper() == "CANCELAR":
                continue

            while True:
                try: 
                    nombre_evento = input("Ingrese el nombre del evento o 'CANCELAR' para salir: ").strip()
                    if nombre_evento.upper() == "CANCELAR":
                        print("Operación cancelada. Regresando al menú principal.")
                        break
                    if not nombre_evento.replace(" ", "").isalpha():
                        raise ValueError("El nombre del evento no puede estar vacío ni contener números.")
                    break
                except ValueError as e:
                    print(f"Error: {e}")

            if nombre_evento.upper() == "CANCELAR":
                continue

            folio = f"R{random.randint(1, 999):03d}"
            while folio in Reservaciones:
                folio = f"R{random.randint(1, 999):03d}"
            evento_duplicado = any(
                r[1] == clave_sala_input and
                r[4] == fecha_dt.strftime("%d/%m/%Y") and
                r[3] == turno and
                r[2].lower() == nombre_evento.lower()
                for r in Reservaciones.values()
            )
            if evento_duplicado:
                print("Ya existe un evento con ese nombre en la misma sala, fecha y turno.")
                continue
            Reservaciones[folio] = (
                clave_cliente_input,
                clave_sala_input,
                nombre_evento,
                turno,
                fecha_dt.strftime("%d/%m/%Y")
            )
            print(f"Reservación registrada con éxito. Folio: {folio}")

        elif opcion == "2":
            print("\n--- Editar Nombre del Evento ---")
            try:
                fecha_inicio = input("Ingrese la fecha de inicio (DD/MM/YYYY): ").strip()
                fecha_fin = input("Ingrese la fecha de fin (DD/MM/YYYY): ").strip()
                f_inicio = datetime.datetime.strptime(fecha_inicio, "%d/%m/%Y").date()
                f_fin = datetime.datetime.strptime(fecha_fin, "%d/%m/%Y").date()
                if f_fin < f_inicio:
                    raise Exception("La fecha de fin no puede ser anterior a la de inicio.")
            except ValueError:
                print("Formato de fecha inválido.")
                continue
            except Exception as e:
                print(f"Error: {e}")
                continue

            print(f"\n--- Reservaciones entre {fecha_inicio} y {fecha_fin} ---")
            print(f"{'Folio':<8}{'Fecha':<12}{'Turno':<10}{'Evento':<25}{'Sala':<25}{'Cliente':<25}")
            print("-" * 105)

            encontradas = []
            for folio, (cli, sala, evento, turno, fecha_str) in Reservaciones.items():
                try:
                    fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y").date()
                    if f_inicio <= fecha <= f_fin:
                        cliente_nombre = f"{Clientes[cli][1]} {Clientes[cli][0]}" if cli in Clientes else "Desconocido"
                        sala_nombre = Salas[sala][0] if sala in Salas else "Desconocida"
                        print(f"{folio:<8}{fecha_str:<12}{turno:<10}{evento:<25}{sala_nombre:<25}{cliente_nombre:<25}")
                        encontradas.append(folio)
                except Exception as e:  
                    print(f"Error al mostrar la reservación {folio}: {e}")
            if not encontradas:
                print("No hay reservaciones en ese rango.")
                continue

            folio_a_editar = input("Ingrese el folio a editar: ").strip().upper()
            if folio_a_editar not in Reservaciones:
                print("Folio no encontrado.")
                continue

            try:
                nuevo_nombre = input("Ingrese el nuevo nombre del evento: ").strip()
                if not nuevo_nombre.replace(" ", "").isalpha():
                    raise Exception("El nombre no puede estar vacío ni contener números.")
            except Exception as e:
                print(f"Error: {e}")
                continue

            datos = list(Reservaciones[folio_a_editar])
            datos[2] = nuevo_nombre
            Reservaciones[folio_a_editar] = tuple(datos)
            print("Evento actualizado correctamente.")

        elif opcion == "3":
            print("\n--- Consultar Reservaciones por Fecha ---")
            try:
                fecha_consulta = input("Ingrese la fecha a consultar (DD/MM/YYYY): ").strip()
                fecha_obj = datetime.datetime.strptime(fecha_consulta, "%d/%m/%Y").date()
            except ValueError:
                print("Formato de fecha inválido.")
                continue

            print(f"\n--- Reporte de Reservaciones ({fecha_obj.strftime('%d/%m/%Y')}) ---")
            print(f"{'Folio':<8}{'Turno':<20}{'Cliente':<30}{'Sala':<25}{'Evento':<20}")
            print("-" * 90)

            encontrados = False
            for folio, (cli, sala, evento, turno, fecha_str) in Reservaciones.items():
                try: 
                    fecha_res = datetime.datetime.strptime(fecha_str, "%d/%m/%Y").date()
                    if fecha_res == fecha_obj:
                        cliente_nombre = f"{Clientes[cli][1]} {Clientes[cli][0]}" if cli in Clientes else "Desconocido"
                        sala_nombre = Salas[sala][0] if sala in Salas else "Desconocida"
                        print(f"{folio:<8}{turno:<20}{cliente_nombre:<30}{sala_nombre:<25}{evento:<20}")
                        encontrados = True
                except Exception as e:
                    print(f"Error al mostrar la reservación {folio}: {e}")  
            if not encontrados:
                print("No hay reservaciones para esta fecha.")

        elif opcion == "4":
            print("\n--- Registrar Nuevo Cliente ---")
            try:
                nombre = input("Nombre del cliente: ").strip()
                apellido = input("Apellido del cliente: ").strip()
                if not nombre or not apellido:
                    raise Exception("Nombre y apellido no pueden estar vacíos.")
                if not nombre.isalpha() or not apellido.replace(" ", "").isalpha():
                    raise Exception("Nombre y apellido solo deben contener letras.")
                clave = f"C{random.randint(1, 999):03d}"
                while clave in Clientes:
                    clave = f"C{random.randint(1, 999):03d}"
                Clientes[clave] = (nombre, apellido)
                print(f"Cliente registrado con clave: {clave}")

            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "5":
            print("\n--- Registrar Nueva Sala ---")
            try:
                nombre = input("Nombre de la sala: ").strip()
                if not nombre:
                    raise Exception("El nombre de la sala no puede estar vacío.")
                cupo = int(input("Cupo de la sala: "))
                if cupo <= 0:
                    raise Exception("El cupo debe ser un número positivo.")
                clave = f"S{random.randint(1, 999):03d}"
                while clave in Salas:
                    clave = f"S{random.randint(1, 999):03d}"
                Salas[clave] = (nombre, cupo)
                print(f"Sala registrada con clave: {clave}")

            except ValueError:
                print("Cupo debe ser un número entero.")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "6":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "_main_":
    main()