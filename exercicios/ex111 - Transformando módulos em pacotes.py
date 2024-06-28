# Agora o pacote utilidades também possui o módulo dado.
from utilidades import moeda
p = float(input('Digite o preço: R$'))
moeda.resumo(p, 10, 15)
