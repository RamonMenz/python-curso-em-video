def maior(*n):
    from time import sleep
    print('=-' * 20)
    print('Analisando os valores passados...')
    sleep(1)
    if len(n) == 0:
        print('Nenhum valor foi informado.')
    else:
        print(f'Foram informados {len(n)} valores, sendo eles:')
        for c in n:
            print(c, end=' ')
            sleep(0.25)
        print(f'\nO maior valor informado foi {max(n)}.')
    sleep(1)


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
