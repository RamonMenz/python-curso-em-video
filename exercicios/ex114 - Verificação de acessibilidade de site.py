from urllib import request, error
try:
    site = request.urlopen('https://www.google.com/')
except error.URLError:
    print('\033[31mO site não está acessível no momento.')
else:
    print('\033[32mConsegui acessar o site com sucesso!\033[m')
