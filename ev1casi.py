import datetime

def main():
    Clientes = {}
    Salas = {}
    Reservaciones = {}

    cliente_id = 1
    sala_id = 1
    reserva_id = 1

    TURNOS = ["Mañana", "Tarde", "Noche"]

    # Datos iniciales
    Clientes[1] = ["Ana", "García López"]
    Clientes[2] = ["Luis", "Pérez Martínez"]
    cliente_id = 3

    Salas[1] = ["Auditorio Principal", 150]
    Salas[2] = ["Sala de Juntas B", 20]
    sala_id = 3

    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar reservación")
        print("2. Editar nombre del evento")
        print("3. Consultar reservaciones")
        print("4. Registrar cliente")
        print("5. Registrar sala")
        print("6. Salir")
        opcion = input("Opción: ")

        # -------------------- Registrar cliente --------------------
        if opcion == "4":
            try:
                nombre = input("Nombre: ").strip()
                if nombre == "":
                    raise ValueError("Nombre vacío")
                apellidos = input("Apellidos: ").strip()
                if apellidos == "":
                    raise ValueError("Apellidos vacíos")
                Clientes[cliente_id] = [nombre, apellidos]
                print("Cliente registrado con ID", cliente_id)
                cliente_id += 1
            except Exception as e:
                print("Error:", e)

        # -------------------- Registrar sala --------------------
        elif opcion == "5":
            try:
                nombre = input("Nombre de la sala: ").strip()
                if nombre == "":
                    raise ValueError("Nombre vacío")
                cupo = int(input("Cupo: "))
                if cupo <= 0:
                    raise ValueError("Cupo inválido")
                Salas[sala_id] = [nombre, cupo]
                print("Sala registrada con ID", sala_id)
                sala_id += 1
            except Exception as e:
                print("Error:", e)

        # -------------------- Registrar reservación --------------------
        elif opcion == "1":
            try:
                if len(Clientes) == 0 or len(Salas) == 0:
                    raise ValueError("Se necesitan clientes y salas registradas")

                print("Clientes:")
                for cid in Clientes:
                    print(cid, ":", Clientes[cid][1], ",", Clientes[cid][0])
                c_id = int(input("ID cliente: "))
                if c_id not in Clientes:
                    raise ValueError("Cliente no existe")

                fecha_str = input("Fecha (DD/MM/YYYY): ")
                dia, mes, anio = fecha_str.split("/")
                fecha = datetime.date(int(anio), int(mes), int(dia))
                if fecha < datetime.date.today() + datetime.timedelta(days=2):
                    raise ValueError("La fecha debe ser al menos dos días después de hoy")

                # Salas disponibles
                disponibles = {}
                for sid in Salas:
                    ocupados = []
                    for r in Reservaciones:
                        if Reservaciones[r][1] == sid and Reservaciones[r][2] == fecha:
                            ocupados.append(Reservaciones[r][3])
                    libres = []
                    for t in TURNOS:
                        if t not in ocupados:
                            libres.append(t)
                    if len(libres) > 0:
                        disponibles[sid] = libres
                        print(sid, ":", Salas[sid][0], "(Cupo:", Salas[sid][1], ") Turnos libres:", libres)

                if len(disponibles) == 0:
                    raise ValueError("No hay salas disponibles")

                s_id = int(input("ID sala: "))
                if s_id not in disponibles:
                    raise ValueError("Sala no disponible")

                turno = input("Turno (" + "/".join(disponibles[s_id]) + "): ").capitalize()
                if turno not in disponibles[s_id]:
                    raise ValueError("Turno no disponible")

                nombre_evento = input("Nombre del evento: ").strip()
                if nombre_evento == "":
                    raise ValueError("Nombre inválido")

                Reservaciones[reserva_id] = [c_id, s_id, fecha, turno, nombre_evento]
                print("Reservación registrada con folio", reserva_id)
                reserva_id += 1

            except Exception as e:
                print("Error:", e)

        # -------------------- Editar nombre del evento --------------------
        elif opcion == "2":
            try:
                if len(Reservaciones) == 0:
                    raise ValueError("No hay reservaciones")

                fecha_ini = input("Fecha inicio (DD/MM/YYYY): ")
                fecha_fin = input("Fecha fin (DD/MM/YYYY): ")
                di, me, ai = fecha_ini.split("/")
                df, mf, af = fecha_fin.split("/")
                f_ini = datetime.date(int(ai), int(me), int(di))
                f_fin = datetime.date(int(af), int(mf), int(df))

                print("FOLIO | FECHA | EVENTO")
                eventos = {}
                for folio in Reservaciones:
                    r = Reservaciones[folio]
                    if f_ini <= r[2] <= f_fin:
                        eventos[folio] = r
                        print(folio, "|", r[2], "|", r[4])

                if len(eventos) == 0:
                    raise ValueError("No hay eventos en ese rango")

                folio_mod = int(input("Folio a modificar: "))
                if folio_mod not in eventos:
                    raise ValueError("Folio no válido")

                nuevo_nombre = input("Nuevo nombre del evento: ").strip()
                if nuevo_nombre == "":
                    raise ValueError("Nombre inválido")

                r = Reservaciones[folio_mod]
                Reservaciones[folio_mod] = [r[0], r[1], r[2], r[3], nuevo_nombre]
                print("Evento actualizado")

            except Exception as e:
                print("Error:", e)

        # -------------------- Consultar reservaciones --------------------
        elif opcion == "3":
            try:
                fecha_str = input("Fecha a consultar (DD/MM/YYYY): ")
                d, m, a = fecha_str.split("/")
                f_consulta = datetime.date(int(a), int(m), int(d))

                for t in TURNOS:
                    print("\nTurno:", t)
                    for r in Reservaciones.values():
                        if r[2] == f_consulta and r[3] == t:
                            c = Clientes[r[0]]
                            s = Salas[r[1]]
                            print(r[4], "- Sala:", s[0], "- Cliente:", c[0], c[1])
            except Exception as e:
                print("Error:", e)

        # -------------------- Salir --------------------
        elif opcion == "6":
            try:
                if input("¿Salir? (S/N): ").strip().lower() == "s":
                    print("Hasta luego!")
                    break
            except Exception as e:
                print("Error:", e)

        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
