import random
import time
from colorama import init, Fore



init(autoreset=True)

print(Fore.GREEN + '==== Jogo Caça ao 🦆 ====')
print(Fore.YELLOW + '--- regras---')
print(Fore.GREEN + ' 1- O jogadore tem 5 disparos;\n 2- O tempo Máximo é de 1 minuto; \n 3- O jogador inicia com 50 pontos, cada erro desconta 10')

nome = input(Fore.BLUE + "Informe o Nome do Jogador: ")

hora_inicial = time.time()