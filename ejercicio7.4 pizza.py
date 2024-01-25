
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

    

