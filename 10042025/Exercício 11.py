n = int(input('Digite o número que deseja obter a raiz quadrada:'))
b = 2

while abs(n - (b*b)) > 0.00001:
       p = (b+(n/b)) / 2
       b = p
       print(f'A raiz quadrada é {p:.3f}')