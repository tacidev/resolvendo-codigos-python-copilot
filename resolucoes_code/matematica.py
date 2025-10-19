# Vamos solicitar como entrada dois números
# Depois, vamos realizar uma operação matemática simples entre eles (soma, subtração, multiplicação ou divisão)

# Recebendo os dados do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Escolha de qual será a operação matemática (+, -, * ou /)
operacao = input("Digite a operação (+, -, * ou /): ")

# Realizando a operação matemática escolhida
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero não é permitida."
else:
    resultado = "Erro: Operação inválida."      

# Exibindo o resultado
print("O resultado da operação é:", resultado)