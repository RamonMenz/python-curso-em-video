t = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
     'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG',
     'Botafogo', 'Athletico-PR', 'Bahia', 'São Paulo',
     'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba',
     'Avaí', 'Ponte Preta', 'Atlético-GO')
print(f'Lista de times do Brasileirão de 2017: ', end='')
for c in t:
    if c == t[-1]:
        print(f'{c}.\n')
    else:
        print(f'{c}, ', end='')
print(f'Os 5 primeiros são: ', end='')
for c in t[:5]:
    if c == t[4]:
        print(f'{c}.\n')
    else:
        print(f'{c}, ', end='')
print(f'Os 4 últimos são: ', end='')
for c in t[-4:]:
    if c == t[-1]:
        print(f'{c}.\n')
    else:
        print(f'{c}, ', end='')
print(f'Times em ordem alfabética: ', end='')
st = sorted(t)
for c in st:
    if c == st[-1]:
        print(f'{c}.\n')
    else:
        print(f'{c}, ', end='')
time = 7
print(f'A {t[time]} está na {t.index(t[time]) + 1}ª posição.')
