cont_cinquenta = cont_dez = cont_um = 0
while True:
    print('='*30)
    print(' '*10,'BANCO CEV')
    print('='*30)
    valor = int(input('Que valor você quer sacar? R$'))
    cont_cinquenta = valor//50
    sobra_1 = valor%50
    cont_dez = sobra_1//10
    sobra_2 = sobra_1%10
    cont_um = sobra_2//1
    print(f'Total de {cont_cinquenta} cédulas de R$50,00')
    print(f'Total de {cont_dez} cédulas de R$10,00')
    print(f'Total de {cont_um} cédulas de R$1')
    print('='*30)
    escolha = str(input('Deseja realizar outra operação? [S/N]')).upper()
    if escolha =='N':
        break
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')