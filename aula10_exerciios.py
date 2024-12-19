# Lista de produtos
tabela = { "Alface": 0.45, "Batata": 1.20, "Tomate": 2.30, "Feijão": 1.50 }
while True:
   produto=input("Digite o nome do produto ou fim:").capitalize()
   if produto == "Fim":
       break
   if produto in tabela:
       print("Preço %5.2f" % tabela[produto])
   else:
       print("Produto não encontrado!")
print("Fim da consulta")

# Questão 1. Defina um dicionário com as informações de nome, idade, e cidade de uma pessoa qualquer. O programa deve solicitar ao usuário qual informação deve ser apresentada ou digitar fim para sair. 

pessoas = { "nome": "João", "idade": 25, "cidade": "São Paulo" }
while True:
   informacao=input("Digite o nome da informação ou fim:")
   if informacao.lower() == "fim":
       break
   if informacao in pessoas:
       print(pessoas[informacao])
   else:
       print("Informação não encontrada!")
print("Fim da consulta")

# # Questão 2. Como você pode adicionar um novo par chave-valor ao dicionário abaixo? Complete o código para adicionar a chave "curso" com o valor "Python Básico": aluno = {"nome": "Ana", "idade": 19}

aluno = { "nome": "Ana", "idade": 19 }
aluno["curso"] = "Python Básico"
print(aluno)

# # Questão 3. Escreva um programa que gere um dicionário, onde cada chave seja um caractere, e seu valor seja o número desse caractere encontrado em uma frase lida. Exemplo: O rato -> { “O”:1, “r”:1, “a”:1, “t”:1, “o”:1}

frase = input("Digite uma frase:")
contagem = {}
for letra in frase:
   if letra in contagem:
       contagem[letra] += 1
   else:
       contagem[letra] = 1
print(contagem)

