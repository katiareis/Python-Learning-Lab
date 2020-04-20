# métodos de teste

n = input('Digite um valor:')
print(type(n))

algo = input('Digite algo:')
print(n.isnumeric())  # O método isnumeric diz se é possível converter o valor em int.
print(n.isalnum())    # O método isalnum diz se é possível converter o valor em str.
print(n.isalpha())
print(n.isupper())
print(n.islower())
print(n.istitle())
