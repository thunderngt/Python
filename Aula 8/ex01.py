# Programa que lê um número real e entrega sua parte inteira
import math
num = float(input('Digite um número: '))
inteira = math.trunc(num)
print('A parte inteira de {} é igual a {}'.format(num, (inteira)))