lista = list()
jogadores = dict()
gols = list()
while True:
    gols.clear()
    print('-' * 40)
    jogadores['Nome'] = input('Nome do jogador: ').strip().capitalize()
    q = int(input(f'Quantas partidas {jogadores["Nome"]} jogou? '))
    for c in range(q):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogadores['Gols'] = gols[:]
    jogadores['Total'] = sum(gols)
    lista.append(jogadores.copy())
    while True:
        r = input('Quer continuar? [S/N] ').strip().upper()[0]
        if r in 'SN':
            break
    if r == 'N':
        break
print('=-' * 20)
print('Cod ', end='')
for k in jogadores.keys():
    print(f'{k:<15}', end='')
print()
print('-' * 40)
for i, v in enumerate(lista):
    print(f'{i:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=-' * 20)
print('[Digite 999 para parar]')
while True:
    r = int(input('Digite o código de um jogador para mostrar mais detalhes sobre ele: '))
    if r == 999:
        break
    elif r >= len(lista):
        print(f'ERRO! Não existe jogador com código {r}. Tente novamente.')
    else:
        print(f'-> Detalhes de aproveitamento de {lista[r]["Nome"]}:')
        for i, v in enumerate(lista[r]['Gols']):
            print(f'    => Partida {i + 1}: {v} ', end='')
            print('gol' if v == 1 else 'gols')
        print(f'Total de gols: {lista[r]["Total"]}')
    print('=-' * 20)
print('Programa encerrado.')
print('<<< Volte sempre! >>>')
