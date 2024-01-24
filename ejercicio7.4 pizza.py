"""
pizza = "\nIngresa un ingrediente para la pizza: "
pizza_no = "\nEscribe 'quit' para quitar el programa."

mensaje = ""

active = True
while active:
    mensaje = input(pizza)

    if mensaje == 'quit':
        active = False
        
    else:
        print(f"Ok, añadiremos el ingrediente {mensaje} a la pizza.")
 """ 

pizza = "\nIngresa un ingrediente para la pizza: "
pizza_no = "\nEscribe 'quit' para quitar el programa."

#print(f"{pizza}")
print(f"{pizza_no}")

mensaje = ""
ingredientes = []
while mensaje != 'quit':
    mensaje = input(pizza)
    print(f"Ok, añadiremos el ingrediente {mensaje} a la pizza.")
    ingredientes.append(mensaje)

    if mensaje == 'quit':
        print('Adios')
        ingredientes.pop()

        break

print(ingredientes)