# O consumo de combustível de um carro pode ser expresso de várias maneiras diferentes. Por exemplo, na Europa, ele é mostrado como a quantidade de combustível consumida por 100 quilômetros.

# Nos EUA, é mostrado como o número de quilômetros percorridos por um carro usando um litro de combustível.

# Sua tarefa é escrever um par de funções convertendo l/100 km em mpg e vice-versa.

# As funções:
# são nomeados liters_100km_to_miles_gallon e miles_gallon_to_liters_100km respectivamente;
# use um argumento (o valor correspondente aos nomes)

# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres

def liters_100km_to_miles_gallon(litres):
    gallons = litres / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    litres = 3.785411784
    return litres / km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))