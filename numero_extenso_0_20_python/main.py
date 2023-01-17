cont = ('zero','um','dois','três','quatro','cinco','seis',
        'sete','oito','nove','dez','onze','doze','treze',
        'catorze','quinze','dezesseis','dezessete','dezoito',
        'dezenove','vinte')
num = int(input('Informe um número entre 0 e 20 '))
while num<0 or num>20:
    num = int(input('Tente novamente. Informe um número entre 0 e 20 '))
print(f'Esse número por extenso é {cont[num]}')