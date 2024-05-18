# Entrada de dados
nome = input('Informe seu nome. \n')
peso = str(input('Informe seu peso em kg. \n')).replace(',', '.')
altura = str(input('Informe sua altura. \n')).replace(',', '.')


# Converte nota para float
peso = float(peso)
altura = float(altura)


# Verifica o IMC
try:
   IMC = peso / (altura * altura)
   print(f'O valor do IMC de {nome} é {IMC:,.2f}.')
except:
    print('Não foi possível calcular o IMC.')


if  IMC <= 18.5:
    print(f'{nome} está com o IMC abaixo. Magreza.')
elif 18.6 < IMC <= 24.9:
    print (f'{nome} está com o IMC normal.')
elif 25.0 < IMC <= 29.9:
    print (f'{nome} está com o IMC um pouco acima. Sobrepeso.')
else: 
    print (f'{nome} está com o IMC elevado. Obesidade.')        




