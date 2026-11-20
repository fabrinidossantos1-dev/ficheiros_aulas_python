import tkinter as tk # Importa a biblioteca tkinter, que permite janelas
janela = tk.Tk() # cria a janela principal da aplicação.
label = tk.Label(janela, text="Olá Mundo") #cria um texto com a mensagem "Olá Mundo"
label.pack() #Posiciona e apresenta o texto na janela.
janela.mainloop() #Mantém a janela aberta e ativa, permitido a interação do utilizador
