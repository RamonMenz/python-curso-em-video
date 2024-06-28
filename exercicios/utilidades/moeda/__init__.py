def metade(preco=0.0, f=False):
    res = preco / 2
    return moeda(res) if f else res


def dobro(preco=0.0, f=False):
    res = preco * 2
    return moeda(res) if f else res


def aumentar(preco=0.0, porcentagem=0.0, f=False):
    res = preco * (1 + porcentagem / 100)
    return moeda(res) if f else res


def diminuir(preco=0.0, porcentagem=0.0, f=False):
    res = preco * (1 - porcentagem / 100)
    return moeda(res) if f else res


def moeda(preco=0.0, tipomoeda='R$'):
    return f'{tipomoeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0.0, aum=0.0, dim=0.0):
    print('-' * 30)
    print('Resumo do valor:'.center(30))
    print('-' * 30)
    print(f'{"Preço analizado:":<16}{moeda(preco):>14}')
    print(f'{"Metade do preço:":<16}{metade(preco, True):>14}')
    print(f'{"Dobro do preço:":<16}{dobro(preco, True):>14}')
    print(f'{f"{aum}% de aumento:":<16}{aumentar(preco, aum, True):>14}')
    print(f'{f"{dim}% de redução:":<16}{diminuir(preco, dim, True):>14}')
    print('-' * 30)
