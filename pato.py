import random
import time
from colorama import init, Fore



# Inicia o Colorama e reseta a cor automaticamente após cada print.
init(autoreset=True)




# print: exibe mensagens no terminal para apresentar o jogo e as regras.



def mostrar_menu():
    
    print(Fore.GREEN + '==== Jogo Caça ao 🦆 ====')
    print(Fore.BLUE + '01. Iniciar Jogo\n02. Regras\n03. Ranking\n04. Sair')

def mostrar_regras():
    print(Fore.YELLOW + '--- regras---')
    print(Fore.GREEN + ' 1- O jogadore tem 5 disparos;\n 2- O tempo Máximo é de 1 minuto; \n 3- O jogador inicia com 50 pontos, cada erro desconta 10')

def mostrar_ranking():
    print(Fore.YELLOW + "\n--- TOP 10 (Vitórias por menor tempo) ---")
    

    try:
        with open("ranking.txt", "r", encoding="utf-8") as arq:
            vitorias = []

            for registro in arq:

                try: #usado para tratar erros (exceções) e evitar que o programa quebre quando algo inesperado acontece.
                    nome, resultado, tempo = registro.strip().split(";") #.strip() em Python é um método usado para remover espaços (ou outros caracteres) do início e do fim de uma string.
                    #append adiciona elementos ao final de uma lista
                    if resultado.upper() == "VITORIA":
                        vitorias.append((nome, float(tempo)))
                except ValueError:
                    continue

        if not vitorias:
            print(Fore.RED + "Nenhuma vitória registrada ainda.")
            return
        for pos, (nome, tempo) in enumerate(sorted(vitorias, key=lambda x: x[1])[:10], start=1):
            print(Fore.CYAN + f"{pos:02d}. {nome} - {tempo:.2f}s")

            #Essa parte faz o Top 10 ordenado por menor tempo e imprime formatado:
            #sorted(vitorias, key=lambda x: x[1]) ---- ordena a lista pelo 2º item da tupla (tempo).

    except FileNotFoundError:
        print(Fore.RED + "Arquivo ranking.txt ainda não existe.")

def jogar():
    venceu = False
    # input: lê texto digitado pelo usuário (nome do jogador).
    nome = input(Fore.BLUE + "Informe o Nome do Jogador: ")

    # time.time(): pega o horário atual em segundos para medir duração da partida.
    hora_inicial = time.time()

    # ----------- Variáveis ----------------

    # Define o tamanho do tabuleiro (5x5) e quantidade inicial de tiros.
    tamanho = 5
    disparos = 5

    # Tempo máximo da partida em segundos.
    tempo_limite = 60

    # Cria uma matriz 5x5 preenchida com "🌊" usando list comprehension.
    # "for _ in range(tamanho)" repete a linha "tamanho" vezes.

    grid = [["🌊"] * tamanho for _ in range (tamanho)]

    # random.randint(a, b): sorteia inteiro entre a e b (incluindo os dois extremos).
    # Aqui o pato pode cair em qualquer posição válida do grid.

    pato_linha = random.randint(0, tamanho -1)
    pato_coluna = random.randint(0, tamanho -1)

    # Lista para armazenar posições já tentadas e evitar tiro repetido.
    tentativas = []

    # Barra visual do estado dos disparos: índice 0 = sem erro, índice 5 = sem tiros.
    icones = [

        "🏹🏹🏹🏹🏹",
        "💥🏹🏹🏹🏹",
        "💥💥🏹🏹🏹",
        "💥💥💥🏹🏹",
        "💥💥💥💥🏹",
        "💥💥💥💥💥"
    ]


    # ===================status========================

    # def: cria uma função reutilizável para exibir o estado do jogo.
    def mostrar_status():
        # Quantidade de erros = tiros iniciais (5) - tiros atuais.
        erros = 5 - disparos

        # f-string: permite montar texto com variáveis dentro de { }.
        print(Fore.YELLOW + f"Status: {icones[erros]}")
        print(Fore.CYAN + f"Disparos: {disparos}/5")

        print(Fore.GREEN + "Mapa:")
        # for: percorre cada linha da matriz para imprimir o tabuleiro.
        for linha in grid:
            # " ".join(linha): junta os elementos da lista em uma string separada por espaço.
            print(" ".join(linha))

    #----------------Programa principal ---------

    # while True: loop infinito controlado por "break" quando o jogo termina.

    while True:
        # Atualiza o tempo a cada rodada.
        tempo_atual = time.time()
        tempo_passado = tempo_atual - hora_inicial
        tempo_restante = tempo_limite - tempo_passado

        # if: condição para encerrar se o tempo acabou.
        if tempo_restante <= 0:
            print(Fore.RED + "⏱️ Tempo esgotado!")
            break  # break: sai do loop imediatamente.

        # if: condição para encerrar se não há mais disparos.
        if disparos == 0:
            print(Fore.RED + "💥 Você não tem mais disparos")
            break

        # Mostra painel de status da rodada.
        mostrar_status()

        # int(...) converte o tempo para inteiro só para exibição (sem casas decimais).
        print(Fore.YELLOW + f"Tempo restante: {int(tempo_restante)}s")

        # try/except: trata erro caso o usuário digite algo que não seja número.
        try:
            # int(input(...)): lê texto e converte para inteiro.
            linha = int(input("Linha (0 a 4): "))
            coluna = int(input("Coluna (0 a 4): "))
        except ValueError:
            print(Fore.RED + "Entrada inválida!")
            continue  # continue: pula para a próxima volta do loop.

        # Valida se o tiro está dentro dos limites do grid.

        # or: basta uma das condições ser verdadeira para ser posição inválida.
        if linha < 0 or linha >= tamanho or coluna < 0 or coluna >= tamanho:
            print(Fore.RED + "Posição fora do grid!")
            continue

        # in: verifica se a tupla já existe na lista de tentativas.
        if (linha, coluna) in tentativas:
            print(Fore.RED + "Você já atirou nessa posição!")
            continue

        # abs(x): valor absoluto. Aqui usamos distância Manhattan:
        # |linha_atual - linha_pato| + |coluna_atual - coluna_pato|.
        distancia = abs(linha - pato_linha) + abs(coluna - pato_coluna)

        # if / elif / else: escolhe a dica de proximidade conforme a distância.
        if distancia == 1:
            print("🔥 Muito perto!")
        elif distancia <= 2:
            print("🌡️ Perto!")
        else:
            print("❄️ Longe!")

        # append: adiciona a tentativa atual no fim da lista.
        tentativas.append((linha, coluna))

        # Verifica acerto exato (linha e coluna iguais às do pato).
        if linha == pato_linha and coluna == pato_coluna:
            # Atualiza o grid para mostrar o pato onde acertou.
            grid[linha][coluna] = "🦆"
            print(Fore.GREEN + f"\nParabéns {nome}! Você acertou o pato! 🦆🎉")
            venceu = True
            break
        else:
            # Marca erro no grid, remove um disparo e informa água.
            grid[linha][coluna] = "X"
            disparos -= 1
            print(Fore.RED + "💥 Água!")

# Após sair do loop, revela o pato se o jogo terminou por derrota (tempo ou tiros).
    if disparos == 0 or tempo_restante <= 0:
        grid[pato_linha][pato_coluna] = "🦆"
        print(Fore.YELLOW + f"O pato estava em ({pato_linha}, {pato_coluna})")

# Calcula e mostra a duração total da partida.
    hora_final = time.time()
    duracao = hora_final - hora_inicial
    print(f"Jogo durou: {duracao:.2f} segundos")

# with open(..., "a"): abre/cria arquivo em modo append (adiciona no final sem apagar).
    with open("ranking.txt", "a") as arq:
        # Operador ternário: escolhe "VITORIA" se acertou, senão "DERROTA".
        resultado = "VITORIA" if venceu else "DERROTA"
        # write: grava uma linha no formato nome;resultado;duracao.
        arq.write(f"{nome};{resultado};{duracao:.2f}\n")

while True:
    mostrar_menu()

    try:
        comando = int(input(Fore.GREEN + 'Digite a opção: '))
    except ValueError:
        print(Fore.RED + 'Erro... valor inválido')
        continue
    if comando == 1:
        jogar()
    elif comando == 2:
        mostrar_regras()
    elif comando == 3:
        mostrar_ranking()
    elif comando == 4:
        print(Fore.CYAN + 'Saindo .... Obrigado por jogar!')
        break
    else:
        print(Fore.RED + 'Erro... valor inválido, escolha entre 1 e 4')

