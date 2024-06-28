lista = []
dados = []
nomesp = []
nomesl = []
r = 0
while r != 'N':
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    lista.append(dados[:])
    dados.clear()
    r = input('Quer continuar? [S/N] ').strip().upper()[0]
for c in lista:
    dados.append(c[1])
for d in lista:
    if d[1] == max(dados):
        nomesp.append(d[0])
    elif d[1] == min(dados):
        nomesl.append(d[0])
print('=-' * 30)
print(f'{len(lista)} pessoas foram cadastradas.')
print(f'O maior peso foi de {max(dados)}kg. Peso de: ', end='')
for np in nomesp:
    print(f'{np}', end='')
    print('.') if np == nomesp[-1] else print(', ', end='')
print(f'O menor peso foi de {min(dados)}kg. Peso de: ', end='')
for nl in nomesl:
    print(f'{nl}', end='')
    print('.') if nl == nomesl[-1] else print(', ', end='')
