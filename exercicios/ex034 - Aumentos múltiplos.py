s = float(input('\033[34mDigite o salário do funcionário:\033[m R$'))
if s <= 1250:
    ns = s * 1.15
else:
    ns = s * 1.1
print('O funcionário que ganhava R${:.2f} passa a ganhar \033[32mR${:.2f}\033[m agora.'.format(s, ns))
