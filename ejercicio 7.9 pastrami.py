pedidos_bocadillos = ['fronterizo', 'pastrami', 'mallorquin', 'catalan', 'pastrami', 'lomo y queso', 'pastrami',]
bocadillos_terminados = []
print(pedidos_bocadillos)
print('No queda Pastrami.')

while pedidos_bocadillos:
    bocata = pedidos_bocadillos.pop()
    if bocata == 'pastrami':
        continue

    print(f"Su bocadillo {bocata} está listo.")
    bocadillos_terminados.append(bocata)

print("\nLa lista de bocadillos es: ")
for bocata in bocadillos_terminados:
    print(bocata.title())