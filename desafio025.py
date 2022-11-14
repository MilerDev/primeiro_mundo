# crie um programa que leia o nome de uma pessoa e diga se ela tem "silva "no nome.

n = str(input('digite seu nome ')).strip()
print('seu nome tem silva?{}'.format('silva' in n.lower()))