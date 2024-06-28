print('\033[33m-=-\033[m' * 8)
print('\033[34mAnalisador de Triângulos\033[m')
print('\033[33m-=-\033[m' * 8)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('\033[32mOs segmentos acima PODEM FORMAR um triângulo.\033[m')
else:
    print('\033[31mOs segmentos acima NÃO PODEM FORMAR um triângulo.\033[m')
