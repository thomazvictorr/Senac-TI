# Usando um dos operadores de comparação em Python, escreva um programa simples de duas linhas que aceita o parâmetro n como entrada, que é um inteiro, e imprime False se n for menor 100, e True se n for maior ou igual a 100.

n = int(input("Digite um número: ")) 
print(n >= 100) 

number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))

largest_number = number1

if number2 > largest_number:
    largest_number = number2

if number3 > largest_number:
    largest_number = number3

# Imprimir o resultado
print("O maior número é:", largest_number)