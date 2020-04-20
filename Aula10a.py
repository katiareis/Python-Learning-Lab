"""
Aula 10 - Condiçoes com If e Else

Exemplo 1

tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--Fim--')

# If simplificado:

tempo = int(input('Quantos anos tem seu carro?'))
print('Carro novo'if tempo <= 3 else 'carro velho')
print('--Fim--')

Exemplo 2
nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))

"""

nota1 = float(input('Nota do primeiro bimestre: '))
nota2 = float(input('Nota do segundo bimestre: '))
media = (nota1 + nota2)/2
print('A média do aluno é: {:.1f}'.format(media))

if media >= 7:
    print('Parabéns, você passou!')
else:
    print('Sinto muito, você está de DP!')