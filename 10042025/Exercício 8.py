while True:
    try:
        print('Lista de opções:')
        print('[1] Adição')
        print('[2] Subtração')
        print('[3] Divisão')
        print('[4] Multiplicação')
        print('[5] Sair')
        
        opcao = int(input('Digite o número da opção desejada:'))
        if opcao == 5:
            print('Saindo...')
            break
        elif 1 <= opcao <= 4:
            num1 = int(input('Digite o número que deseja saber a tabuada:'))
            
            for i in range(1,11):     
                if opcao == 1:
                    print(f'A soma de {num1} + {i} é: {num1 + i}') 
                if opcao == 2:
                    print(f'A subtração de {num1} - {i} é: {num1 - i}')
                if opcao == 3:
                    print(f'A divisão de {num1} / {i} é: {num1 / i:.2f}')    
                if opcao == 4:
                    print (f'A multiplicação de {num1} * {i} é: {num1 * i}')
        else: 
            print ('Opção inválida.')
    except(ValueError): print('Você não digitou um número válido')

