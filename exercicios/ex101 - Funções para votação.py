def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        print('NÃO VOTA.')
    elif 16 <= idade < 18 or idade > 65:
        print('VOTO OPCIONAL.')
    else:
        print('VOTO OBRIGATÓRIO.')


# Programa principal
print('-' * 30)
a = int(input('Em que ano você nasceu? '))
voto(a)
