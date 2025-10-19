# Vamos solicitar uma string e um número inteiro como entrada.
# Depois, teremos que retornar a string repetida o número de vezes informado.

# Recebendo os dados do usuário
texto = input("Digite uma string: ")
vezes = int(input("Digite um número inteiro: "))

# Repetindo a string com espaço entre cada repetição
resultado = (texto + " ") * vezes

# Exibindo o resultado
print("O resultado da repetição é:", resultado)

