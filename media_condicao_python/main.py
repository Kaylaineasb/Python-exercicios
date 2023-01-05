n1 = float(input('Informe sua primeira nota: '))
n2 = float(input('Informe sua segunda nota: '))
media = (n1+n2)/2
if media<5:
    print('Sua média foi {} e você está reprovado'.format(media))
elif media>=5 and media<6.9:
    print('Sua média foi {} e você está de recuperação'.format(media))
else:
    print('Sua média foi {} e você está aprovado'.format(media))