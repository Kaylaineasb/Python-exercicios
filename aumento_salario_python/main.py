valor = float(input('Informe seu salário'))
if valor>1250:
    salario= salario+ (salario*0.10)
else:
    salario= salario+ (salario*0.15)
print('Seu novo salário com aumento é R${} '.format(salario))