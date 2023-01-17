cont_mulheres = cont_homens = maiores_idade = 0
while True:
    print('-'*30)
    print('Cadastro de usuário')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [F/M]')).upper()
    if sexo=='M':
        cont_homens+=1
    else:
        if idade<20:
            cont_mulheres+=1
    if idade>18:
        maiores_idade+=1
    escolha = str(input('Quer cadastrar outro? [s/n]')).upper()
    if escolha=='N':
        break
print(f'A quantidade de mulheres que tem menos de 20 anos foi: {cont_mulheres}')
print(f'A quantidade de homens cadastrados foi: {cont_homens}')
print(f'Total de pessoas com mais de 18 anor: {maiores_idade}')
