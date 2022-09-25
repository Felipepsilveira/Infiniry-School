import tkinter as tk

janela = tk.Tk()
janela.geometry('300x300')

# 'bd' define a largura da borda em pixels
bt = tk.Button(janela,text='Aperte aqui',bd=5, command=janela.destroy)

#"Width" e "Height" definem a largua e altura do botão em pixels
bt.config(width=25,height=5)

#coloca o botão na janela
bt.pack()

janela.mainloop()