import tkinter as tk


janela = tk.Tk()
janela.title('usando pack')
janela.geometry("800x600")

#label
label = tk.Label(janela,
                 text='este é o label',
                 bg = 'red',
                 fg='white',
                )
label.pack(tk.CENTER)

janela.mainloop()