# um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
n1 = input('primeiro aluno')
n2 = input('segundo aluno:')
n3 = input('treceiro aluno:')
n4 = input('quarto aluno:')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))
