v = int(input('Qual é a velocidade atual do carro: '))
if v > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80km/h.\033[m')
    print('\033[31mVocê deve pagar uma multa de \033[32mR${:.2f}\033[31m.\033[m'.format((v - 80) * 7))
print('\033[33mTenha um bom dia! Dirija com segurança!\033[m')
