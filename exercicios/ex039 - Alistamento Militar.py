from datetime import date
print('[ 1 ] Mulher\n[ 2 ] Homem')
s = int(input('Informe seu sexo: '))
if s == 1:
    print('Você não precisa se alistar.')
elif s == 2:
    a = int(input('Ano de nascimento: '))
    i = date.today().year - a
    print('Quem nasceu em {} faz {} anos em {}.'.format(a, i, date.today().year))
    if i == 17:
        print('Ainda falta 1 ano para o alistamento.')
        print('Seu alistamento será em {}.'.format(date.today().year + 1))
    elif i < 18:
        print('Ainda faltam {} anos para o alistamento.'.format(18 - i))
        print('Seu alistamento será em {}.'.format(a + 18))
    elif i == 18:
        print('Está na hora de se alistar ao serviço militar.')
    elif i == 19:
        print('Você já deveria ter se alistado há 1 ano.')
        print('Seu alistamento foi em {}.'.format(date.today().year - 1))
    else:
        print('Você já deveria ter se alistado há {} anos.'.format(i - 18))
        print('Seu alistamento foi em {}.'.format(a + 18))
else:
    print('Opção inválida. Tente novamente.')
