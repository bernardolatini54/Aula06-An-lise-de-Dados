for i in range(5):
    print(f'\nVENDA {i + 1}')
    venda = float(input('Valor da compra: R$ '))
    if venda >= 200:
        desconto = venda * 0.1
        final = venda - desconto
        print(f'O desconto é de: R$ {desconto}.\nO valor da compra é de: R$ {final}')
    else:
        print('Desconto não aplicado.')
