im = mm = ihv = hv = 0
for c in range(1, 5):
    print("=-=-= {}ª pessoa =-=-=".format(c))
    n = input('Nome: ').strip()
    i = int(input('Idade: '))
    s = input('Sexo [M/F]: ').strip().upper()
    im += i
    if c == 1 and s == 'M':
        ihv = i
        hv = n
    if s == 'M' and i > ihv:
        ihv = i
        hv = n
    if s == 'F':
        if i < 20:
            mm += 1
    print('')
print('A média de idade do grupo é de {} anos.'.format(im / 4))
if ihv != 0:
    print('O homem mais velho tem {} anos e se chama {}.'.format(ihv, hv))
if mm == 1:
    print('Ao todo, {} mulher tem menos de 20 anos.'.format(mm))
else:
    print('Ao todo, {} mulheres têm menos de 20 anos.'.format(mm))
