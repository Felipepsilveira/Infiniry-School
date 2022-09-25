import tkinter as tk

janela = tk.Tk()
janela.geometry("450x300")

Lbtexto1 = tk.Label(janela, text = "texto de exemplo",bg = "blue", fg="magenta")
Lbtexto1.pack()

Lbtexto2 = tk.Label(janela, text = "texto de exemplo", bg="red", fg="orange", font=("Helvetica bold", 20))
Lbtexto2.pack()

btFim = tk.Button(janela, text='Aperte Aqui', command=janela.destroy,
                  bg='yellow', fg='red',font=('Broadway', 40))

btFim.pack()

janela.mainloop()
                     