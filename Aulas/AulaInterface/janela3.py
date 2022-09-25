import tkinter as tk

janela = tk.Tk()

janela.title("Janela dos botões")

janela.geometry('800x600')
#cria um butão e definie a janela em que aparece, o texto dentro dele, e o comando que ira utilizar
bt1 = tk.Button(janela, text='Aperte aqui', command=janela.destroy)
bt2 = tk.Button(janela, text='Aperte aqui', command=janela.destroy)
bt3 = tk.Button(janela, text='Aperte aqui', command=janela.destroy)
#coloca sequencialmente os butões na janela
bt1.pack()
bt2.pack()
bt3.pack()

janela.mainloop()
