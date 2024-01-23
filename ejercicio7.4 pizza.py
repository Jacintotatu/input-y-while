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