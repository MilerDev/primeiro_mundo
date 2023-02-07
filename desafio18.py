# faça um programa ue leia um angulo qualuer e mostre na tela o seno, cosseno e tangente desse angulo.
import math
an = float(input('digite o angulo que você deseja:'))
seno = math.sin(math.radians(an))
print('o ângulo de {} tem o Seno de {:.2f}'.format(an, seno))
cos = math.cos(math.radians(an))
print('o ângulo de {} tem o cosseno de {:.2f}'.format(an, cos))
tag = math.tan(math.radians(an))
print('o Ângulo de {} tem a tangente de {:.2f}'.format(an, tag))