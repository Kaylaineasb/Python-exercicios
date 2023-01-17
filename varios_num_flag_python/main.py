cont = soma = 0
while True:
    num = int(input('Digite um número [999 para parar] '))
    if num==999:
        break
    cont+=1
    soma+=num
print('Você digitou {} números e a soma é {} '.format(cont,soma)