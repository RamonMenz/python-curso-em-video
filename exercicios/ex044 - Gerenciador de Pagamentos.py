print('{:=^30}'.format(" PETER'S BOUTIQUE "))
p = float(input('Preço das compras: R$'))
print('OPÇÕES DE PAGAMENTO:')
print('''[ 1 ] À vista em dinheiro/cheque (10% de desconto).
[ 2 ] À vista no cartão (5% de desconto).
[ 3 ] Em até 2x no cartão (preço normal).
[ 4 ] 3x ou mais no cartão (20% de juros).''')
o = int(input('Digite a opção desejada: '))
if o == 1:
    pf = p * 0.9
    print('Sua compra de R${:.2f}, com desconto de 10%, custará R${:.2f} em dinheiro/cheque.'.format(p, pf))
elif o == 2:
    pf = p * 0.95
    print('Sua compra de R${:.2f}, com desconto de 5%, custará R${:.2f} no cartão.'.format(p, pf))
elif o == 3:
    print('Sua compra de R${:.2f} será parcelada em 2x de R${:.2f} no cartão (sem juros).'.format(p, p / 2))
elif o == 4:
    x = int(input('Quantidade de parcelas: '))
    pf = p * 1.2
    print('Sua compra de R${:.2f}, com juros de 20%, custará R${:.2f} '.format(p, pf), end='')
    print('e será parcelada em {}x de R${:.2f}.'.format(x, pf / x))
else:
    print('Opção inválida. Tente novamente.')
