import math
co = float(input('Informe o valor do cateto oposto '))
ca = float(input('Informe o valor do cateto adjacente '))
hip = math.hypot(co,ca)
print('A hipotenusa é: {:.2f}'.format(hip))