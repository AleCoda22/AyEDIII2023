def divi(num,seg):
    try:
        res = num/seg
        print(res)
    except ZeroDivisionError:
        print("Trataste de dividir entre cero :( ")
    
divi(100,2)
divi(100,0)


