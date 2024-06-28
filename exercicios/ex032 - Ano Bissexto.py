from datetime import date
a = int(input('Que ano você quer analisar? \033[4mColoque 0 para analisar o ano atual:\033[m '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano {} é \033[1;42mBISSEXTO\033[m.'.format(a))
else:
    print('O ano {} \033[1;41mNÃO é BISSEXTO\033[m.'.format(a))
