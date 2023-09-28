class Math:

    @staticmethod
    def sumar(num1, num2):
        return num1 + num2

    @staticmethod
    def restar(num1, num2):
        return num1 - num2

    @staticmethod
    def multiplicar(num1, num2):
        return num1 * num2

    @staticmethod
    def dividir(num1, num2):
        return num1 / num2

print(Math.sumar(5, 7))
print(Math.restar(9, 3))
print(Math.multiplicar(15, 9))
print(Math.dividir(10, 2))