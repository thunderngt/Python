# Programa que lê quantos reais uma pessoa tem e diz quantos dólares ela pode comprar
n = float(input('Digite quantos reais você tem: R$ '))
d = n / 5.64
print('Você pode comprar {:.2f} dólares'.format(d))