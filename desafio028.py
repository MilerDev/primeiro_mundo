# escreva um programa que faça o computador 'pensar' em um numero
# inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual
# foi o numero escolhido pelo computador .
# o programa devera escrever na tela se o usuario venceu ou perdeu.
from random import randint
from time import sleep
c = randint(0, 5) # faz o computador 'pensar'
print('-=-' * 20)
print('vou pensar em um numero entre 0 e 5 .tente adivinhar')
print('-=-' * 20)
n = int(input(print('digite um numero :'))) # jorgador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if n == c:
    print('Barabéns vocé a certou! eu pensei {} '.format(c))
else:
    print('voce errou! eu pensei no numero {} e não {}'.format(c, n))