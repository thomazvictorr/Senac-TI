# Sua tarefa é completar o código para avaliar a seguinte expressão: Derivada parcial: ∂z/∂x
# O resultado deve ser atribuído a y. Tenha cuidado - observe os operadores e mantenha suas prioridades em mente. Não hesite em usar quantos parênteses forem necessários.
# Você pode usar variáveis adicionais para encurtar a expressão (mas não é necessário). Teste seu código com cuidado.

x = float(input("Digite o valor para x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)