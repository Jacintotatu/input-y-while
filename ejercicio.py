"""
ingredientes = []

print('Cuando no quieras mas pon "quit".')

while True:
    ingrediente = input('Introduce un ingrediente para tu pizza: ')
    if ingrediente == "quit":
        print('Adeu')
        break
    
    print(f'Ok, añadiremos {ingrediente.title()} a tu pizza.')
    ingredientes.append(ingrediente)

print('Los ingredientes de la pizza son: ') 
for i in ingredientes:
    
    print(f'                         *{i.title()}')

--------------------------------------------------------------------------------
ingredientes = []

print('Cuando no quieras mas pon "quit".')
bandera = True
while bandera:
    ingrediente = input('Introduce un ingrediente para tu pizza: ')
    if ingrediente == "quit":
        print('Adeu')
        bandera = False
    
    elif ingrediente != "quit":
        print(f'Ok, añadiremos {ingrediente.title()} a tu pizza.')
        ingredientes.append(ingrediente)

print('Los ingredientes de la pizza son: ') 
for i in ingredientes:
    
    print(f'                         *{i.title()}')


ingredientes = []

print('Cuando no quieras mas pon "quit".')

ingrediente = " "

while ingrediente != "quit":
    ingrediente = input('Introduce un ingrediente para tu pizza: ')
    print(f'Ok, añadiremos {ingrediente.title()} a tu pizza.')
    ingredientes.append(ingrediente)
    
else:
    print('Adeu')

    

print('Los ingredientes de la pizza son: ') 
for i in ingredientes:
    
    print(f'                         *{i.title()}')
"""

pedidos_bocadillos = ['mortadela', 'fronterizo', 'mallorquin', 'choriqueso',]

bocatas_terminados = []

while True:
    pide_bocata = input('¿De que quieres el bocata?: ')
    if pide_bocata not in pedidos_bocadillos:
        print(f'De {pide_bocata} no tengo, makina.')
    elif pide_bocata in pedidos_bocadillos:
        print(f'Su bocata de {pide_bocata} esta listo.')
        bocatas_terminados.append(pide_bocata)
        bocatas = bocatas_terminados.remove(pide_bocata)
    elif pedidos_bocadillos == []:
        break
    
    print('Los bocatas elegidos son:  ')
    for i in bocatas_terminados:
        print('                      ', i)
