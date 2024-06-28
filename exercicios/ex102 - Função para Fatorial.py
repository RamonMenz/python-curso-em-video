def fatorial(n=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: o número a ser calculado.
    :param show: valor opcional, mostra ou não a conta.
    :return: o valor do fatorial de um número n.
    """
    f = 1
    print(f'{n}! = ', end='')
    for c in range(n, 0, -1):
        if show:
            print(f'{c} = ' if c == 1 else f'{c} x ', end='')
        f *= c
    return f


# Programa principal
print(fatorial(5, True))
print('-' * 50)
help(fatorial)
