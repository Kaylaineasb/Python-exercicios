soma=0
for cont in range(1,7):
    num= int(input('Informe um número: '))
    if num%2==0:
        soma+=num;
print('A soma dos números pares foi: {} '.format(soma))