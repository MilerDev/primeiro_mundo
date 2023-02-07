# faça um programa que leia uma frase pelo teclato e mostre:
# quantas vezes aparece a letra "A"
# em que posiçao ela aparece a primeira vez
# em que posiçao ela aparece a ultima vez.
f = str(input('digite uma frase :')).upper().strip()
print('A letra A aparece {} vezes na frase .'.format(f.count('A')))
print('A primeira letra A apareceu na posição {}'.format(f.find('A') +1))
print('A ultima letra A apareceu na posição {}'.format(f.rfind('A')+1))