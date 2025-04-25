import tkinter as tk

# Cria a janela principal
janela = tk.Tk()
janela.title("Minha Janela")
janela.geometry("300x200")  # Largura x Altura

# Adiciona um rótulo (texto) na janela
rotulo = tk.Label(janela, text='''-------------------------------------------------------------------------
        ''')
rotulo.pack(pady=20)

# Inicia o loop da interface
janela.mainloop()
