"""
Cores no terminal
"""

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m !!!'.format(a, b))

# Dicionário de cores:
nome = 'Kátia'
cores = {'limpa':'\033]m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('Prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, cores['amarelo']))
# dá pra colocar as cores dentro das chaves tb.
