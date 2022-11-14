# crie um programa que leia o nome de uma
# cidade e diga se ela começa ou nao com o nome "santo".
cid = str(input('em que  cidade que voce nasceu')).strip()
print(cid[:5].upper() == 'SANTO')