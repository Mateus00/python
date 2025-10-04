import os
import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path

class Menu:
    BASE_DIR = Path(__file__).resolve().parent
    
    def __init__(self, altura=405, largura=720):
        self._ALTURA, self._LARGURA = altura, largura
        self._janela = tk.Tk()
        self._janela.title("Golden Sword - Menu")
        self._janela.geometry(f"{self._LARGURA}x{self._ALTURA}")
        
        self._canvas = tk.Canvas(
            self._janela,
            width=self._LARGURA,
            height=self._ALTURA,
            bg="white"
        )
        self._canvas.pack()

    def criar_fundo(self, url_fundo_menu=None):
        if url_fundo_menu is None:
            url_fundo_menu = os.path.join(self.BASE_DIR, "assets", "static-assets", "fundo.jpg")

        fundo_img = Image.open(url_fundo_menu).resize((self._LARGURA, self._ALTURA), Image.LANCZOS)
        tk_fundo_img = ImageTk.PhotoImage(fundo_img)

        # Coloca a imagem no canvas
        self._canvas.create_image(self._LARGURA/2, self._ALTURA/2, image=tk_fundo_img, anchor="center")

        # mantém referência para a imagem não ser coletada
        self._canvas.img_ref = tk_fundo_img  
        return tk_fundo_img

    def criar_btns(self, lista_botoes=None):
        if not lista_botoes:
            lista_botoes = [
                {
                    "text": "Iniciar Jogo",
                    "bg": "gold",
                    "fg": "black",
                    "width": 15,
                    "font": ("Arial", 14, "bold"),
                    "command": self.iniciar_jogo
                },
                {
                    "text": "Sair",
                    "bg": "red",
                    "fg": "white",
                    "width": 15,
                    "font": ("Arial", 14, "bold"),
                    "command": self._janela.destroy
                }
            ]
        
        y_inicial = self._ALTURA/2 - 30
        espaco = 50  # distância entre botões

        for i, botao in enumerate(lista_botoes):
            b = tk.Button(self._canvas.master, **botao)
            y_pos = y_inicial + i * espaco
            self._canvas.create_window(self._LARGURA/2, y_pos, window=b)

    def iniciar_jogo(self):
        print("🎮 Iniciando o jogo...")  

    def criar_menu(self):
        self.criar_fundo()
        self.criar_btns()
        self._janela.mainloop()


if __name__ == "__main__":
    menu = Menu()
    menu.criar_menu()
