def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg:.2f}m X {comp:.2f}m é de {a:.2f}m².')


# Programa principal
lar = float(input('Digite a largura do terreno (m): '))
com = float(input('Digite o comprimento do terreno (m): '))
area(lar, com)
