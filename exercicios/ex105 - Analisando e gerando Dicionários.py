def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos.
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['Total de notas'] = len(n)
    r['Maior nota'] = max(n)
    r['Menor nota'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        else:
            r['Situação'] = 'RAZOÁVEL' if r['Média'] >= 5 else 'RUIM'
    return r


# Programa principal
resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)
print('-' * 50)
help(notas)
