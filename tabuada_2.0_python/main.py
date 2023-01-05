num = int(input('Digite um número para ver sua tabuada: '))
print('-='*6)
for cont in range(0,11):
    print('{} x {} = {} '.format(num,cont,num*cont))
print('-='*6)