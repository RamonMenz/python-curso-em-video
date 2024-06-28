t = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9,
     'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
     'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-' * 40)
n = 0
for c in t:
    print(f'{t[n]:.<31}R${t[n + 1]:>7.2f}')
    if n != 16:
        n += 2
    else:
        break
print('-' * 40)
