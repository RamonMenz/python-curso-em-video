lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = input('Quer continuar? [S/N] ').strip().upper()[0]
    if r == 'N':
        print('=-' * 25)
        print(f'Você digitou {len(lista)} números.')
        print(f'Números em ordem decrescente: {sorted(lista, reverse=True)}')
        if 5 in lista:
            print('O valor 5 faz parte da lista.')
        else:
            print('O valor 5 não faz parte da lista.')
        break
