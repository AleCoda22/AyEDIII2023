num1= int(input("Ingrese un numero:"))
num2= int(input("Ingrese otro numero:"))
pares=[]
impares=[]
while num1!= num2:         
    if num1%2==0:
        pares.append(num1)
    else:
        impares.append(num1)
    num1= num1+1
print(pares)
print(impares)
