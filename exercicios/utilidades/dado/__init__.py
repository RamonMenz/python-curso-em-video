def leiadinheiro(msg):
    while True:
        num = str(input(msg)).replace(',', '.',).strip()
        if num.isnumeric():
            num = f'{num}.00'
        if num.isalpha() or num.isalnum() or num == '':
            print(f'\033[31mERRO: "{num}" é um número inválido!\033[m')
        else:
            return float(num)
