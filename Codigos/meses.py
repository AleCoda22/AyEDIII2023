meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
num=int(input("Escribe un numero de mes:"))
if num >=1 and num <=12:
    print(meses[num-1])
else:
    print("ERROR-Ingrese un numero de mes correcto")
    
    

       
