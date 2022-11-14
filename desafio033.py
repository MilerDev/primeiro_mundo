# faça uma programa que leia tres numero e motre qual é o maior é qual é o menor.
a = int(input('primeiro valor:'))
b = int(input('segundo valor:'))
c = int(input('terceiro valor:'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
print('o menor numero digitado foi {}'.format(menor))
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('o maior numero digitado foi {}'.format(maior))

