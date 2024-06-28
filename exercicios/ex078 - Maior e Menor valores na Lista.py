lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {c}: ')))
print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {max(lista)} nas seguintes poisções: ', end='')
for i, n in enumerate(lista):
    if n == max(lista):
        print(i, end=' ')
print(f'\nO menor valor digitado foi {min(lista)} nas seguintes poisções: ', end='')
for i, n in enumerate(lista):
    if n == min(lista):
        print(i, end=' ')
