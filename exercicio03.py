x = float(input("Digite o valor de X: "))
y = float(input("Digite o valor de Y: "))

try:
    z = (x**2)+(y**2)/(x-y)
    print(f"O resultado da operação é: ", z)
except ZeroDivisionError:
    print("ERRO: É impossível dividir por '0'.")
    z = None