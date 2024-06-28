print('=' * 30)
print('{:^30}'.format("PETER'S BANK"))
print('=' * 30)
v = int(input('Qual valor você quer sacar? R$'))
c = 50
tc = 0
while True:
    if v >= c:
        v -= c
        tc += 1
    else:
        if tc != 0:
            print(f'{tc} cédula(s) de R${c}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        tc = 0
        if v == 0:
            break
print('=' * 30)
print('{:^30}'.format("Volte sempre ao PETER'S BANK!\nTenha um bom dia."))
print('=' * 30)
