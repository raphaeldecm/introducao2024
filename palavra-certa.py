import random

numeros = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
random.shuffle(numeros)
tamanho = len(numeros)
visivel = ["*"] * tamanho

pares_encontrados = 0

print("Bem-vindo ao jogo da memória!")
print("Encontre todos os pares de números.")

while pares_encontrados < tamanho // 2:
    
    print("\nEstado atual: ", " ".join(visivel))
    
    try:
        pos1 = int(input(f"Escolha a primeira posição (0 a {tamanho-1}): "))
        pos2 = int(input(f"Escolha a segunda posição (0 a {tamanho-1}): "))

        if pos1 == pos2 or not (0 <= pos1 < tamanho) or not (0 <= pos2 < tamanho):
            print("Escolha posições válidas e diferentes!")
            continue

        visivel[pos1] = str(numeros[pos1])
        visivel[pos2] = str(numeros[pos2])
        print("\nTentativa: ", " ".join(visivel))

        if numeros[pos1] == numeros[pos2]:
            print("Par encontrado!")
            pares_encontrados += 1
        else:
            print("Não formam um par. Tente novamente.")
            visivel[pos1] = "*"
            visivel[pos2] = "*"

    except ValueError:
        print("Por favor, insira apenas números inteiros!")

print("\nParabéns! Você encontrou todos os pares!")
