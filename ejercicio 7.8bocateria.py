pedidos_bocadillos = ['fronterizo', 'mallorquin', 'catalan', 'lomo y queso',]
bocadillos_terminados = []

while pedidos_bocadillos:
    bocata = pedidos_bocadillos.pop()

    print(f"Su bocadillo {bocata} está listo.")
    bocadillos_terminados.append(bocata)

print("\nLa lista de bocadillos es: ")
for bocata in bocadillos_terminados:
    print(bocata.title())