def sorteia(lista):
    from random import randint
    from time import sleep
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(5):
        lista.append(randint(1, 10))
        print(lista[c], end=' ')
        sleep(0.5)


def somapar(lista):
    s = 0
    for c in lista:
        if c % 2 == 0:
            s += c
    print(f'\nA soma dos valores pares é {s}.')


# Programa principal
numeros = list()
sorteia(numeros)
somapar(numeros)
