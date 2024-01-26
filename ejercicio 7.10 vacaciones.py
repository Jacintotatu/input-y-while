respuestas = {}

while True:
    nombre = input('¿Como te llamas?: ')
    lugar = input('Si pudieras visitar cualquier lugar del mundo, ¿donde irías?: ')

    respuestas[nombre] = lugar

    repetir = input('¿A alguien mas le gustaria responder? (si/no): ')
    if repetir == 'no':
        break

print('\n----Resultados----')
for nombre, lugar in respuestas.items():
    print(f"{nombre.title()}, quiere viajar a {lugar.title()}. ")