a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO.')
    elif a == b or a == c or b == c:
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES.')
    else:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')
