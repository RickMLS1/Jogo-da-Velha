import random

print('Bem vindo ao seu gerador de senhas!')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*(),.?0123456789'

number = input('De quantas senhas você precisa? ')
number = int(number)

length = input('Coloque o tamanho da sua senha: ')
length = int(length)

print('\nAqui estão as suas senhas:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
