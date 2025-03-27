# Programa que lê um ângulo qualquer e mostre o valor do seno, cosseno e tangente.
import math
a = float(input('Digite o ângulo que você deseja: '))
print('Seno: {}'.format (math.sin(math.radians(a))))
print('Cosseno: {}'.format (math.cos(math.radians(a))))
print('Tangente: {}'.format (math.tan(math.radians(a))))