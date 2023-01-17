total = caro = cont = preco_barato = 0
barato = ''
while True:
    print('='*30)
    print(' '*5,'LOJA SUPER BARATÃO')
    print('='*30)
    nome_produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total +=preco
    cont+=1
    if preco>1000:
        caro+=1
    if cont==1:
        barato = nome_produto
        preco_barato = preco
    if preco<preco_barato:
        preco_barato = preco
        barato=nome
    escolha = str(input('Quer continuar?[S/N]')).upper()
    if escolha=='N':
        break
print('='*10,'FIM DO PROGRAMA','='*10)
print(f'O total da compra foi R${total:5.2f}')
print(f'Temos {caro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${preco_barato:5.2f}')