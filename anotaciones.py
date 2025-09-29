datos1 = [10,20,30,40]
resultado1 = []
a,b,c,d = datos1
#debe haber tantas variables a asignar como valores
a,b,*c = datos1

##############################################################################
mascotas = [(15, "fido ")
            (8, "milaneso")
            (6, "Firulais")]

for mascota in mascotas:
    print(f"{mascotas[0]}/t{mascotas [1]}")

##############################################################################
datos2 = [10,20,30,40]
resultado2 = []

for valor in datos2:
    resultado2.append(valor * 3)

print(resultado2)

resultado3 = [valor * 3 for valor in datos2] #list comprehension
print(resultado3)
#################################################################################

valores = [valor for valor in range (1,51)]

pares = [valor for valor in valores if (valor % 2 == 0)]

print(pares)
################################################################################