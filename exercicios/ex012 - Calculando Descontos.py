p = float(input('Digite o preço do produto: '))
np = p - p * 0.05
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(p, np))
