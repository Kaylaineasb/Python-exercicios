from random import randint
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogada = int(input('Qual é a sua jogada? '))
print('''JO
KEN
PO!!!''')
print('-='*11)
if computador ==0:
    if jogada ==0:
        print('EMPATE')
    elif jogada==1:
        print('JOGADOR VENCE')
    elif jogada==2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
if computador==1:
    if jogada ==0:
        print('COMPUTADOR VENCE')
    elif jogada==1:
        print('EMPATE')
    elif jogada==2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
if computador==2:
    if jogada ==0:
        print('JOGADOR VENCE')
    elif jogada==1:
        print('COMPUTADOR VENCE')
    elif jogada==2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogada]))
print('-='*11)