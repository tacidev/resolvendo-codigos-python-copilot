# Receba um número inteiro e verifique se ele é par ou ímpar.

# Recebendo o número do usuário
numero = int(input("Digite um número inteiro: "))

# Verificando se o número é par ou ímpar
if numero % 2 == 0:
    resultado = "par"
else:
    resultado = "ímpar" 

# Exibindo o resultado
print(f"O número {numero} é {resultado}.")  
