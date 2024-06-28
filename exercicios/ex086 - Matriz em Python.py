lista = [[], [], []]
for x in range(3):
    for y in range(3):
        n = int(input(f'Digite um valor para ({x}, {y}): '))
        lista[x].append(n)
print('=-' * 16)
for a in range(3):
    for b in lista[a]:
        print(f'[{b:^5d}]', end='')
    print()
