anchura = int(input("Anchura del rectángulo: "))
altura = int(input("Altura del rectángulo: "))
dibujo = input("Ingrese el caracter a ser dibujado: ")
for i in range(altura):
    for j in range(anchura):
        print(dibujo, end="")
    print()