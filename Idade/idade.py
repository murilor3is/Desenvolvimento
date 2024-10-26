# Pede ao usuario para inserir uma idade
idade = int(input('Digite sua idade: '))

if idade >= 65:
    print('Você é um idoso!')
elif idade >= 18:
    print('Você é um adulto!')
else:
    print('Voce é menor de idade!')
