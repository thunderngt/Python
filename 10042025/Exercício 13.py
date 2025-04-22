n1 = input("Digite um número: ")

if n1 == n1[::-1]:
    print("O número", n1, "é um palíndromo.")
else:
    print("O número", n1, "não é um palíndromo.")