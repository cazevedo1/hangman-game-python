palavraCerta = "abacate"

tentativas = 6

chutesErrados = []

letrasDescobertas = ["_"] * len(palavraCerta)

print("JOGO DA FORCA")
print("-" * 40)

while tentativas > 0 and "_" in letrasDescobertas:
    print("\nPalavra:", " ".join(letrasDescobertas))
    print("Tentativas Restantes: ", tentativas)
    print("Letra usadas: ", chutesErrados)

    letra = input("Digite uma letra: ").lower()

    if letra in palavraCerta:
        for i in range(len(palavraCerta)):
            if palavraCerta[i] == letra:
                letrasDescobertas[i] = letra
        print("Você acertou uma letra!")
    else:
        tentativas -= 1
        print("Letra Errada!")
        chutesErrados.append(letra)
        print(chutesErrados)

if "_" not in letrasDescobertas:
    print("\nParabéns! Você ganhou!")
    print("\nA palavra é: ", palavraCerta)
else:
    print("\nVocê Perdeu! A palavra era: ", palavraCerta)
