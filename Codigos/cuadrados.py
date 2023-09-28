lista = [1, 2, 3, 4, 5]
def cuadrados(x):
    return x * x
lista_cuadrados= map(cuadrados, lista)
print(list(lista_cuadrados))
