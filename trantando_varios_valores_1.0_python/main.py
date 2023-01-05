num = 0
cont=0
soma=0
while num!=999:
    num = int(input('Digite um número [999 para parar]: ')) 
    cont +=1 
    if num!=999:
        soma+=num
print('Foram digitados {} números e a soma deles é {}'.format(cont-1,soma))