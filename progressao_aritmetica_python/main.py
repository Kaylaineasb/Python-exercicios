primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Qual a razão da PA? '))
decimo = primeiro +(10-1) *razao
for c in range(primeiro,decimo,razao):
    print('{} '.format(c),end=' ')
print('ACABOU')