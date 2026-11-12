valor = float(input('Valor da venda: R$ '))

print('''
[1] - Pix {12%  de Desconto}
[2] - Débito {8% de Desconto}
[3] - Crédito {5% de Desconto}
[4] - Dinhero {15% de Desconto}
''')

# operacao = True
desconto = 0
opcao = int(input('Informe a opção escolhida: '))

match opcao:
    case 1:
        print('***Pix***')
        desconto = valor * 0.12

    case 2:
        print('***Débito***')
        desconto = valor * 0.08

    case 3:
        print('***Crédito***')
        desconto = valor * 0.05

    case 4:
        print('***Dinheiro***')
        desconto = valor * 0.15
    
    case _:
        # operacao = False
        print('Opção inválida')

if opcao in {1, 2, 3, 4}:
# operacao == True:
# desconto != 0:
    valor_final = valor - desconto
    print(f'Preço: {valor}')
    print(f'Desconto: {desconto}')
    print(f'Total a pagar: {valor_final}')

else:
    print('Por favor, escolha uma das opções acima')