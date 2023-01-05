opcao = 'S'
cont=0
soma=0
maior=0
manor=0
while opcao=='S':
    num = int(input('Digite um número: '))
    cont+=1
    soma+=num
    if cont==1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        if num<menor:
            menor=num
    opcao = str(input('Quer continuar? [S/N]')).upper()
media=soma/cont
print('Você digitou {} números e a média foi {}'.format(cont,media))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))