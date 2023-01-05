from datetime import date
cont_maiores=0
cont_menores=0
ano_atual= date.today().year
for c in range(0,7):
    ano = int(input('Em que ano essa pessoa nasceu? '))
    idade = ano_atual-ano
    if idade>=18:
        cont_maiores+=1
    else:
        cont_menores+=1
print('Ao todo tivemos {} pessoas maiores de idade'.format(cont_maiores))
print('E também tivemos {} pessoas menores de idade'.format(cont_menores))