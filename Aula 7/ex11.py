# Programa que lê o preço de um produto e mostra seu novo preço com 5% de desconto
p1 = float(input('Digite o preço de um produto:R$ '))
p2 = p1 * 0.95
print('O preço novo desse produto é de {:.2f} reais'.format(p2))