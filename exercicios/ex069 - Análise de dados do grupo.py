p18 = h = m20 = 0
while True:
    print('-' * 25)
    print('{:^25}'.format('CADASTRE UMA PESSOA'))
    print('-' * 25)
    r = s = ' '
    i = int(input('Idade: '))
    while s not in 'MF':
        s = input('Sexo: [M/F] ').strip().upper()[0]
    print('-' * 25)
    if i > 18:
        p18 += 1
    if s == 'M':
        h += 1
    if s == 'F' and i < 20:
        m20 += 1
    while r not in 'SN':
        r = input('Quer continuar? [S/N] ').strip().upper()[0]
    if r == 'N':
        break
    print('-' * 25)
    print('')
print('-' * 25)
print(f'''Total de pessoas com mais de 18 anos: {p18}
Total de homens: {h}
Total de mulheres com menos de 20 anos: {m20}''')
