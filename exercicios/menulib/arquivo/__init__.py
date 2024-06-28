def arqexiste(nome):
    """
    -> Essa função verifica a existência de um arquivo.
    :param nome: o nome do arquivo.
    :return: False caso ele não exista e True caso ele exista.
    """
    try:
        arq = open(nome, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararq(nome):
    """
    -> Essa função cria um arquivo.
    :param nome: o nome do arquivo.
    :return: a informação de que o arquivo foi criado ou não.
    """
    try:
        arq = open(nome, 'wt+')
        arq.close()
    except Exception as e:
        print('\033[31mHouve um erro na criação do arquivo!\033[m')
        print(f'\033[31m{e}\033[m')
    else:
        print(f"\033[32mArquivo '{nome}' criado com sucesso!\033[m")


def lerarq(nome):
    """
    -> Essa função lê um arquivo.
    :param nome: o nome do arquivo.
    :return: o conteúdo do arquivo.
    """
    arq = ''
    from menulib.interface import cabecalho
    try:
        arq = open(nome, 'r')
    except Exception as e:
        print('\033[31mErro ao ler o arquivo!\033[m')
        print(f'\033[31m{e}\033[m')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in arq:
            dado = linha.replace('\n', '').split(';')
            print(f"{dado[0]:<30}{dado[1]:>5} anos")
    finally:
        arq.close()


def cadastrar(arquivo, nome='<desconhecido>', idade=0):
    """
    -> Essa função cadastra os dados de um novo usuário.
    :param arquivo: o nome do arquivo.
    :param nome: o nome da pessoa a ser cadastrada.
    :param idade: a idade da pessoa a ser cadastrada.
    :return: alguma informação sobre os dados do novo cadastro.
    """
    arq = ''
    try:
        arq = open(arquivo, 'at')
    except Exception as e:
        print('\033[31mHouve um erro na abertura do arquivo!\033[m')
        print(f'\033[31m{e}\033[m')
    else:
        try:
            arq.write(f'{nome};{idade}\n')
        except Exception as e:
            print('\033[31mHouve um erro na hora de escrever os dados!\033[m')
            print(f'\033[31m{e}\033[m')
        else:
            print(f'\033[32mOs dados de {nome} foram adicionados!\033[m')
    finally:
        arq.close()
