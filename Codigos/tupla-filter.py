tupla = (7,3,8,1,9,25,63,2,78,45,5,4,50)
def mayor_a_cinco(elemento):
    return elemento > 5


resultado = tuple(filter( mayor_a_cinco, tupla))
resultado = len(resultado)
print(resultado)