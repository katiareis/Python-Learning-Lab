"""
Manipulando Strings

Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento
de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(),
strip(), junção com join().

frase[1:2:3] - 1 é o início da STR, 2 é o final da STR, 3 é quantas casas deve pular.

frase = "Curso em Video Python"

# Fatiamento de str
print(frase[9])  # Fatiamento com o número do índice
print(frase[9:13])   # Fatiamento de range (com início e fim). O 13 fica de fora.
print(frase[9:21])   # Começa o 9 e vai até o 20.
print(frase[9:21:2])   # Vai do 9 ao 20 de 2 em 2.
print(frase[:5])   # Quando eu não coloco onde é para começar, ele começa do 0 até 4.
print(frase[15:])   # Indica o início mas omite o final. Python vai mostrar até o final da str.
print(frase[9::3])   # Indica que deve iniciar no 9, omitindo o final, pulando de 3 em 3 letras.

# Análise de str
print(len(frase))   # A função len mostra o comprimento da str.
print(frase.count('o'))   # A função .count() conta quantas vezes aparece alguma coisa dentro da str.
print(frase.count('o', 0, 13))   # A função .count() + fatiamento. Dentro do range de 0 ao 12, qtos "o" aparecem.
print(frase.find('deo'))    # .find vai dizer qtas vezes ele encontrou a palavra 'deo', começando na posição 11.
print(frase.find('Android'))    # Se vc colocar no .find um parâmetro que não existe na str, ele retorna com -1 (não existe)
print('Curso'in frase)  # Operador in = Existe curso em frase? retorna True ou False.

# Transformação de str
print(frase.replace('Python', 'Androide'))  # Método replace = Onde houver 'Python', vai trocar por 'Androide'.
print(frase.upper())    # Este método põe tudo em maiúsculo.
print(frase.lower())    # Este método de tranformação de str põe tudo em minúsculo.
print(frase.capitalize())   # Joga tudo para minúsculo e coloca só a primeira letra em maiúscula.
print(frase.title())    # Joga a primeira letra de cada palavra em maiúscula.
print(frase.strip())    # Remove espaços vazios e desnecessários nas expremidades.
print(frase.rstrip())   # Remove espaços vazios à direita.
print(frase.lstrip())   # Remove espaços vazios à esquerda.

# Divisão de str
print(frase.split())    # Split gera tecnicamente um lista com a str. As palavras dentro da str separadas usando como referência os espaços entre os caracteres.
print('-'.join(frase))  # Join realiza a junção de itens que foram splitados em uma str. O que for solicitado entre aspas ser´o separados dos itens na nova str.
"""

# Exercícios da aula

frase = "Curso em Video Python"
print(frase.upper().count('O'))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print(frase.lower().find('video'))
print('Curso'in frase)
print(frase.find('Curso'))

print(frase.split())
frase_splitada = frase.split()
print(frase_splitada[2][3])

