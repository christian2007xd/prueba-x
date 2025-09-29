import datetime

fecha_nacimiento_str = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y").date()# str ->datetime

fecha_actual = datetime.datetime.today()

edad_aproximada = fecha_actual.year - fecha_nacimiento.year
if (fecha_actual.month, fecha_actual.day)<(fecha_nacimiento.month, fecha_nacimiento.day):
    edad_actual = edad_aproximada -1
else:
    edad_actual = edad_aproximada


print(f"Naciste un {fecha_nacimiento}, eso significa que tienes {edad_actual} años")
