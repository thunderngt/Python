n = int(input("Digite a quantidade de números primos que deseja ver:"))
quantidade = 0
numero = 2 

while quantidade < n:
    primo = True
    if numero > 2 and numero % 2 == 0:
        primo = False
    else:
        i = 3
        while i * i <= numero and primo:
            if numero % i == 0:
                primo = False
            i += 2

    if primo:
        print(numero, end=' ')
        quantidade += 1

    numero += 1
