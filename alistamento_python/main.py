from datetime import date
ano = int(input('Informe o ano de nascimento'))
atual =date.today().year 
idade = atual - ano
if idade==18:
    print('Você precisa se alistar imediatamente')
elif idade<18:
    saldo = 18-idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
elif idade>18:
    saldo = idade-18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
