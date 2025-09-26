import tkinter as tk
import jogo  # importa o outro arquivo do jogo

def iniciar_jogo():
    # chama a função que inicia o jogo no outro arquivo
    jogo.iniciar_janela_jogo()

def sair_jogo():
    menu.destroy()

# Criar janela do menu
menu = tk.Tk()
menu.title("Menu do Jogo")
menu.geometry("300x200")

# Título
titulo = tk.Label(menu, text="Meu Jogo da Cobra", font=("Arial", 16))
titulo.pack(pady=20)

# Botão iniciar
btn_iniciar = tk.Button(menu, text="Iniciar Jogo", font=("Arial", 12), command=iniciar_jogo)
btn_iniciar.pack(pady=10)

# Botão sair
btn_sair = tk.Button(menu, text="Sair", font=("Arial", 12), command=sair_jogo)
btn_sair.pack(pady=10)

menu.mainloop()