la = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
a = la * h
t = a / 2
print('Sua parede tem a dimensão de {:.2f}m X {:.2f}m e sua área é de {:.2f}m².'.format(la, h, a))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(t))
