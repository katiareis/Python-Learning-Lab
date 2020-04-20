"""
Trabalhando com módulos

Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python.
Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos
built-in e módulos externos, oferecidos no Pypi (pacotes extras).

import *** Importa tudo que vem no módulo
from .... import **** Importa algo dentro de um módulo de forma específica.

Ex: import math ( importa tudo)
from math import sqrt, ceil, ... ( importa só o que está entre vírgulas)

Módulo math
função ceil
função floor
função trunc
função pow
função sqrt
função factorial

Para verificar quais módulos estão intalados no meu pycharm.
Clicar em file e depois em settings. ProjectPycharm: projects e depois em pycharm interpreter. Clicar no sinal de + para
ver as possibilidades de módulos externos a serem baixados. Também é possível ver essas infos no site.

"""
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, math.ceil(raiz)))   # .ceil = arredondamento para cima

from math import floor, sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))   # apertar ctrl + space mostra todas as funcionalidades
