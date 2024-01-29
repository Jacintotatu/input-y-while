"""
entradas = "¿Cuantos años tienes?: "

comprar = ""

while True:
    comprar = int(input(entradas))

    if comprar >= 3 and comprar <= 12:
        print(f"Ok, si tienes {comprar} años tu entrada te cuesta 8 €.")

    elif comprar > 12:
        print(f"Ok, si tienes {comprar} años tu entrada te cuesta 12 €.")

    else:
        print(f"Ok, si tienes {comprar} años ¡¡entras gratis!!.")
    break

entradas = "¿Cuantos años tienes?: "

comprar = ""

active = True

while active:
    comprar = int(input(entradas))

    if comprar >= 3 and comprar <= 12:
        print(f"Ok, si tienes {comprar} años tu entrada te cuesta 8 €.")

    elif comprar > 12:
        print(f"Ok, si tienes {comprar} años tu entrada te cuesta 12 €.")

    else:
        print(f"Ok, si tienes {comprar} años ¡¡entras gratis!!.")
    
    active = False
    """

entradas = "¿Cuantos años tienes?: "

comprar = ""

while True:
    comprar = int(input(entradas))

    if comprar >= 3 and comprar <= 12:
        print(f"Ok, si tienes {comprar} años tu entrada te cuesta 8 €.")

    elif comprar > 12:
        print(f"Ok, si tienes {comprar} años tu entrada te cuesta 12 €.")

    else:
        print(f"Ok, si tienes {comprar} años ¡¡entras gratis!!.")

"""
while True:
    edad = int(input('Cuantos años tienes: '))
    if edad < 3:
        print('¡Entras gratiiiis!')
    elif edad < 12:
        print('Tu entrada cuesta 8 €.')
    else:
        print('Tu entrada cuesta 12 €.')
"""