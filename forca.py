secreto = "cobertor"
digitadas= []
chances = 3

while True:
    if chances <= 0:
        print("Você perdeu!!")

    letra = input("Digite uma letra: ")
    if len(letra) > 1:
        print("isso não vale, digite apenas uma letra")

    digitadas.append(letra)
    if letra in secreto:
        print(f"Parabéns, a letra '{letra}' existe na palavra secreta!!")
    else:
        print(f"OPS, a letra '{letra}' não existe na palavra secreta")
        digitadas.pop()

    secreto_temporario = ""
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += "_"

    if secreto_temporario == secreto:
        print(f"Que legal! Você ganhou! a palavra secreta era {secreto_temporario}")
        break
    else:
        print(f"A palavra secreta esta assim {secreto_temporario}")

    if letra not in secreto:
        chances -= 1
    print(f"Você ainda tem {chances} chances")
    print("")