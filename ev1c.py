import datetime

def main():
    Clientes = {}
    Salas = {}
    Reservaciones = {}

    clave_cliente = 1
    clave_sala = 1
    No_folio = 1

    TURNOS = ["Mañana", "Tarde", "Noche"]

    # Cliente y sala pre-registrados
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
        opcion = input("Opción: ").strip()

        if opcion == "1":
            if not Clientes:
                print("No tiene agendado ninguna reserva.")
                continue

            # Mostrar clientes
            clientes_ordenados = sorted(Clientes.items(), key=lambda x: (x[1][1], x[1][0]))
            print("\n--- Clientes Registrados ---")
            for clave, (nombre, apellido) in clientes_ordenados:
                print(f"Clave: {clave} - {apellido}, {nombre}")

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
                fecha_reservacion_dt = datetime.datetime.strptime(fecha_reservacion, "%d/%m/%Y").date()
                if (fecha_reservacion_dt - datetime.date.today()).days < 2:
                    print("Las reservaciones solo se pueden hacer con al menos 2 días de anticipación.")
                    continue
            except ValueError:
                print("La fecha ingresada no es válida.")
                continue

            # Mostrar salas disponibles con cupo
            print("\n--- Salas disponibles ---")
            disponibles = False
            for clave, (nombre_sala, cupo) in Salas.items():
                if cupo > 0:
                    print(f"Clave: {clave} - {nombre_sala} (Cupo: {cupo})")
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

            turno_reservacion = input("Ingrese el turno de la reservación (Mañana, Tarde, Noche): ").strip().capitalize()
            if turno_reservacion not in TURNOS:
                print("El turno ingresado no es válido.")
                continue

            existe_turno = False
            for reserva in Reservaciones.values():
                sala_res, nombre_evento_res, turno_res, fecha_res = reserva
                if sala_res == clave_sala_input and turno_res == turno_reservacion and fecha_res == fecha_reservacion:
                    existe_turno = True
                    break
            if existe_turno:
                print(f"La sala ya está reservada para el turno {turno_reservacion} en esa fecha.")
                continue

            nombre_evento = input("Ingrese el nombre del evento: ").strip()
            if nombre_evento == "" or not nombre_evento.replace(" ", "").isalpha():
                print("El nombre del evento no puede estar vacío ni contener números.")
                continue

            Reservaciones[No_folio] = (clave_sala_input, nombre_evento, turno_reservacion, fecha_reservacion)
            print(f"Reservación guardada con éxito. Su número de folio es: {No_folio}")
            No_folio += 1

            nombre_sala, cupo_sala = Salas[clave_sala_input]
            Salas[clave_sala_input] = (nombre_sala, cupo_sala - 1)

        elif opcion == "2":
            if not Reservaciones:
                print("No hay reservaciones para editar.")
                continue

            try:
                fecha_inicio = input("Ingrese la fecha de inicio (DD/MM/YYYY): ")
                fecha_fin = input("Ingrese la fecha de fin (DD/MM/YYYY): ")
                f_inicio = datetime.datetime.strptime(fecha_inicio, "%d/%m/%Y").date()
                f_fin = datetime.datetime.strptime(fecha_fin, "%d/%m/%Y").date()
                if f_fin < f_inicio:
                    print("La fecha de fin no puede ser anterior a la de inicio.")
                    continue
            except ValueError:
                print("Formato de fecha inválido.")
                continue

            print(f"\n--- Reservaciones entre {fecha_inicio} y {fecha_fin} ---")
            reservaciones_en_rango = []
            for folio, (clave_sala_res, nombre_evento_res, turno_res, fecha_res) in Reservaciones.items():
                fecha_dt = datetime.datetime.strptime(fecha_res, "%d/%m/%Y").date() if isinstance(fecha_res, str) else fecha_res
                if f_inicio <= fecha_dt <= f_fin:
                    print(f"Folio: {folio} - Evento: {nombre_evento_res} - Fecha: {fecha_res} - Turno: {turno_res}")
                    reservaciones_en_rango.append(folio)

            if not reservaciones_en_rango:
                print("No hay reservaciones en ese rango.")
                continue

            try:
                folio_a_editar = int(input("Ingrese el folio de la reservación a editar: "))
            except ValueError:
                print("El folio ingresado no es válido.")
                continue

            if folio_a_editar not in Reservaciones:
                print("Folio no encontrado.")
                continue

            nuevo_nombre = input("Ingrese el nuevo nombre del evento: ").strip()
            if nuevo_nombre == "" or not nuevo_nombre.replace(" ", "").isalpha():
                print("El nombre no puede estar vacío ni contener números.")
                continue

            # Actualizar nombre evento
            clave_sala_res, _, turno_res, fecha_res = Reservaciones[folio_a_editar]
            Reservaciones[folio_a_editar] = (clave_sala_res, nuevo_nombre, turno_res, fecha_res)
            print("Evento actualizado correctamente.")

        elif opcion == "3":
            if not Reservaciones:
                print("No hay reservaciones registradas.")
                continue

            try:
                fecha_consulta = input("Ingrese la fecha a consultar (DD/MM/YYYY): ")
                fecha_consulta_dt = datetime.datetime.strptime(fecha_consulta, "%d/%m/%Y").date()
            except ValueError:
                print("Fecha inválida.")
                continue

            print(f"\n--- Reservaciones para {fecha_consulta} ---")
            encontradas = False
            for folio, (clave_sala_res, nombre_evento_res, turno_res, fecha_res) in Reservaciones.items():
                fecha_dt = datetime.datetime.strptime(fecha_res, "%d/%m/%Y").date() if isinstance(fecha_res, str) else fecha_res
                if fecha_dt == fecha_consulta_dt:
                    cliente_nombre = "Desconocido"
                    sala_nombre = "Desconocida"
                    if clave_sala_res in Salas:
                        sala_nombre = Salas[clave_sala_res][0]

                    print(f"Folio: {folio} - Sala: {sala_nombre} - Evento: {nombre_evento_res} - Turno: {turno_res}")
                    encontradas = True

            if not encontradas:
                print("No hay reservaciones para esa fecha.")

        elif opcion == "4":
            try:
                nombre = input("Ingrese el nombre del cliente: ").strip()
                if nombre == "" or not nombre.replace(" ", "").isalpha():
                    print("El nombre no puede estar vacío ni contener números.")
                    continue

                apellido = input("Ingrese los apellidos del cliente: ").strip()
                if apellido == "" or not apellido.replace(" ", "").isalpha():
                    print("Los apellidos no pueden estar vacíos ni contener números.")
                    continue

                Clientes[clave_cliente] = [nombre, apellido]
                print(f"Cliente guardado con éxito. Clave asignada: {clave_cliente}")
                clave_cliente += 1
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "5":
            try:
                nombre_sala = input("Ingrese el nombre de la sala: ").strip()
                if nombre_sala == "" or not nombre_sala.replace(" ", "").isalpha():
                    print("El nombre de la sala no puede estar vacío ni contener números.")
                    continue

                cupo = input("Ingrese el cupo de la sala: ").strip()
                if not cupo.isdigit() or int(cupo) <= 0:
                    print("El cupo debe ser un número entero mayor que cero.")
                    continue

                cupo = int(cupo)
                Salas[clave_sala] = [nombre_sala, cupo]
                print(f"Sala registrada con éxito. Clave asignada: {clave_sala}")
                clave_sala += 1
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "6":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "_main_":
    main()