# Vamos testar se uma palavra é um palíndromo.

# Recebendo a palavra do usuário
palavra = input("Digite uma palavra: ")

# Verificando se a palavra é um palíndromo
# Um palíndromo é uma palavra que é igual quando lida de trás para frente
palavra_invertida = palavra[::-1]
if palavra == palavra_invertida:
    resultado = True    
else:
    resultado = False

# Exibindo o resultado
print("A palavra é um palíndromo?", resultado)
