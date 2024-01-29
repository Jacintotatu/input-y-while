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
"""

ingredientes = []

print('Cuando no quieras mas pon "quit".')
bandera = True
while bandera:
    ingrediente = input('Introduce un ingrediente para tu pizza: ')
    if ingrediente == "quit":
        print('Adeu')
        bandera = False
    
    print(f'Ok, añadiremos {ingrediente.title()} a tu pizza.')
    ingredientes.append(ingrediente)

print('Los ingredientes de la pizza son: ') 
for i in ingredientes:
    
    print(f'                         *{i.title()}')


