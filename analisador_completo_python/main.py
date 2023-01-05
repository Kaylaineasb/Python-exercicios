soma_idades=0
media_idades=0
idade_homem=0
homem_velho=''
cont_mulheres=0
for c in range(1,5):
    print('-'*5,"{}º PESSOA".format(c),'-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).upper()
    soma_idades+=idade
    media_idades=soma_idades/4
    if c==1:
        homem_velho=nome
    if sexo=='M':
        if idade>idade_homem:
            idade_homem=idade
            homem_velho=nome
    if sexo=='F':
        if idade<20:
            cont_mulheres+=1
print('A média de idade do grupo é de {} anos'.format(media_idades))
print('O homem mais velho tem {} anos e se chama {}. '.format(idade_homem,homem_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(cont_mulheres))