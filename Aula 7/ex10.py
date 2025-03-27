# Programa que lê a altura e largura de uma parede e diz quantos litros de tinta serão necessários para pintá-la, sabendo que cada litro de tinta pinta 2m²
a = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))
area = a * l
t = area / 2
print('A área da parede é de {}m² e será necessário {} litros de tinta'.format(area,t))