"""
Operadores Lógicos - Aula 4
and = comparação entre dois argumentos e ambas precisam ser verdadeiras (Verdadeiro + Verdadeiro = True
or =  comparação entre dois argumentos e uma delas precisa ser verdadeira (Verdadeiro + Falso ou vice-versa = True
not = inverte o valor do argumento ou expressão (Verdadeiro1 + Falso2 = um resultado (vice-versa = outro valor)

in = Verifica se algo está contido numa variável
not in = Verica se algo não está contido numa variável
"""

# Verdadeiro E Verdadeiro (comparação1 and comparação2) = True
a = 2
b = 2
c = 3
if a == b and b < c:
    print('Verdadeiro')

# Verdadeiro OU Verdadeiro (Qualquer uma das duas que for verdadeira retorna como verdadeiro
a = 2
b = 2
c = 3
if a == b or b < c:
    print('Verdadeiro')

# Not invert a expressão (0 também é considerado vazio)
var_1 = ""
Var_2 = 0
if not var_1:
    print('Por favor preencha o valor')
else:
    print('Prosseguir')

# In e not in retornam a checagem se algo está ou não contido no código
nome = 'Katia'

if 't' in nome:
    print('Esta letra existe em Kátia')
else:
    print('Não existe')


