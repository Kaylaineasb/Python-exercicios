v = float(input('Qual é a velocidade atual do carro?'))
if v>80:
    print('Você foi multado')
    multa = (v-80)*7
    print('Sua multa foi de: R${}'.format(multa))
print('Tenha um bom dia! Dirija com cuidado! ')