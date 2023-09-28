mi_lista = ["Python","C","C++","JavaScript"]
buscar_ind = 4
try:
  print(mi_lista[buscar_ind])
except IndexError:
  print("Lo siento, el indice esta fuera de rango")