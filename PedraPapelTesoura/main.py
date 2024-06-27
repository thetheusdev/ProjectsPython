#Importando Bibliotecas
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from random import choice
from pygame import *
import functions as f

#cores
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha
co6 = "#808080" # gray / cinza
fundo = "#3b3b3b"

#Configuração da Janela
janela = Tk()
janela.title('Pedra, Papel e Tesoura by: theus_sl7')
janela.geometry('358x305')
janela.configure(bg=fundo)

#Dividindo a janela

frame_cima = Frame(janela, width=358, height=101, bg=co1, relief='raised')
frame_cima.grid(row = 0, column = 0, sticky=NW)
frame_baixo = Frame(janela, width=358, height=300, bg=co0, relief='flat')
frame_baixo.grid(row = 1, column = 0, sticky=NW)
mixer.init()

estilo = ttk.Style(janela)
estilo.theme_use('clam')

#Configurando o frame_cima
#P1

app_1 = Label(frame_cima, text='Você', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_1.place(x=40, y=70)
app_1_linha = Label(frame_cima, text='', height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_1_linha.place(x=0, y=0)
app_1_pontos = Label(frame_cima, text='0 ', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_1_pontos.place(x=60, y=20)

app_  = Label(frame_cima, text=':', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_.place(x=170, y=20)

#P2
app_2_pontos = Label(frame_cima, text='0 ', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_2_pontos.place(x=240, y=20)
app_2 = Label(frame_cima, text='PC', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_2.place(x=290, y=70)
app_2_linha = Label(frame_cima, text='', height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_2_linha.place(x=352, y=0)

app_linha = Label(frame_cima, text='',width= 359, anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co0)
app_linha.place(x=0, y=95)

app_you = Label(frame_baixo, text='', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_you.place(x=25, y=10)

app_pc = Label(frame_baixo, text='', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_pc.place(x=275, y=10)

app_rounds = Label(frame_baixo, text='ESCOLHA AS RODADAS', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
app_rounds.place_forget()

b_jogar = Button(frame_baixo,command=f.botão_rounds, width=30, text='Iniciar o jogo',  bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED,overrelief=RIDGE)
b_jogar.place(x=50, y=151)

f.som_comeco()
janela.mainloop()

