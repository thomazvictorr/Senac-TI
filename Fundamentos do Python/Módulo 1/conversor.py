# Milhas e quilômetros são unidades de comprimento ou distância.
# Lembrando que 1 milha é igual a aproximadamente 1.61 quilômetros, complete o programa no editor para que converta:
# milhas em quilômetros;
# quilômetros em milhas.

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "milhas é", round(miles_to_kilometers, 2), "quilômetros")
print(kilometers, "quilômetros é", round(kilometers_to_miles, 2), "milhas")