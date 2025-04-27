# Sua tarefa é preparar um código simples capaz de avaliar a hora de término de um período, dado como um número de minutos (pode ser arbitrariamente grande). A hora de início é fornecida como um par de horas (0..23) e minutos (0..59). O resultado deve ser impresso no console.
# Por exemplo, se um evento começa às 12:17 e dura 59 minutos, termina às 13:16.
# Não se preocupe com imperfeições no código - tudo bem se ele aceitar um tempo inválido - o mais importante é que o código produz resultados válidos para dados de entrada válidos.
# Teste seu código com cuidado. Dica: usar o operador % pode ser a chave para o sucesso.

hour = int(input("Hora de início (horas): "))
mins = int(input("Hora de início (minutos): "))
dura = int(input("Duração do evento (minutos): "))

mins = mins + dura # encontre um total de todos os minutos
hour = hour + mins // 60 # encontre um número de horas escondido em minutos e atualize a hora
mins = mins % 60 # minutos corretos para cair no intervalo (0..59)
hour = hour % 24 # horas corretas para cair no intervalo (0..23)

print(hour, ":", mins, sep='')