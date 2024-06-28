lista = []
for c in range(5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > max(lista):
        lista.append(n)
    else:
        p = 0
        while p < len(lista):
            if n <= lista[p]:
                lista.insert(p, n)
                break
            p += 1
    print(f'Valor adicionado na posição {lista.index(n)}.')
print('=-' * 30)
print(f'Os valores digitados em ordem formam: {lista}')
