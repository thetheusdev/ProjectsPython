from tkinter import *

#Cores
cor1 = "#000000" #preta
cor2 = '#f3ffff' #branca
cor3 = '#1b00ff' #azul
cor4 = '#ECEFF1' #cinza
cor5 = '#FFAB40' #laranja

#Corpo
calculadora = Tk()
calculadora.title('calculadora')
calculadora.geometry('235x310')
calculadora.config(bg=cor1)

tela_result = Frame(calculadora, width=235, height=50, bg=cor2)
tela_result.grid(row=0, column=0)

tela_botao = Frame(calculadora, width=235, height=268, bg=cor1)
tela_botao.grid(row=1, column=0)

#Variavel Global
todos_valores = ''

#Criando os numeros
valor_texto = StringVar()
numeros = Label(tela_result, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', \
justify=RIGHT, font=('Ivy 18'), bg=cor2)
numeros.place(x=0, y=0)

#Funções
def valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

def clear():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

def apagar(event):
    global todos_valores
    apagar = todos_valores - str(event)
    valor_texto.set(apagar)

#BOTÕES
#Primeira Fileira
b_clear = Button(tela_botao, command=clear, text='C', width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_clear.place(x=0, y=0)
b_erase = Button(tela_botao, command=apagar, text='X', width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_erase.place(x=59, y=0)
b_por = Button(tela_botao, command=lambda: valores('%'), text='%', width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_por.place(x=118, y=0)
b_barra = Button(tela_botao, command=lambda: valores('/'), text='÷', width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_barra.place(x=177, y=0)

#Segunda Fileira
b_7 = Button(tela_botao, command=lambda: valores('7'), text='7', width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=52)
b_8 = Button(tela_botao, command=lambda: valores('8'), text='8', width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=59, y=52)
b_9 = Button(tela_botao, command=lambda: valores('9'), text='9', width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=118, y=52)
b_x = Button(tela_botao, command=lambda: valores('*'), text='*', width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_x.place(x=177, y=52)

#Terceira Fileira
b_4 = Button(tela_botao, command=lambda: valores('4'), text='4', width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=104 )
b_5 = Button(tela_botao, command=lambda: valores('5'), text='5', width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=104)
b_6 = Button(tela_botao, command=lambda: valores('6'), text='6', width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=104)
b_menos = Button(tela_botao, command=lambda: valores('-'), text='-', width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_menos.place(x=177, y=104)

#Quarta Fileira
b_1 = Button(tela_botao, command=lambda: valores('1'), text='1', width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=156)
b_2 = Button(tela_botao, command=lambda: valores('2'), text='2', width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=59, y=156)
b_3 = Button(tela_botao, command=lambda: valores('3'), text='3', width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=118, y=156)
b_mais = Button(tela_botao, command=lambda: valores('+'), text='+', width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_mais.place(x=177, y=156)

#Ultima Fileira

b_0 = Button(tela_botao, command=lambda: valores('0'), text='0', width=11, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_0.place(x=0, y=208)
b_ponto = Button(tela_botao, command=lambda: valores('.'), text='.', width=5, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_ponto.place(x=118, y=208)
b_result = Button(tela_botao, command=calcular, text='=', width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_result.place(x=177, y=208)




calculadora.mainloop()
