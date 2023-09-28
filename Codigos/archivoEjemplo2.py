archivo = open("Archivoejemplo1.txt", "r+")
content = archivo.read()
nombre=archivo.name
modo=archivo.mode
encoding=archivo.encoding
print (nombre)
print (modo)
print (encoding)
print (content)
archivo.close()
