from math import radians, sin, cos, tan
a = int(input('Digite o ângulo que você deseja: '))
print('O ângulo de {}° tem o seno de {:.3f}.'.format(a, sin(radians(a))))
print('O ângulo de {}° tem o cosseno de {:.3f}.'.format(a, cos(radians(a))))
print('A ângulo de {}° tem a tangente de {:.3f}.'.format(a, tan(radians(a))))
