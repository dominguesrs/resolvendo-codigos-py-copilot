# Vamos solicitar como entrada dois números inteiros e depois vamos realizar uma operação simples entre eles.

# Solicitar dois números inteiros como entrada  

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# Realizar a operação entre os números informados
operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

if operacao == '+':
    print(num1 + num2)
elif operacao == '-':
    print(abs(num1 - num2))
elif operacao == '*':
     print(num1 * num2)
elif operacao == '/':
     print(num1 / num2)
else:
     print("Operação inválida")





