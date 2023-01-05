from datetime import date
atual = date.today().year
nasc = int(input('Informe o seu ano de nascimento: '))
idade = atual-nasc
if idade<=9:
    print('Sua categoria é MIRIM')
elif idade>9 and idade<=14:
    print('Sua categoria é INFANTIL')
elif idade>14 and idade<=19:
    print('Sua categoria é JUNIOR')
elif idade>19 and idade<=25:
    print('Sua categoria é SENIOR')
else:
    print('Sua categoria é MASTER')