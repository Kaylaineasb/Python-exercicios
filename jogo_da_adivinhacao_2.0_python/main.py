import random
tentativas =0
num = random.randint(0,10)
print(num)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
palpite = int(input('Qual o seu palpite? '))
if  palpite==num:
    print('Você acertou!!')
else:
    if palpite>num:
        print('Menos...Tente mais uma vez.')
    else:
        print('Mais...Tente mais uma vez.')
    while palpite!=num:
        palpite = int(input('Qual o seu palpite? '))
        tentativas+=1
        if palpite>num:
            print('Menos...Tente mais uma vez.')
        elif palpite<num:
            print('Mais...Tente mais uma vez.')
        else:
            print('Você acertou!!!')
    
