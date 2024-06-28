lista = []
p = []
i = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        p.append(n)
    else:
        i.append(n)
    r = input('Quer continuar? [S/N] ').strip().upper()[0]
    if r == 'N':
        break
print('=-' * 25)
print(f'A lista completa é: {lista}')
print(f'A lista dos pares é: {p}')
print(f'A lista dos ímpares é: {i}')
