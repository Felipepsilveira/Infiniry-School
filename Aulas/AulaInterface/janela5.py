import tkinter as tk

janela = tk.Tk()
janela.geometry("800x600")
janela.title("Label")

bt = tk.Button(janela, text="aperte aqui", bd = 2, command=janela.destroy)

bt.config(width=50, height=5)

#criando um label
lbTexto = tk.Label(janela, text="o botão abaixo fecha a janela!")

#põe o label na janela
lbTexto.pack()
bt.pack()

janela.mainloop()
