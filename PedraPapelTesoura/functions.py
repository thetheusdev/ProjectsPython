import main as m
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from random import choice
from pygame import *

#Variantes globais
rounds = 0
pontos_you = 0
pontos_pc = 0
global you
global pc

#função som do começo
def som_comeco():
    m.mixer_music.load('começo.mp3')
    m.mixer_music.play(0)

    
#função botão das rodadas
def botão_rounds():
    global icon_r3
    global icon_r5
    global icon_r7
    global b_icon_r3
    global b_icon_r5
    global b_icon_r7

    m.b_jogar.destroy()

    icon_r3 = m.Image.open('3.png')
    icon_r3 = icon_r3.resize((70,70), Image.LANCZOS)
    icon_r3 = m.ImageTk.PhotoImage(icon_r3)
    b_icon_r3 = m.Button(m.frame_baixo, command=lambda: escolher_rodadas('rounds3'), width=50, image=icon_r3, compound=CENTER, bg=m.co0, fg=m.co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_r3.place(x=40, y=50)

    icon_r5 = Image.open('5.png')
    icon_r5 = icon_r5.resize((70,70), Image.LANCZOS)
    icon_r5 = ImageTk.PhotoImage(icon_r5)
    b_icon_r5 = Button(m.frame_baixo, command=lambda: escolher_rodadas('rounds5'), width=50, image=icon_r5, compound=CENTER, bg=m.co0, fg=m.co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_r5.place(x=150, y=50)

    icon_r7 = Image.open('7.png')
    icon_r7 = icon_r7.resize((70,70), Image.LANCZOS)
    icon_r7 = ImageTk.PhotoImage(icon_r7)
    b_icon_r7 = Button(m.frame_baixo, command=lambda: escolher_rodadas('rounds7'), width=50, image=icon_r7, compound=CENTER, bg=m.co0, fg=m.co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_r7.place(x=260, y=50)


#função escolher as rodadas
def escolher_rodadas(r):
    global rounds
    if r == 'rounds3':
        rounds += 3

    elif r == 'rounds5':
        rounds += 5

    elif r == 'rounds7':
        rounds += 7
    iniciar_jogo()

    
#função Iniciar o jogo
def iniciar_jogo():
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3
    
    m.app_rounds.destroy()

    icon_1 = Image.open('pedra.png')
    icon_1 = icon_1.resize((70,70), Image.LANCZOS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(m.frame_baixo, command=lambda: jogar('pedra'), width=50, image=icon_1, compound=CENTER, bg=m.co0, fg=m.co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_1.place(x=40, y=50)

    icon_2 = Image.open('papel.png')
    icon_2 = icon_2.resize((70,70), Image.LANCZOS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(m.frame_baixo, command=lambda: jogar('papel'), width=50, image=icon_2, compound=CENTER, bg=m.co0, fg=m.co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_2.place(x=150, y=50)

    icon_3 = Image.open('tesoura.png')
    icon_3 = icon_3.resize((70,70), Image.LANCZOS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(m.frame_baixo, command=lambda: jogar('tesoura'),  width=70, image=icon_3, compound=CENTER, bg=m.co0, fg=m.co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_3.place(x=260, y=50)


#função Lógica do jogo
def jogar(i):
    global pontos_you
    global pontos_pc
    global rounds

    if rounds > 0:
        print(rounds)
        opcoes = ['pedra', 'papel', 'tesoura']
        pc = choice(opcoes)
        defeats = {
                    "pedra": "papel",
                    "papel": "tesoura",
                    "tesoura": "pedra"
                   }

        you = i
        
        m.app_you['text'] = you.capitalize()
        m.app_you['fg'] = m.co1

        m.app_pc['text'] = pc.capitalize()
        m.app_pc['fg'] = m.co1

        #Caso der o mesmo resultado ou alguem ganhe:
        if you.lower() == pc:
            print('Empatou')
            m.app_1_linha['bg'] = m.co0
            m.app_2_linha['bg'] = m.co0
            m.app_linha['bg'] = m.co3
            mixer_music.load('empate.mp3')
            mixer_music.play()
        
        elif defeats[pc] == you.lower():
            print('Você ganhou!')
            m.app_1_linha['bg'] = m.co4
            m.app_2_linha['bg'] = m.co0
            m.app_linha['bg'] = m.co0
            pontos_you += 10
            mixer_music.load('euacertei.mp3')
            mixer_music.play()
        
        else:
            print('PC ganhou. Tente novamente.')
            m.app_1_linha['bg'] = m.co0
            m.app_2_linha['bg'] = m.co4
            m.app_linha['bg'] = m.co0
            pontos_pc += 10
            mixer_music.load('pcacertou.mp3')
            mixer_music.play()

        print(you, pc)

    else:
        fim_do_jogo()

    #Atualizando a pontuação
    m.app_1_pontos['text'] = pontos_you
    m.app_2_pontos['text'] = pontos_pc
    rounds -= 1

def fim_do_jogo():
    global rounds
    global pontos_you
    global pontos_pc
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3
    global b_icon_r3
    global b_icon_r5
    global b_icon_r7

    #Reiniciando e destruindo os botões
    pontos_you = 0
    pontos_pc = 0
    rounds = 0
    b_icon_1.destroy()
    b_icon_2.destroy()
    b_icon_3.destroy()
    b_icon_r3.destroy()
    b_icon_r5.destroy()
    b_icon_r7.destroy()


    #Definindo o vencedor
    jogador_you = int(m.app_1_pontos['text'])
    jogador_pc = int(m.app_2_pontos['text'])

    if jogador_you > jogador_pc:
        app_winner = Label(m.frame_baixo, text='PARABENS, VOCÊ GANHOU!!!', height=1, anchor='center', font=('Ivy 10 bold'), bg=m.co0, fg=m.co4)
        app_winner.place(x=80, y=50)
        mixer_music.load('vencer.mp3')
        mixer_music.play()

    elif jogador_pc > jogador_you:
        app_winner = Label(m.frame_baixo, text='VOCÊ PERDEU PARA O PC!!', height=1, anchor='center', font=('Ivy 10 bold'), bg=m.co0, fg=m.co5)
        app_winner.place(x=80, y=50)
        mixer_music.load('perder.mp3')
        mixer_music.play()
    else:
        app_winner = Label(m.frame_baixo, text='EMPATOU!', height=1, anchor='center', font=('Ivy 10 bold'), bg=m.co0, fg=m.co2)
        app_winner.place(x=100, y=50)
        mixer_music.load('empatouojogo.mp3')
        mixer_music.play()

    #jogar denovo
    def jogar_denovo():
        app_winner.destroy()
        b_jogar_denovo.destroy()

        botão_rounds()


    b_jogar_denovo = Button(m.frame_baixo,command=jogar_denovo, width=30, text='Jogar novamente',  bg=m.fundo, fg=m.co0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED,overrelief=RIDGE)
    b_jogar_denovo.place(x=50, y=151)
