lanche = 'Hambúrguer','Suco','Pizza','Pudim'
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')
#ou
for cont in range(0,len(lanche)):
    print(lanche[cont])
#ou
for pos,comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
#Ordenação de tupla
print(sorted(lanche))