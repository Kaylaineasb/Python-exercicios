l1 = float(input('Informe o primeiro lado: '))
l2 = float(input('Informe o segundo lado: '))
l3 = float(input('Informe o terceiro lado: '))
if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('É triângulo')
    if l1==l2 and l2==l3:
       print('É um triângulo equilátero!')
    elif l1==l2 and l1!=l2 or l2==l3 and l2!=l1:
       print('É um triângulo isósceles!')
    else:
       print('É um triângulo escaleno')
else:
    print('Não é triângulo!')
