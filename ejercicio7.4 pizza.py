
pizza = "\nIngresa un ingrediente para la pizza: "
pizza_no = "\nEscribe 'quit' para quitar el programa."


print(f"{pizza_no}")
mensaje = ""
while mensaje != 'quit':
    mensaje = input(pizza)
    
    if mensaje == 'quit':
        print('Adios')
    else:
        print(f"\nOk, añadiremos el ingrediente {mensaje} a la pizza.")

"""
#Otra opcion

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

