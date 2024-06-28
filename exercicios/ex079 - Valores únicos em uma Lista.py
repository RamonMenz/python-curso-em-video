lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Este valor já tinha sido adicionado.')
    r = 'a'
    while r not in 'S':
        r = input('Quer continuar? [S/N] ').strip().upper()[0]
        if r == 'N':
            break
    if r == 'N':
        break
print('-' * 45)
print(f'Você digitou os valores: {sorted(lista)}')
