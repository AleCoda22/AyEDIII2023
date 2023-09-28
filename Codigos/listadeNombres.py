numero = int(input("Decime cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        palabra = input(f"Decime una palabra {i + 1}: ")
        lista += [palabra]
    print(f"La lista creada es: {lista}")