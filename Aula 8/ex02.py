# Programa que lê a medida dos catetos oposto e adjacente e dá o valor da hipotenusa
import math
c1 = float(input('Digite a medida do cateto oposto'))
c2 = float(input('Digite a medida do cateto adjacente'))
hip = (c1**2 + c2**2) ** (1/2)
print('O comprimento da hipotenusa é de {:.2f}'.format(hip))