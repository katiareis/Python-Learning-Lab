"""
Alinhamentos com print

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))

{:>20} Alinhamento de 20 caracteres à direita
{:<20} Alinhamento de 20 caracteres à esquerda
{:^20} Alinhamento centralizado em 20 caracteres ou "espaços".
{:=>20} Alinhamento centralizado em 20 caracteres ou "espaços" com sinal de igual no espaços.
, end=' '    Para que o print da próxima linha suba para o fim da linha anterior
\n    Para que o print desça para a próxima linha

"""
nome = input('Qual é o seu nme? ')
print('Prazer em te conhecer {:20}!'.format(nome))
