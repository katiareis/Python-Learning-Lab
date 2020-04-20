"""
Formatando Valores com modificadores - Aula 5

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de pronto flutuante (float)
:.(NÚMERO) Quantidade de casas decimais (float)
:(cARACTERE) (< ou > ou ^) (QUANTIDADE) (TIPO - s,d, ou f)

> - Esquerda
< - Direita
^- Centro

#  num1 = input('Digite um numero: ')
#  num2 = input('Digite outro numero: ')
#  print(num1, num2)  # contatenação
__________________________________________________________________
num_1 = 10
num_2 = 3
divisao = (num_1 / num_2)
print('{:.2f}'.format(divisao))  # O : sinaliza para o Python que vai haver uma formatação. .2 significa duas casas decimais e o f é de float.
print( f'{divisao:.2f}')
"""

nome = 'Katia'
print(f'{nome:s}')