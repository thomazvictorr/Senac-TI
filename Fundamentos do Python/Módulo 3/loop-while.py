# Ouça esta história: um garoto e seu pai, um programador de computador, estão jogando com blocos de madeira. Eles estão construindo uma pirâmide.
# A pirâmide deles é um pouco esquisita, pois na verdade é uma parede em forma de pirâmide - é plana. A pirâmide é empilhada de acordo com um princípio simples: cada camada inferior contém um bloco a mais do que a camada acima.

# A figura ilustra a regra usada pelos construtores:
# A imagem mostra uma pirâmide construída com 6 blocos empilhados em 3 camadas de altura:
# Na base (altura 1), temos 3 blocos alinhados lado a lado.
# Na camada intermediária (altura 2), estão 2 blocos posicionados sobre a base.
# No topo (altura 3), há 1 bloco apoiado no centro.
# Ao lado esquerdo, uma seta aponta para cima indicando "altura: 3", e abaixo dos blocos está escrito "blocos: 6".

# Sua tarefa é escrever um programa que lê o número de blocos que os construtores têm e gera a altura da pirâmide que pode ser construída usando esses blocos.

# Nota: a altura é medida pelo número de camadas totalmente concluídas; se os construtores não tiverem um número suficiente de blocos e não puderem concluir a próxima camada, eles terminarão seu trabalho imediatamente.

# Teste seu código usando os dados que fornecemos.

blocks = int(input("Digite o número de blocos disponíveis: "))

height = 0
used_blocks = 0

while used_blocks + (height + 1) <= blocks:
    height += 1
    used_blocks += height

print("A altura da pirâmide:", height)
