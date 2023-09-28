num1= int(input("Ingrese un numero:"))
num2= int(input("Ingrese otro numero:"))

while num1 <= num2:         
    if num1%2==0:
        print("El numero :",num1,"  Es Par")
    else:
        print("El numero :",num1,"  Es Impar")  
    num1= num1+1
