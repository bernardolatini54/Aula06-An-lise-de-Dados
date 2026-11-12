ingresso = float(input('Valor do ingresso: R$ '))

print('''
[1] - Inteira {Sem desconto}
[2] - Meia entrada {50% de desconto}
[3] - Promoção {30% de desconto}
''')

operacao = True
desconto = 0
opcao = int(input('Qual o tipo de ingresso: '))

match opcao:
    case 1:
        print('Inteira sem desconto!')
    case 2:
        print('Meia entrada - Desconto de 50%!')
        desconto = ingresso * 0.5
    case 3:
        print('Ingresso da promoção - Desconto de 30%!')
        desconto = ingresso * 0.3
    case _:
        print('Opção inválida! *ERROR*')
        operacao = False

if operacao == True:
    valor_final = ingresso - desconto
    print(f'Preço: R$ {ingresso}')
    print(f'Desconto: R$ {desconto}')
    print(f'Valor final: R$ {valor_final}')

else:
    print('Por favor, escolha uma das opções acima!')