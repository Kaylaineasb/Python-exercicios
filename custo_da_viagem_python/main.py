dist = float(input('Qual é a distância da sua viagem '))
if dist<=200:
    valor = dist*0.50
else:
    valor = dist*0.45
print('O valor a pagar será R${} '.format(valor))