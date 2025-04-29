# Era uma vez um chapéu. O chapéu não continha coelhos, mas uma lista de cinco números: 1, 2, 3, 4 e 5.

# Sua tarefa:
# escreva uma linha de código que solicite que o usuário substitua o número do meio na lista por um número inteiro inserido pelo usuário (Etapa 1)
# escreva uma linha de código que remova o último elemento da lista (Etapa 2)
# escreva uma linha de código que imprima o comprimento da lista atual (Etapa 3).

chapéu = [1, 2, 3, 4, 5]

chapéu[2] = int(input("Digite um número para substituir o do meio: "))

chapéu.pop()

print("O comprimento da lista agora é:", len(chapéu))
