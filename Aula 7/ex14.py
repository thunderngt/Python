# Programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. O carro custa R$60 por dia e R$0,15 por Km rodado.
dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos quilômetros rodados? '))
preço = (dia * 60) + (km * 0.15)
print('-=-' * 20)
print('O valor a se pagar é de R${:.2f} '.format(preço))
print('-=-' * 20)