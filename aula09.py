# Crie um programa que encontre o menor e maior valor na lista L=[5, 6, 4, 3, 10, 16, 2, 1]
L=[5, 6, 4, 3, 10, 16, 2, 1]
max = L[0]
min = L[0]
for elemento in L:
    if elemento > max:
        max = elemento
    if elemento < min:
        min = elemento
print(f"O maior valor é {max} e o menor valor é {min}")

# A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [ -10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.
T = [ -10, -8, 0, 1, 2, 5, -2, -4]
max = T[0]
min = T[0]
soma = 0
for temperatura in T:
    soma += temperatura
    if temperatura > max:
        max = temperatura
    if temperatura < min:
        min = temperatura
media = soma/len(T)
print(f"A maior temperatura é {max}, a menor temperatura é {min} e a média das temperaturas é {media}")

# Crie um programa que receba uma lista com números digitados pelo usuário. O programa deve parar ao digitar o número zero. Além disso, deve separar os números em outras duas lista contendo os números pares e ímpares digitados.
numeros = []
pares = []
impares = []
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    numeros.append(numero)
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f"Os números digitados foram {numeros}")
print(f"Os números pares são {pares} e os números ímpares são {impares}")
