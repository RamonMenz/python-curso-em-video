from datetime import date
dic = dict()
dic['Nome'] = input('Nome: ')
dic['Idade'] = date.today().year - int(input("Ano de nascimento: "))
dic['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if dic['CTPS'] != 0:
    dic['Ano de contratação'] = int(input('Ano de contratação: '))
    dic['Salário'] = f'R${float(input("Salário: R$")):.2f}'
    dic['Idade ao se aposentar'] = dic['Ano de contratação'] + 35 + dic['Idade'] - date.today().year
print('=-' * 25)
for k, v in dic.items():
    print(f'{k}: {v}')
