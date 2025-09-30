import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path

LARGURA, ALTURA = 720, 405
BASE_DIR = Path(__file__).resolve().parent


def criar_janela():
    janela = tk.Tk()
    janela.title("Golden Sword - janela")
    janela.geometry(f"{LARGURA}x{ALTURA}")
    canvas = tk.Canvas(janela, width=LARGURA, height=ALTURA, bg="white")
    canvas.pack()
    return janela, canvas

def criar_fundo(canvas):
    fundo_img = Image.open(rf"{BASE_DIR}\assets\static-assets\fundo.jpg").resize((LARGURA, ALTURA), Image.LANCZOS)
    tk_fundo_img = ImageTk.PhotoImage(fundo_img)
    canvas.create_image(LARGURA/2, ALTURA/2, image=tk_fundo_img, anchor='center')
    canvas.img_ref = tk_fundo_img
    return tk_fundo_img

def criar_btns(canvas):
    btn_iniciar = tk.Button(canvas.master, text="Iniciar Jogo", font=("Arial", 14, "bold"), 
                            bg="gold", fg="black", width=15, command=iniciar_jogo)

    btn_sair = tk.Button(canvas.master, text="Sair", font=("Arial", 14, "bold"), 
                        bg="red", fg="white", width=15, command=canvas.master.destroy)

    # Adiciona os botões ao canvas (um abaixo do outro)
    canvas.create_window(LARGURA/2, ALTURA/2 - 30, window=btn_iniciar)  
    canvas.create_window(LARGURA/2, ALTURA/2 + 30, window=btn_sair)

def iniciar_jogo():
    print("🎮 Iniciando o jogo...")  # Aqui você pode chamar sua função de jogo

def iniciar():
    janela, canvas = criar_janela()
    criar_fundo(canvas)
    criar_btns(canvas)
    janela.mainloop()

if __name__ == "__main__":
    iniciar()
    