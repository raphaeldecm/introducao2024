# Crie uma lista com os números de 1 a 5 e exiba o terceiro elemento.
L1 = [1, 2, 3, 4, 5]
print(L1[2])

# Crie uma lista com os números [10, 20, 30, 40]. Substitua o segundo número pelo valor 25.
L2 = [10, 20, 30, 40]
L2[1] = 25
print(L2)

# Crie uma lista vazia. Adicione os valores 5, 10, 15 à lista, um de cada vez.
L3 = []
L3.append(5)
L3.append(10)
L3.append(15)
print(L3)

# Crie uma lista com os números [1, 2, 3, 4, 5]. Remova o número 3 da lista.
L4 = [1, 2, 3, 4, 5]
del L4[2]
print(L4)

# Crie uma lista com os elementos ['a', 'b', 'c', 'd'] e exiba o tamanho da lista.
L5 = ['a', 'b', 'c', 'd']
print(len(L5))

# Receba dez números do usuário e armazene em uma lista vazia. Em seguida, exiba cada número multiplicado por 2.
numeros1 = []
for i in range(10):
    numero = int(input("Digite um número: "))
    numeros1.append(numero)
for numero in numeros1:
    print(numero*2)

# Receba dez números do usuário e armazene em uma lista vazia. Em seguida, exiba a soma de todos os números.
numeros2 = []
soma = 0
for i in range(10):
    numero = int(input("Digite um número: "))
    numeros2.append(numero)
    soma += numero
print(soma)

# Receba dez números do usuário e armazene em uma lista vazia. Em seguida, verifique se o valor 200 está na lista.
numeros3 = []
for i in range(10):
    numero = int(input("Digite um número: "))
    numeros3.append(numero)
if 200 in numeros3:
    print("O valor 200 está na lista")
else:
    print("O valor 200 não está na lista")

# Receba dez números do usuário e armazene em uma lista vazia. Exiba o último elemento usando indexação negativa.
numeros4 = []
for i in range(10):
    numero = int(input("Digite um número: "))
    numeros4.append(numero)
print(numeros4[-1])

# Crie uma lista com os elementos ['python', 'java', 'c++']. Exiba os elementos na ordem inversa.
L6 = ['python', 'java', 'c++']
# Start = tamanho da lista - 1, 
# Stop = -1 (incluir até o primeiro elemento),
# Step = -1 (diminuir um elemento por vez),
for i in range(len(L6)-1, -1, -1): 
    print(L6[i])

# Receba dez números do usuário e armazene em uma lista vazia. Em seguida, exiba apenas os números pares.
numeros5 = []
for i in range(10):
    numero = int(input("Digite um número: "))
    numeros5.append(numero)
for numero in numeros5:
    if numero % 2 == 0:
        print(numero)

# Crie duas listas: [1, 2, 3] e [4, 5, 6]. Junte as duas listas em uma única lista.
L7 = [1, 2, 3]
L8 = [4, 5, 6]
L9 = L7 + L8
print(L9)

# Crie uma lista com os números [10, 20, 30]. Faça uma cópia da lista e altere o primeiro elemento da cópia para 15. Exiba as duas listas.
L10 = [10, 20, 30]
L11 = L10.copy()
L11[0] = 15
print(L10)
print(L11)

# Crie uma lista com os números [5, 10, 15, 20]. Remova o elemento na posição 2.
L12 = [5, 10, 15, 20]
del L12[2]
print(L12)

# Crie uma lista com os elementos ['a', 'b']. Repita a lista 3 vezes.
L13 = ['a', 'b']
L14 = L13*3
print(L14)

# Receba três número do usuário e armazene em uma lista vazia. Em seguida, ordene-os em ordem crescente e apresente o resultado.
numeros6 = []
aux = 0
for i in range(3):
    numero = int(input("Digite um número: "))
    numeros6.append(numero)
for i in range(3):
    for j in range(3):
        if numeros6[i] < numeros6[j]:
            aux = numeros6[i]
            numeros6[i] = numeros6[j]
            numeros6[j] = aux

# Receba dez números do usuário e armazene em uma lista vazia. Em seguida, exiba o maior e o menor número da lista.
numeros7 = []
for i in range(10):
    numero = int(input("Digite um número: "))
    numeros7.append(numero)

maior = numeros7[0]
menor = numeros7[0]
for numero in numeros7:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

# Crie uma lista com os números [1, 2, 2, 3, 3, 4]. Remova os valores duplicados.
L15 = [1, 2, 2, 3, 3, 4]
L16 = []
for numero in L15:
    if numero not in L16:
        L16.append(numero)

# Crie uma lista com os números [1, 2, 2, 3, 4, 4, 4]. Conte quantas vezes o número 4 aparece.
L17 = [1, 2, 2, 3, 4, 4, 4]
cont = 0
for numero in L17:
    if numero == 4:
        cont += 1

# Crie uma lista com os números [10, 20, 30]. Insira o número 25 na posição correta para manter a lista ordenada.
L18 = [10, 20, 30]
numero = 25
for i in range(3):
    if numero < L18[i]:
        L18.insert(i, numero)
        break

