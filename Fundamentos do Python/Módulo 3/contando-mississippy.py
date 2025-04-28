# Você sabe o que é o Mississipi? Bem, é o nome de um dos estados e riachos dos Estados Unidos. O Rio Mississipi tem cerca de 2.340 milhas de comprimento, o que o torna o segundo maior rio dos Estados Unidos (o mais longo é o Rio Missouri). É tão longo que uma única gota de água precisa de 90 dias para percorrer todo o seu comprimento!

# A palavra Mississipi também é usada para uma finalidade ligeiramente diferente: contar com erros de sorte.

# Se você não está familiarizado com a frase, estamos aqui para explicar o que ela significa: ela é usada para contar segundos.

# A ideia por trás disso é que adicionar a palavra Mississipi a um número ao contar segundos em voz alta faz com que soem mais perto do relógio e, portanto, "um Mississipi, dois Mississipi, três Mississipi" levará aproximadamente três segundos reais! É frequentemente usado por crianças que brincam de esconde-esconde para garantir que o candidato faça uma contagem honesta.

# Sua tarefa é muito simples aqui: escreva um programa que use um loop for para "contar de forma incorreta" para cinco. Depois de contar até cinco, o programa deve imprimir na tela a mensagem final "Pronto ou não, aqui vou eu!"

# Use o esqueleto que fornecemos no editor.

# INFORMAÇÕES EXTRA:
# Observe que o código no editor contém dois elementos que podem não estar totalmente claros para você no momento: a declaração import time e o método sleep(). Vamos falar sobre eles em breve.

# Por enquanto, gostaríamos que você soubesse que importamos o módulo time e usamos o método sleep() para suspender a execução de cada função subsequente print() dentro do loop for por um segundo, para que a mensagem enviada para o console se assemelhe a uma contagem real. Não se preocupe, em breve você saberá mais sobre módulos e métodos.

import time

# Contando até cinco usando "Mississipi"
for i in range(1, 6):  # Contagem de 1 a 5
    print(f"{i} Mississipi")
    time.sleep(1)  # Pausa de 1 segundo

# Mensagem final depois da contagem
print("Pronto ou não, aqui vou eu!")
