
from functools import reduce
numeros= (7,3,8,1,9,63,2,45,5,4,50,65)

resultado=reduce(lambda x,y:x+y,filter(lambda j:j>5,numeros),0)
print(resultado)
