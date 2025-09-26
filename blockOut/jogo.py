import tkinter as tk
import random

def iniciar_janela_jogo():

    global x, y, cobra, pilares, coletaveis, bloco, largura, altura, passo, LARGURA_CANVAS, ALTURA_CANVAS

    # Posição inicial do retângulo
    x, y = 16, 16
    bloco = 16
    largura, altura = 1*bloco, 1*bloco
    passo = 1*bloco  # Quantos pixels o retângulo se move
    pilares = []

    LARGURA_CANVAS = 400
    ALTURA_CANVAS = 300

    # Criar a janela principal
    janela = tk.Tk()
    janela.title("Exemplo de Painel com Retângulo")
    janela.geometry("400x300")

    # Criar o Canvas
    painel_desenho = tk.Canvas(janela, width=LARGURA_CANVAS, height=ALTURA_CANVAS, bg="white")
    painel_desenho.pack()
    
    # Garantir que o Canvas receba foco para detectar teclas
    # Forçar foco após abrir a janela
    def focar_janela_jogo():
        janela.lift()           # traz a janela para frente
        janela.focus_force()    # força foco
        painel_desenho.focus_set()  # foca o canvas

    janela.after(100, focar_janela_jogo)

    # Desenhar o retângulo e guardar o ID
    cobra = painel_desenho.create_rectangle(x, y, x + largura, y + altura, fill="red", outline="red")

    def criarColetaveis():
        c = []
        for _ in range(300):
            px = random.choice(range(0, LARGURA_CANVAS - bloco + 1, 16))
            py = random.choice(range(0, ALTURA_CANVAS - bloco + 1, 16))
            # Criar retângulo e guardar ID junto da posição
            ret_id = painel_desenho.create_rectangle(px, py, px + bloco, py + bloco, fill="red", outline="red")
            c.append({"id": ret_id, "x": px, "y": py})
        return c

    def desenharcroba():
        painel_desenho.delete("pilares")  # remove tudo com a tag "pilares"
        for p in pilares:
            px = p['x']
            py = p['y']
            painel_desenho.create_rectangle(px, py, px + bloco, py + bloco, fill="black", outline="black", tags="pilares")

    def gameover():
        janela.destroy()  # encerra o mainloop e fecha a janela

    # Função para mover o retângulo
    def mover(event):
        global x, y
        old_x, old_y = x, y  # guarda posição anterior
        moved = False         # flag para saber se realmente houve movimento
        
        # mover o retângulo
        if event.keysym == 'w' and y - passo >= 0:                  #cima
            y -= passo
            moved = True
        elif event.keysym == 's' and y + altura <= ALTURA_CANVAS:   #baixo
            y += passo
            moved = True
        elif event.keysym == 'a' and x - passo >= 0:                #direita
            x -= passo
            moved = True
        elif event.keysym == 'd' and x + largura <= LARGURA_CANVAS: #esquerda
            x += passo
            moved = True

        if not moved:
            return  # não fez movimento válido, não verifica colisão nem gameover
            

        # verificar colisão com pilares (game over)
        for p in pilares:
            if x == p['x'] and y == p['y']:
                gameover()
                return

        # coletar itens
        for p in coletaveis[:]:
            if x == p['x'] and y == p['y']:
                pilares.append(p)           # adiciona aos já coletados
                painel_desenho.delete(p['id'])
                coletaveis.remove(p)
                break

        # Atualizar posição do retângulo
        desenharcroba()
        painel_desenho.coords(cobra, x, y, x + largura, y + altura)
        
    coletaveis = criarColetaveis()

    # Vincular as teclas ao Canvas
    janela.bind('<Key>', mover)

    # Iniciar o loop principal
    janela.mainloop()
