tabela = {
   "Alface": 0.45,
   "Batata": 1.20,
   "Tomate": 2.30,
   "Feijão": 1.50
}
print(tabela["Tomate"])
# Saída: 2.3

print(tabela)
# Saída: {'Batata': 1.2, 'Alface': 0.45, 'Tomate': 2.3, 'Feijão': 1.5}
tabela["Tomate"] = 2.50
print(tabela["Tomate"])
# Saída: 2.5

# Perdemos a noção de ordem ao utilizar dicionários.
print(tabela)
# Saída: {'Batata': 1.2, 'Alface': 0.45, 'Tomate': 2.3, 'Feijão': 1.5}
tabela["Cebola"] = 1.20
print(tabela)
# Saída {'Batata': 1.2, 'Alface': 0.45, 'Tomate': 2.5, 'Cebola': 1.2, 'Feijão': 1.5}

# Verificar se uma chave existe, antes de acessá-la
print(tabela)
# Saída: {'Batata': 1.2, 'Alface': 0.45, 'Tomate': 2.3, 'Feijão': 1.5}
print(tabela["Manga"])
# Saída: Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# KeyError: 'Manga'
print("Manga" in tabela)
# Saída: False
print("Batata" in tabela)
# Saída: True

# lista de chaves ou lista dos valores do dicionário
print(tabela.keys())
#dict_keys(['Batata', 'Alface', 'Tomate', 'Feijão'])
print(tabela.values())
#dict_values([1.2, 0.45, 2.3, 1.5])
print(tabela.items())
#dict_items([('Batata', 1.2), ('Alface', 0.45), ('Tomate', 2.3), ('Feijão', 1.5])

# Apagar uma chave utilizando a instrução del
del tabela["Tomate"]
print(tabela)
# Saída:
# {'Batata': 1.2, 'Alface': 0.45, 'Feijão': 1.5}

# Iterando em dicionários
# Iterar sobre chaves
for chave in tabela.keys():
   print(chave)

# Iterar sobre valores
for valor in tabela.values():
   print(valor)

# Iterar sobre pares chave-valor
for chave, valor in tabela.items():
   print(f"{chave}: {valor}")
