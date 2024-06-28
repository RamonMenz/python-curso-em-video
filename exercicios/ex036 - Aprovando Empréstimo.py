c = float(input('Valor da casa: R$'))
s = float(input('Salário do comprador: R$'))
t = int(input('Quantos anos de financiamento? '))
p = (c / t) / 12
if p <= s * 0.3:
    print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.'.format(c, t, p))
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.'.format(c, t, p))
    print('Empréstimo NEGADO!')
