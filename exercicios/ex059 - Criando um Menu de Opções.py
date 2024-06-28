from time import sleep
e = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while e != 5:
    e = int(input('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa\n
>>> Escolha uma opção: '''))
    if e == 1:
        print('A soma entre {} e {} é igual à {}.'.format(n1, n2, n1 + n2))
        sleep(3)
    elif e == 2:
        print('A multiplicação entre {} e {} é igual à {}.'.format(n1, n2, n1 * n2))
        sleep(3)
    elif e == 3:
        if n1 > n2:
            print('Entre {} e {}, o maior valor é {}.'.format(n1, n2, n1))
        elif n2 > n1:
            print('Entre {} e {}, o maior valor é {}.'.format(n1, n2, n2))
        else:
            print('Os dois valores são iguais.')
        sleep(3)
    elif e == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif e == 5:
        print('Finalizando...')
        sleep(2)
        print('Fim do programa. Volte sempre!')
    else:
        print('Opção inválida. Tente novamente!')
    print('-=-' * 15, '\n')
