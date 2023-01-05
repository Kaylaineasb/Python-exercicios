import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O ângulo {} tem o SENO de {:.2f}'.format(angulo,seno))
cos = math.cos(math.radians(angulo))
print('O ângulo {} tem o COSSENO de {:.2f}'.format(angulo,cos))
tg = math.tan(math.radians(angulo))
print('O ângulo {} tem a TANGENTE de {:.2f}'.format(angulo,tg))