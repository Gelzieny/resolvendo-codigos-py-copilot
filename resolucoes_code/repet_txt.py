# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

operacoes = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}


dado1 = int(input("Digite o primeiro dado: "))
dado2 = int(input("Digite o segundo dado: "))

operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")


if operacao in operacoes:
    resultado = operacoes[operacao](dado1, dado2)
else:
    print("Operação inválida")

# Exibe o resultado
print("Resultado da soma:", resultado)
