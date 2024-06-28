c = ('\033[m',       # 0 - sem cores
     '\033[39;41m',  # 1 - vermelho
     '\033[39;42m',  # 2 - verde
     '\033[39;44m',  # 3 - azul
     '\033[39;40m'   # 4 - negativo
     )


def escreva(msg, cor):
    from time import sleep
    print(c[cor], end='')
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))
    print(c[0], end='')
    sleep(1)


def ajuda():
    while True:
        escreva('Sistema de Ajuda PyHelp', 3)
        r = input('Função ou Biblioteca > ').strip()
        if r.lower() == 'sair':
            escreva('ATÉ LOGO!', 1)
            break
        escreva(f'Acessando o manual do comando "{r}"', 2)
        print(c[4], end='')
        help(r)
        print(c[0], end='')


# Programa principal
ajuda()
