peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura'))
imc = peso/ (altura**2)
if imc<18.5:
    print('Seu IMC é {:.1f} e você está abaixo do peso'.format(imc))
elif imc>=18.5 and imc<25:
    print('Seu IMC é {:.1f} e você está no peso ideal'.format(imc))
elif imc>=25 and imc<30:
    print('Seu IMC é {:.1f} e você está com sobrepeso'.format(imc))
elif imc>=30 and imc<40:
    print('Seu IMC é {:.1f} e você está obeso'.format(imc))
else:
    print('Seu IMC é {:.1f} e você está com obesidade mórbida'.format(imc))