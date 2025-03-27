# Programa que converte temperaturas
celsius = float(input('|Informe a temperatura em °C: '))
fahrenheit = (celsius * 1.8) + 32
kelvin = (celsius + 273.15)
print('-=-' * 20)
print('A temperatura em Celsius informada equivale a {}°F e {}K'.format(fahrenheit, kelvin))
print('-=-' * 20)