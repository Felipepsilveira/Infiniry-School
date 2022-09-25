import tkinter as tk

janela1 = tk.Tk()

janela1.title('Janela 1')

janela1.geometry('800x600')



bt = tk.Button(janela1, text='Aperte aqui', command=janela1.destroy)


bt.pack()


janela1.mainloop()
