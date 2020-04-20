"""
Cores no terminal
Código ANSI para cores -  o melhor que funciona em python é o que começa com 033 conforme abaixo:

ANSI escape sequence

\033[ + estilo da letra + cor do texto + cor do fundo + m

Códigos que melhor funcionam em python:
STYLE = 0(none) , 1(negrito) , 4(sublinado) , 7(inverte)
TEXT = 30(branco), 31(vermelho), 32(verde), 33(amarelo), 34(azul), 35(rosa), 36(azul céu), 37(cinza)
BACKGROUND = 40(branco), 41(vermelho), 42(verde), 43(amarelo), 44(azul), 45(rosa), 46(azul céu), 47(cinza)

\033[m    # desfaz as coonfigurações e retorna às cores do terminal


print('\033[0;30;41mTESTE')   # Sem estilo, texto em branco, fundo vermelho
print('\033[4;33;44mTESTE')   # Sublinhado, texto em amarelo, fundo azul
print('\033[1;35;43mTESTE')   # Em negrito, texto em rosa, fundo amarelo
print('\033[30;42mTESTE')   # Sem estilo se eu omitir, texto em branco, fundo verde
print('\033[mTESTE')   # Sem estilo, fundo preto e letra cinza.
print('\033[7;30m')   # Inverte o fundo e a letra. Fica letra preta e fundo branco.

"""
print('\033[7;30mOlá, mundo!')   # Letra preta e fundo branco, e a formatação até o fim da linha.
print('\033[7;30mOlá, mundo!\033[m')   # Letra preta e fundo branco, e a formatação centralizado no texto.
