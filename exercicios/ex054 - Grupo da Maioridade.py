from datetime import date
m = 0
for c in range(1, 8):
    a = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if date.today().year - a >= 18:
        m += 1
print('Ao todo tivemos {} pessoa(s) maior(es) de idade e {} pessoa(s) menor(es) de idade.'.format(m, 7 - m))
