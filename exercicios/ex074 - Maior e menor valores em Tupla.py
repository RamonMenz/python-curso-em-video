from random import randint
x = int(input('Digite o maior valor que pode ser sorteado: '))
t = (randint(0, x), randint(0, x), randint(0, x),
     randint(0, x), randint(0, x))
print(f'Os valores sorteados foram: ', end='')
for c in t:
    print(c, end=' ')
st = sorted(t)
print(f'\nO maior valor sorteado foi {st[-1]}.')  # Ou {max(t)}
print(f'O menor valor sorteado foi {st[0]}.')  # Ou {min(t)}
