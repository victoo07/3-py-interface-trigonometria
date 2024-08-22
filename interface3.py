import tkinter as tk
import math
from PIL import Image, ImageTk
import os
import sys

def resource_path(relative_path):
    """
    Obtém o caminho absoluto para o recurso, funciona tanto em ambiente de desenvolvimento quanto após o empacotamento com PyInstaller. 
    """
    try:
        base_path = sys._MEIPASS

    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def calcular():
    """
    Realiza o cálculo dos valores trigonométricos (seno, cosseno e tangente) do ângulo fornecido
    """
    try:
        angulo = float(entrada_angulo.get())
        radiano = math.radians(angulo)

        seno = math.sin(radiano)
        cosseno = math.cos(radiano)
        tangente = math.tan(radiano)

        resultado_seno.config(text=f"{seno:.3f}")
        resultado_cosseno.config(text=f"{cosseno:.3f}")
        resultado_tangente.config(text=f"{tangente:.3f}")

    except ValueError:

        resultado_seno.config(text="Erro")
        resultado_cosseno.config(text="Erro")
        resultado_tangente.config(text="Erro")

def limpar():
    """
    Limpa a entrada do usuário e reseta as labels dos resultados.
    """
    entrada_angulo.delete(0, tk.END)
    resultado_seno.config(text="")
    resultado_cosseno.config(text="")
    resultado_tangente.config(text="")

def validar_entrada(texto):
    """
    Valida a entrada do usuário permitindo apenas número e garantindo que o valor esteja entre 0 e 90
    """
    if texto.isdigit() or texto == "":
        if texto == "":
            return True
        valor = int(texto)
        return 0 <= valor <= 90
    return False

janela = tk.Tk()
janela.title("Calculadora Trigonométrica")
janela.geometry("400x550")
janela.configure(bg="#f0f0f0")

try:
    icone_path = resource_path("seno.png")
    icone = Image.open(icone_path)
    icone = ImageTk.PhotoImage(icone)
    janela.iconphoto(True, icone)
except FileNotFoundError:
    print("Imagem 'seno.png' não encontrada para o ícone")

try:
    imagem_path = resource_path("seno2.png")
    imagem = Image.open(imagem_path)
    imagem = imagem.resize((380, 200), Image.LANCZOS)
    foto = ImageTk.PhotoImage(imagem)
    label_imagem = tk.Label(janela, image=foto, bg="#f0f0f0", borderwidth=0)
    label_imagem.image = foto
    label_imagem.pack(pady=20)
except FileNotFoundError:

    label_imagem = tk.Label(janela, text="Imagem 'seno2.png' não encontrada", bg="#f0f0f0")
    label_imagem.pack(pady=20)

frame_entrada = tk.Frame(janela, bg="#f0f0f0") 
frame_entrada.pack(pady=10)

label_angulo = tk.Label(frame_entrada, text="Ângulo (0 à 90):", font=('Arial', 14), bg="#f0f0f0")
label_angulo.pack(pady=(0, 5))

validacao = janela.register(validar_entrada) 

entrada_angulo = tk.Entry(frame_entrada, width=3, justify='center', font=('Arial', 16), 
                          bd=0, highlightthickness=0, relief='flat', bg="#f0f0f0", fg='red', 
                          validate="key", validatecommand=(validacao, '%P')) 

entrada_angulo.pack()


linha = tk.Frame (frame_entrada, bg="black", height=1, width=entrada_angulo.winfo_reqwidth()) 
linha.pack(pady=(0,5)) 

frame_botoes = tk.Frame(janela, bg="#f0f0f0") 
frame_botoes.pack(pady=20)

botao_calcular = tk.Button(frame_botoes, text="Calcular", command=calcular, font=('Arial', 12),
                            bg="#d9d9d9", relief='flat', bd=0, highlightthickness=0) 
botao_calcular.pack(side=tk. LEFT, padx=10) 

botao_limpar = tk.Button(frame_botoes, text="Limpar", command=limpar, font=('Arial', 12),
                          bg="#d9d9d9", relief='flat', bd=0, highlightthickness=0)
botao_limpar.pack(side=tk.RIGHT, padx=10)

frame_resultados = tk.Frame(janela, bg="#f0f0f0") 
frame_resultados.pack(pady=10)

label_seno = tk.Label(frame_resultados, text="Seno:", font=('Arial', 12), bg="#f0f0f0")
label_seno.grid(row=0, column=0, padx=10, pady=5, sticky='e') 
resultado_seno = tk.Label(frame_resultados, text="", font=('Arial', 12, 'bold'), fg='red', bg="#f0f0f0")
resultado_seno.grid(row=0, column=1, padx=10, pady=5, sticky='w') 

label_cosseno = tk.Label(frame_resultados, text="Cosseno:", font=('Arial', 12), bg="#f0f0f0")
label_cosseno.grid(row=1, column=0, padx=10, pady=5, sticky='e') 
resultado_cosseno = tk.Label(frame_resultados, text="", font=('Arial', 12, 'bold'), fg='red', bg="#f0f0f0") 
resultado_cosseno.grid(row=1, column=1, padx=10, pady=5, sticky='w')

label_tangente = tk.Label(frame_resultados, text="Tangente:", font=('Arial', 12), bg="#f0f0f0")
label_tangente.grid(row=2, column=0, padx=10, pady=5, sticky='e')  
resultado_tangente = tk.Label(frame_resultados, text="", font=('Arial', 12, 'bold'), fg='red', bg="#f0f0f0")
resultado_tangente.grid(row=2, column=1, padx=10, pady=5, sticky='w') 

janela.mainloop()