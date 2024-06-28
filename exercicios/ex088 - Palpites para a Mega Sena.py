from random import randint
from time import sleep
jogos = []
jogo = []
print('-' * 50)
print(f'{"PALPITES DA MEGA SENA":^50}')
print('-' * 50)
j = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(j):
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
            cont += 1
        if cont == 6:
            break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
a = f' SORTEANDO {j} JOGOS '
print(f'{a:=^50}')
for i, d in enumerate(jogos):
    print(f'JOGO {i + 1}: {d}')
    sleep(0.5)
print(f'{" BOA SORTE ":=^50}')
