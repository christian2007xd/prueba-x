import random

cartas = ["el gallo", "la chalupa", "la luna", "el valiente", "el soldado", "el sol", "la dama", "la garza", "el pino ","el arbol", "la palma", "la estrella", "las flechas", "el gorrito" ,"el barril"]

random.shuffle(cartas)

for carta in cartas:
    print(cartas):
    if input("Alguien gano? (S/N)").upper() == "S":
        break
else:
    print("se acabaron las cartas ")