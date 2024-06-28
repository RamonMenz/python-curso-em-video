from random import randint
print('=-' * 15 + '=')
print('VAMOS JOGAR PAR OU ÍMPAR')
cont = -1
while True:
    print('=-' * 15 + '=')
    j = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    n = int(input('Digite um número: '))
    print('-' * 31)
    cont += 1
    c = randint(0, 5)
    t = c + n
    if j in 'PI':
        print(f'Você jogou {n} e o computador {c}.\nTotal é {t} e DEU', end=' ')
        print('PAR!' if t % 2 == 0 else 'ÍMPAR!')
        print('-' * 31)
        if j == 'P':
            if t % 2 == 0:
                print('Você VENCEU!')
                print('Vamos jogar novamente...')
            else:
                print('Você PERDEU!')
                break
        elif j == 'I':
            if t % 2 == 0:
                print('Você PERDEU!')
                break
            else:
                print('Você VENCEU!')
                print('Vamos jogar novamente...')
    else:
        print('Opção inválida! Tente novamente.')
        break
    print('=-' * 15 + '=')
    print('')
print(f'GAME OVER! Você venceu {cont} vezes.')
print('=-' * 15 + '=')
