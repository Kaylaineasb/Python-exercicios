soma=0
for cont in range(1,501,+2):
    if cont%3 ==0:
       soma+=cont
print('A soma dos números ímpares e múltiplos de 3 no intervalo de 1 a 500 é {}'.format(soma) )