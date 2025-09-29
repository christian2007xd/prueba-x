import datetime

FORMATO_FECHA = "%d/%m/%Y"
FECHA_ACTUAL = datetime.datetime.today()

empleado = []
identificados = []

def Calcular_edad_actual(fecha_nacimiento: datetime.date) -> int:
    edad_aproximada = FECHA_ACTUAL.year - fecha_nacimiento.year
    if (FECHA_ACTUAL.month, FECHA_ACTUAL.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        return edad_aproximada -1
    return edad_aproximada

while True:
    nombre = input("Ingrese el nombre del empleado (x para terminar): ")
    if nombre.upper() == "X":
        break
    
    fecha_nacimiento_str = input("Ingrese la fecha de nacimiento del empleado (DD/MM/AAAA): ")
    empleado.append((nombre,datetime.datetime.strptime(fecha_nacimiento_str, FORMATO_FECHA).date()))


edad_minima = int(input("Ingrese una edad mínima: "))
for nombre, fecha in empleado:
    if Calcular_edad_actual(fecha) >= edad_minima:
        identificados.append((nombre, fecha, Calcular_edad_actual(fecha)))

print(f"{'Nombre':<20}{'Fecha de Nacimiento':<20}{'Edad':<5}")
print("*" * 50)
for nombre, fecha, edad in identificados:
    print(f"{nombre:<20}{fecha.strftime(FORMATO_FECHA):<20}{edad:<5}")

