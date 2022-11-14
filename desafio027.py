# faça um programa que leia o nome completo de um apessoa
# mostre em seguida o primeiro e o ultim nome separadamente.
nome = str(input('digite seu nome completo :')).strip()
n = nome.split()
print('muito prazer em te conhecer!')
print('seu primeiro nome é {}'.format(n[0]))
print('seu ultimo nome é {}'.format(n[len(n)-1]))
