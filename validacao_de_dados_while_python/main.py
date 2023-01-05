sexo = str(input('Informe seu sexo: [M/F] ')).upper()
while sexo!='M' or sexo!='F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F] '))
print('Sexo {} registrado com sucesso'.format(sexo))