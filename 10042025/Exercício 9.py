numero = int(input('Digite o número que você deseja saber se é ou não primo:'))
if numero == 0 or numero == 1:
    print('Esses números são casos especiais.')
else:
    if numero == 2:
        print('2 é um número primo, pois tem 2 divisores apenas, sendo 1 e ele mesmo.') 
    elif numero % 2 == 0:
        print(f'{numero} não é um número primo.') 

    else: 
        x = 3
        while x < numero:
            if numero % x == 0:
                print('Esse número não é primo.')
                break
            x = x + 2
        if x == numero:
                print('Esse número é primo, pois tem 2 divisores apenas, sendo 1 e ele mesmo.')
        else: 
                print('Esse número não é primo, pois possui mais de 2 divisores.')
