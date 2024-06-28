def leiaint(msg):
    """
    -> Essa função só aceita números inteiros.
    :param msg: a mensagem que aparecerá para o usuário.
    :return: o número inteiro digitado pelo usuário.
    """
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return num


def linha(tam=40):
    """
    -> Essa função cria uma linha.
    :param tam: o tamanho da linha.
    :return: a linha do tamanho desejado.
    """
    return '-' * tam


def cabecalho(msg):
    """
    -> Essa função cria um cabeçalho.
    :param msg: a mensagem que aparecerá no cabeçalho.
    :return: o cabeçalho com a mensagem desejada.
    """
    print(linha())
    print(msg.center(len(linha())))
    print(linha())


def menu(lista):
    """
    -> Essa função cria um menu.
    :param lista: a lista que contém as opções que aparecerão no menu.
    :return: o menu com as opções da lista.
    """
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    op = leiaint('\033[32mSua opção: \033[m')
    return op
