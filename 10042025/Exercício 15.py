lista = [-10, -8, 0, 1, 2, 5, -2, -4]

menor = lista[0]
maior = lista[0]
soma = 0
contador = 0 

for temp in lista:
    if temp < menor:
        menor = temp
    if temp > maior:
        maior = temp
    soma += temp
    contador += 1 

media = soma / contador 

print("Menor temperatura:", menor)
print("Maior temperatura:", maior)
print("Temperatura média:", media)