# desenvolva um programa que leia o comprimento de tres reas e diga ao usuario
# se elas pode ou nao formar um triangulo.
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('    Analisandor de triangulos')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-')
a = float(input('primeiro segmento:'))
b = float(input('segundo segmento:'))
c = float(input('teceiro segmento'))
if a < b + c and b < a + c and c < a + b:
    print('os segmentos acima Pode formar trinâgulo!')
else:
    print('os segmentos acima não poden formar triângulo!')