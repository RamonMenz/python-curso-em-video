c = t = m1000 = b = mp = 0
print('-' * 30)
print('{:^30}'.format("PETER'S BOUTIQUE"))
print('-' * 30)
while True:
    c += 1
    n = input('Nome do produto: ').strip()
    p = float(input('Preço: R$'))
    r = ' '
    while r not in 'SN':
        r = input('Quer adicionar mais um produto? [S/N] ').strip().upper()[0]
    t += p
    if p > 1000:
        m1000 += 1
    if c == 1 or mp > p:
        mp = p
        b = n
    if r == 'N':
        break
print('-' * 30)
print('INFORMARÇÕES SOBRE AS SUAS COMPRAS:')
print(f'''O total da compra foi R${t:.2f}.
Temos {m1000} produto(s) custando mais de R$1000.00.
O produto mais barrato foi {b} que custa R${mp:.2f}.''')
