from random import randint
from time import sleep
from operator import itemgetter
dado = {}
ranking = []
print('Dados rolando...')
for c in range(1, 5):
    dado[f'Jogador{c}'] = randint(1, 6)
    print(f'Jogador{c} tirou {dado[f"Jogador{c}"]} no dado.')
    sleep(1)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
print('=-' * 15)
print(f'{" Ranking Dos Jogadores ":=^30}')
for i, d in enumerate(ranking):
    print(f"{f'{i + 1}° lugar: {d[0]} com {d[1]}':^30}")
print('=' * 30)
