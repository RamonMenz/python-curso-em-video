jogos = dict()
gols = list()
jogos['nome'] = input('Nome do jogador: ').strip().capitalize()
q = int(input(f'Quantas partidas {jogos["nome"]} jogou? '))
for c in range(q):
    gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
jogos['gols'] = gols[:]
jogos['total'] = sum(gols)
print('=-' * 20)
print(f'O jogador {jogos["nome"]} jogou {q} partidas.')
print('Quantidade de gols em cada partida:')
for i, v in enumerate(jogos['gols']):
    print(f'    => Partida {i + 1}: {v}')
print(f'Total de gols: {jogos["total"]}')
print('=-' * 20)
