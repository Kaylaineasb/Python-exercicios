print('='*10,'LOJAS BARBOSA','='*10)
preco_compra = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')
opcao = int(input('Qual é a opção? '))
if opcao==1:
    valor = preco_compra - (preco_compra*10/100)
    print('Sua compra vai custar {} com 10% de desconto'.format(valor))
elif opcao==2:
    valor = preco_compra - (preco_compra*5/100)
    print('Sua compra vai custar {} com 5% de desconto'.format(valor))
elif opcao==3:
    print('Sua compra vai ser parcelada para 2x de R${} sendo o total R${}'.format(valor/2,valor))
elif opcao==4:
    parcela = int(input('Quantas parcelas? '))
    valor = preco_compra + (preco_compra*20/100)
    valor_parcela = valor/parcela
    print('Sua compra será parelada em {}x de R${} com JUROS'.format(parcela,valor_parcela))
    print('Sua compra de R${} vai custar R${} no final'.format(preco_compra,valor))
else:
    print('Informe um valor de opção válido!')
