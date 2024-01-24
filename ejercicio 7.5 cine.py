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

