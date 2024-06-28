d = int(input('\033[34mDigite a distância da viagem:\033[m '))
print('Você está prestes a começar uma viagem de \033[4;33m{}km\033[m.'.format(d))
if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45
print('E o preço da sua passagem será de \033[4;32mR${:.2f}\033[m.'.format(p))
