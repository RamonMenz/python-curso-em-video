lista = [[], [], []]
mais = [[], [], []]
for x in range(3):
    for y in range(3):
        n = int(input(f'Digite um valor para ({x}, {y}): '))
        lista[x].append(n)
        if n % 2 == 0:
            mais[0].append(n)
        if y == 2:
            mais[1].append(n)
        if x == 1:
            mais[2].append(n)
print('=-' * 20)
for x in range(3):
    for y in lista[x]:
        print(f'[{y:^5d}]', end='')
    print()
print('=-' * 20)
print(f'Soma dos valores pares: {sum(mais[0])}')
print(f'Soma dos valores da terceira coluna: {sum(mais[1])}')
print(f'O maior valor da segunda linha: {max(mais[2])}')
