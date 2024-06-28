maior = 0
menor = 0
for c in range(1, 6):
    p = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('O maior peso lido foi de {:.1f} kg.'.format(maior))
print('O menor peso lido foi de {:.1f} kg.'.format(menor))
