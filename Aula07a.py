"""
# Operadores Aritméticos com operandos Binários

Operadores Aritméticos Binários

+ Adição
- Subtração
* Multiplicação
/ Divisão
** Potência
// Divisão Inteira
% Resto da divisão

Ordem de Precedência
1 () Parênteses
2 ** Exponencial (ou exemplo pow(4,3)
3 *  /  //  %
4 +  -

Raíz Quadrada
A raíz de 81 é 9
Podemos fazer 81**(1/2)

A raíz cúbica de 127 é 5,026
127**(1/3)

"""

n1 = int(input('Digite um valor: '))
n2 = int(input('Ditite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')  # Para que as informações fiquem
# na mesma linha.
print('Divisão inteira {}, \n e potência {}'.format(di, e))  # Para quebrar a linha, \n
