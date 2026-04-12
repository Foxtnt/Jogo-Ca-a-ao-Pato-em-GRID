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

    "🏹🏹🏹🏹🏹"
    "💥🏹🏹🏹🏹"
    "💥💥🏹🏹🏹"
    "💥💥💥🏹🏹"
    "💥💥💥💥🏹"
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

