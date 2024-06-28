def runmenu():
    """
    -> Essa função roda o menu.
    :return: o menu.
    """
    from menulib import arquivo, interface
    arq = r'..\exercicios\menulib\cadastros.txt'
    if not arquivo.arqexiste(arq):
        arquivo.criararq(arq)
    from time import sleep
    while True:
        resposta = interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
        if resposta == 1:
            # Opção de ver as pessoas cadastradas.
            arquivo.lerarq(arq)
        elif resposta == 2:
            # Opção de cadastrar uma nova pessoa.
            interface.cabecalho('NOVO CADASTRO')
            n = input('Nome: ').strip().title()
            i = interface.leiaint('idade: ')
            arquivo.cadastrar(arq, n, i)
        elif resposta == 3:
            # Opção de sair do sistema.
            interface.cabecalho('Saindo do sistema... Até logo!')
            break
        else:
            # Digitou uma opção errada no menu.
            print('\033[31mERRO! Por favor, digite uma opção válida.\033[m')
        sleep(2)
