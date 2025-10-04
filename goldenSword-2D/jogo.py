import tkinter as tk
from PIL import Image, ImageTk
import os

BASE_DIR = os.path.dirname(__file__)

class Jogo:
    def __init__(self, root):
        self.root = root
        self._LARGURA = 800
        self._ALTURA = 600
        self.canvas = tk.Canvas(root, width=self._LARGURA, height=self._ALTURA)
        self.canvas.pack()
        self.botoes = []
        self.player_img = BASE_DIR+'/assets/static-assets/player.png'
        self.player = None

        # fundo
        self.fundo_img = None
        self.fundo1 = None
        self.fundo2 = None
        self.velocidade_fundo = 2  # pixels por atualização

        self.criar_fundo(self.canvas)  # fundo inicial
        self.criar_menu(self.canvas)   # menu inicial

    def criar_fundo(self, canvas, url_fundo_menu=BASE_DIR+'/assets/static-assets/fundo.jpg'):
        """Renderiza duas imagens lado a lado para simular movimento infinito"""
        img = Image.open(url_fundo_menu)
        img = img.resize((self._LARGURA, self._ALTURA))
        self.fundo_img = ImageTk.PhotoImage(img)

        # Cria duas imagens lado a lado
        self.fundo1 = canvas.create_image(0, 0, image=self.fundo_img, anchor="nw")
        self.fundo2 = canvas.create_image(self._LARGURA, 0, image=self.fundo_img, anchor="nw")

    def passar_fundo(self):
        """Move o fundo infinitamente para a esquerda"""
        # Move as duas imagens
        self.canvas.move(self.fundo1, -self.velocidade_fundo, 0)
        self.canvas.move(self.fundo2, -self.velocidade_fundo, 0)

        # Pega posição atual
        x1 = self.canvas.coords(self.fundo1)[0]
        x2 = self.canvas.coords(self.fundo2)[0]

        # Se uma sair da tela, reposiciona atrás da outra
        if x1 <= -self._LARGURA:
            self.canvas.move(self.fundo1, self._LARGURA*2, 0)
        if x2 <= -self._LARGURA:
            self.canvas.move(self.fundo2, self._LARGURA*2, 0)

        # chama novamente
        self.root.after(30, self.passar_fundo)  # 30ms = ~33fps

    def criar_menu(self, canvas):
        """Cria os botões do menu"""
        lista_botoes = [
            {"text": "Iniciar Jogo", "bg": "gold", "fg": "black", "font": ("Arial", 14, "bold"),
             "width": 15, "command": self.iniciar_jogo}
        ]

        for botao in lista_botoes:
            b = tk.Button(canvas.master, **botao)
            self.botoes.append(b)
            canvas.create_window(self._LARGURA/2, self._ALTURA/2, window=b)

    def iniciar_jogo(self):
        """Remove botões e renderiza o player"""
        for b in self.botoes:
            b.destroy()
        self.botoes.clear()

        # Renderiza o player no centro
        img = Image.open(self.player_img)
        img = img.resize((96, 135))
        self.player_img = ImageTk.PhotoImage(img)
        
        self.player = self.canvas.create_image(50, self._ALTURA-185, image=self.player_img)

        # Inicia movimento do fundo
        self.passar_fundo()

        print("Jogo iniciado!")

if __name__ == "__main__":
    root = tk.Tk()
    app = Jogo(root)
    root.mainloop()
