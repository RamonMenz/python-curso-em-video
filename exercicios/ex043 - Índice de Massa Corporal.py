p = float(input('Digite o seu peso em quilogramas (kg): '))
h = float(input('Digite a sua altura em metros (m): '))
imc = p / h ** 2
print('O seu IMC é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif imc < 25:
    print('Você está na faixa de peso ideal.')
elif imc < 30:
    print('Você está com sobrepeso.')
elif imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')
