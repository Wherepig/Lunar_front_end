

#exec(open('PK_iteration_II.py').read())
import os
from tkinter import *

import tkinter as tk


from PIL import Image, ImageTk
#use tkinter instead of Tkinter (small, not capital T) if it doesn't work
#as it was changed to tkinter in newer Python versions





root = tk.Tk()
button_win = tk.Frame(root, width = 800, height = 400)
button_win.pack()
button_win.config(background='#eff5f6')
#root = Tk()

#background image:

image1 = Image.open("lunar_surface_3.png")
test = ImageTk.PhotoImage(image1)
label1 = tk.Label(image=test)
label1.image = test
label1.place(relx=0,rely=0)
label1_kill = label1.destroy

#title of game:
title = tk.Label(root, text='Mission Lunar Lander',font=("",25,"bold"), fg='#ffdf00',bg='#000000')
title.place(relx=0.5, rely= 0.1,height=40, anchor=tk.CENTER)
title_kill = title.destroy


#Author
author = tk.Label(root,text='Presented by The League of Astronomical Gentlemen',font=("",19,"bold"), fg='#ffdf00',bg='#000000')
author.place(relx=0.5, rely= 0.2,height=40, anchor=tk.CENTER)
author_kill = author.destroy
#Play button:

play_button = tk.Button(root, text="Manned Mission",bg='#009df4',font=("",14,"bold"),bd=0,fg='white',cursor='hand2',activebackground='#32cf8e', command=lambda:[root.destroy(),play_game()]) #.pack() #button to close the window
play_button.place(relx=0.5, rely= 0.5,height=40, anchor=tk.CENTER)
play_button_kill = play_button.destroy

def play_game():
    #exec(open('PK_iteration_II.py').read())
    #os.system('PK_iteration_II.py')
    #import PK_iteration_II

    from subprocess import call
    call(['python','PK_iteration_II.py'])




def credit_destroy():
    #label2 =

    image2 = Image.open("lunar_surface_3.png")
    test = ImageTk.PhotoImage(image2)
    label2 = tk.Label(image=test)
    label2.image = test
    label2.place(relx=0,rely=0)
    back_button = tk.Button(root, text="Back",bg='#f44336',font=("",14,"bold"),
bd=0,fg='white',cursor='hand2',activebackground='#32cf8e', command=lambda:[label2.destroy(),back_button.destroy()])
    back_button.place(relx=0.5, rely= 0.8,width=80,height=40, anchor=tk.CENTER)




#Quit button :
quit_button = tk.Button(root, text="Quit",bg='#f44336',font=("",14,"bold"),bd=0,fg='white',cursor='hand2',activebackground='#32cf8e', command=root.destroy) #button to close the window
quit_button.place(relx=0.5, rely= 0.7,width=80,height=40, anchor=tk.CENTER)
quit_button_k = quit_button.destroy


#credits_button:
credit_button = tk.Button(root, text="Credits",bg='#f44336',font=("",14,"bold"),
bd=0,fg='white',cursor='hand2',activebackground='#32cf8e', command=credit_destroy)


credit_button.place(relx=0.5, rely= 0.9,width=80,height=40, anchor=tk.CENTER)
credit_kill = credit_button.destroy







#throw loop
tk.mainloop()
