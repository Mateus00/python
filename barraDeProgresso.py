import time

# Códigos ANSI para cores
VERDE = "\033[92m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"
RESET = "\033[0m"

def barra_progresso(total=20, tempo=0.2):
    for i in range(total + 1):
        porcentagem = int((i / total) * 100)
        barra = "#" * i + "-" * (total - i)  # # preenchido, - vazio
        print(f"\r[{barra}] {porcentagem}%", end="", flush=True)
        time.sleep(tempo)
    print()  # pula linha no fina


def barra_progresso_colorida(total=30, tempo=0.1):
    for i in range(total + 1):
        porcentagem = int((i / total) * 100)

        # Decide a cor pela porcentagem
        if porcentagem < 50:
            cor = VERMELHO
        elif porcentagem < 80:
            cor = AMARELO
        else:
            cor = VERDE

        barra = "#" * i + "-" * (total - i)
        print(f"\r{cor}[{barra}] {porcentagem}%{RESET}", end="", flush=True)
        time.sleep(tempo)

    print()  # quebra de linha no final

barra_progresso()

barra_progresso_colorida()