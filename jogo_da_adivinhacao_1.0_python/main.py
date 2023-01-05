from random import randint
print('Vou pensar em um número entre 0 e 5!')
num = int(input('Que número eu pensei? '))
n = randint(0,5)
if num==n:
    print('Você acertou!')
else:
    print('Você errou! Eu pensei no {} '.format(n))