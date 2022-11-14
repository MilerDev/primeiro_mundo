# crie um programa que leia un numero inteiro
# e mostre na tela se ele é PAR ou IMPAR.
n = int(input('Digite um numero'))
r = n % 2
if r == 0:
    print(' o numero {} e PAR'.format(n))
else:
    print('o numero {} é IMPAR'.format(n))