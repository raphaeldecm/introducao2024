# Escreva um programa que receba uma operação (+, -, *, /, sair) e dois números inteiros como entrada do usuário e exiba o resultado da operação. O programa deve realizar operações até que o usuário digite sair para a operação. Se o operador digitado for inválido, mostre uma mensagem de erro. Se o usuário tentar realizar uma divisão por zero, mostre uma mensagem de erro.

while True:
    operacao = input("Digite a operação (+, -, *, /, sair):").lower()
    
    if operacao == "sair":
        break
    
    if operacao not in ["+", "-", "*", "/"]:
        print("Operação inválida!")
    
    else:
      num1 = int(input("Digite o primeiro número:"))
      num2 = int(input("Digite o segundo número:"))
      
      if operacao == "+":
          print(num1 + num2)
      elif operacao == "-":
          print(num1 - num2)
      elif operacao == "*":
          print(num1 * num2)
      elif operacao == "/":
        if num2 == 0:
            print("Divisão por zero!")
        else:
          print(num1 / num2)
      
print("Fim da operação")

# Crie um programa que: Leia as notas de 10 alunos e armazene-as em uma lista (10 pontos). 
# Em seguida: Exiba a maior nota (10 pontos); Exiba a menor nota (10 pontos); Calcule e mostre a média das notas (5 pontos).
# obs: Os itens i e ii devem ser respondidos manualmente, sem utilização de funções de apoio como max e min.

notas = []
for i in range(10):
    notas.append(float(input(f"Digite a nota do aluno {i+1}:")))

maior = notas[0]
menor = notas[0]
soma = 0
for nota in notas:
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota
    soma += nota
print("Maior nota:", maior)
print("Menor nota:", menor)
print("Média:", soma / len(notas))

# Elabore um programa que simule uma loja de roupas. O programa deve conter um dicionário com os produtos e seus preços: estoque = {"camiseta": 50, "calça": 100, "casaco": 150, “sapato”: 120, “bolsa”: 110, “meia": 20}. O usuário pode:
# Visualizar os produtos disponíveis e seus preços (10 pontos).
# Adicionar um produto ao carrinho digitando o nome do produto e a quantidade (10 pontos).
# Quando o usuário digitar "sair", o programa deve mostrar:
# Os itens comprados e suas quantidades (10 pontos).
# O valor total da compra (10 pontos).

estoque = {"camiseta": 50, "calça": 100, "casaco": 150, "sapato": 120, "bolsa": 110, "meia": 20}
carrinho = {}
soma = 0
while True:
    print("Produtos disponíveis:")
    for produto, preco in estoque.items():
        print(f"{produto}: R$ {preco:.2f}")
    
    produto = input("Digite o nome do produto ou sair:").lower()
    if produto == "sair":
        break
    
    if produto in estoque:
        quantidade = int(input("Digite a quantidade:"))
        soma = soma + (estoque[produto] * quantidade)
        
        if produto in carrinho:
            carrinho[produto] = carrinho[produto] + quantidade
        else:
            carrinho[produto] = quantidade
    else:
        print("Produto não encontrado!")

print("Itens comprados:")
for produto, quantidade in carrinho.items():
        print(f"{produto}: Quantidade {quantidade}")
print("Valor total da compra: R$ %.2f" % soma)