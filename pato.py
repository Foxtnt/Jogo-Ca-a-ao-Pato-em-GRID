import random
import time
from colorama import init, Fore



init(autoreset=True)

print(Fore.GREEN + '==== Jogo Caça ao 🦆 ====')
print(Fore.YELLOW + '--- regras---')
print(Fore.GREEN + ' 1- O jogadore tem 5 disparos;\n 2- O tempo Máximo é de 1 minuto; \n 3- O jogador inicia com 50 pontos, cada erro desconta 10')

nome = input(Fore.BLUE + "Informe o Nome do Jogador: ")

hora_inicial = time.time()

# ----------- Variáveis ----------------

tamanho = 5
disparos = 5

tempo_limite = 60

# essa linha completa linhas em colunas com a quantidade de 5x5 de ondas

grid = [["🌊"] * tamanho for _ in range (tamanho)]

# sorteio da posição do pato

pato_linha = random.randint(0, tamanho -1)
pato_coluna = random.randint(0, tamanho -1)

tentativas = []

icones = [

    "🏹🏹🏹🏹🏹",
    "💥🏹🏹🏹🏹",
    "💥💥🏹🏹🏹",
    "💥💥💥🏹🏹",
    "💥💥💥💥🏹",
    "💥💥💥💥💥"
]


# ===================status========================

#def usado para definir uma função ou seja, nesse caso você pode usala varias vezes chamando mostrar_status()
def mostrar_status():
    erros = 5 - disparos
    print(Fore.YELLOW + f"Status: {icones[erros]}")
    print(Fore.CYAN + f"Disparos restantes: {disparos}/5")

    print(Fore.GREEN + "Mapa:")
    for linha in grid:
        print(" ".join(linha))

#----------------Programa principal ---------

#while vai rodar o programa enquanto o tempo for verdadeiro, ou seja dentro de 60 segundos, sempre descontando

while True:
    tempo_atual = time.time()
    tempo_passado = tempo_atual - hora_inicial
    tempo_restante = tempo_limite - tempo_passado

    #verifica o tempo
    if tempo_restante <= 0:
        print(Fore.RED + "⏱️ Tempo esgotado!")
        break
    #verificar se tem disparos
    if disparos == 0:
        print(Fore.RED + "💥 Você não tem mais disparos")
        break

    mostrar_status()

    print(Fore.YELLOW + f"Tempo restante: {int(tempo_restante)}s")

    try:
        linha = int(input("Linha (0 a 4): "))
        coluna = int(input("Coluna (0 a 4): "))
    except ValueError:
        print(Fore.RED + "Entrada inválida!")
        continue

    # validação

    if linha < 0 or linha >= tamanho or coluna < 0 or coluna >= tamanho:
        print(Fore.RED + "Posição fora do grid!")
        continue

    if (linha, coluna) in tentativas:
        print(Fore.RED + "Você já atirou nessa posição!")
        continue

    # Dica de proximidade calculada com base no tiro atual.
    distancia = abs(linha - pato_linha) + abs(coluna - pato_coluna)

    if distancia == 1:
        print("🔥 Muito perto!")
    elif distancia <= 2:
        print("🌡️ Perto!")
    else:
        print("❄️ Longe!")

    tentativas.append((linha, coluna))

        # verifica acerto
    if linha == pato_linha and coluna == pato_coluna:
        grid[linha][coluna] = "🦆"
        print(Fore.GREEN + f"\nParabéns {nome}! Você acertou o pato! 🦆🎉")
        break
    else:
        grid[linha][coluna] = "X"
        disparos -= 1
        print(Fore.RED + "💥 Água!")

# revela posição se perdeu
if disparos == 0 or tempo_restante <= 0:
    grid[pato_linha][pato_coluna] = "🦆"
    print(Fore.YELLOW + f"O pato estava em ({pato_linha}, {pato_coluna})")

hora_final = time.time()
duracao = hora_final - hora_inicial
print(f"Jogo durou: {duracao:.2f} segundos")

with open("ranking.txt", "a") as arq:
    resultado = "VITORIA" if (linha == pato_linha and coluna == pato_coluna) else "DERROTA"
    arq.write(f"{nome};{resultado};{duracao:.2f}\n")