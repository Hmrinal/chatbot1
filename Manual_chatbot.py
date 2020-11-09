#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 22:18:36 2020

@author: MrinalTyagi
"""

from tkinter import *

root = Tk()

root.title('ChatBot')

def send():
    send = "You:"+ e.get()
    text.insert(END,"\n" + send)
    if(e.get()=='hi'):
        text.insert(END,"\n" + "Bot: Hello")
    elif(e.get()=='hello'):
        text.insert(END,"\n" + "Bot: Hi")
    elif(e.get()=='how are you'):
        text.insert(END,"\n" + "Bot: I'm fine and you?")
    elif(e.get()=="I'm fine too"):
        text.insert(END,"\n" + "Bot: Nice to hear that")
    elif(e.get()=='do you know me'):
        text.insert(END,"\n" + "Bot: Human!!")
    else:
        text.insert(END,"\n" + "Bot: Sorry I did'nt get it.")

text= Text(root,bg='light blue')
text.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=55)
send=Button(root,text='Send',bg='black',width=10,command=send).grid(row=1,column=1)
e.grid(row=1,column=0)


root.mainloop()
