# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = int(input('Digite a quantidade de dias:'))
horas = int(input('Quantas horas?'))
minutos = int(input('Quantos minutos?'))
segundos = int(input('Quantos segundos?'))
total = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos

print('O total de segundos é',total, 'segundos')