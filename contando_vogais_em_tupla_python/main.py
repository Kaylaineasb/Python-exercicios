palavras = ('aprender','programar','linguagem','python',
            'curso','gratis','estudar','praticar','trabalhar',
            'mercado','programador','futuro')
for p in palavras:
    cont=0
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')
            cont+=1
    print(f', {cont} vogais')