
def mas_10(num):
  return num + 10
mi_num = "cinco"
try:
  resultado = mas_10(mi_num)
  print(resultado)
except TypeError:
  print("El argumento `mi_num` deberia ser un número")