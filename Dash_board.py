from tkinter import *
from PIL import Image, ImageTk
from datetime import *
import time


class Dashboard:

    def __init__(self,window):
        self.window = window
        self.window.title('System Management Dashboard')
        self.window.geometry('1366x768')
        self.window.state('zoomed')
        self.window.config(background='#eff5f6')
        #window Icon, this would be for the window
        #icon = PhotoImage(file='<image>')
        #self.window.iconphoto(True, icon)

        # =============================================
        # =============================================
        #===============Header========================
        #==============================================

        self.header = Frame(self.window, bg='#009df4')
        self.header.place(x=300, y=0,width=1070,height=60)

        self.logout_text = Button(self.window,text='Logout',bg='#32cf8e',font=("",13,"bold"),bd=0,fg='white',cursor='hand2',activebackground='#32cf8e')
        self.logout_text.place(x=1250,y=15)

        # =============================================
        # =============================================
        #===============Sidebar========================
        #==============================================
        self.sidebar = Frame(self.window,bg='#ffffff')
        self.sidebar.place(x=0,y=0, width=300,height=750)

        # =============================================
        # =============================================
        #===============Body========================
        #==============================================

        self.heading = Label(self.window, text='Dashboard',font=("",13,"bold"), fg='#0064d3',bg='#eff5f6')
        self.heading.place(x=325,y=70)

        # =============================================
        # =============================================
        #===============Body_frame1========================
        #==============================================
        #Most likely use frame1 as the window_viewfor the lunar surface,<-----------so insert here
        
        self.bodyframe1 = Frame(self.window,bg='#ffffff')
        self.bodyframe1.place(x=328, y=110,width=1040,height=350)

        # =============================================
        # =============================================
        #===============Body fram2========================
        #==============================================

        self.bodyframe2 = Frame(self.window,bg='#009aa5')
        self.bodyframe2.place(x=328, y=495,width=310,height=220)

        #Altitude:

        self.heading = Label(self.window, text='Altitude',font=("",13,"bold"), fg='#0064d3',bg='#eff5f6')
        self.heading.place(x=338,y=550)

        #Altitude results:

        #self.result1 = Label(win)
        #self.result1.place(x=338 , y=500)
        self.result1=Entry()
        self.result1.place(x=338, y=600)


        
        self.result1.insert(END,"tada") #<---------For Altitude info, place variable in tada as string result

        

        # =============================================
        # =============================================
        #===============Body frame 3========================
        #==============================================

        self.bodyframe3 = Frame(self.window,bg='#e21f26')
        self.bodyframe3.place(x=680, y=495,width=310,height=220)
        
        #Gravitation accel:

        self.heading = Label(self.window, text='Gravitational Acceleration',font=("",13,"bold"), fg='#0064d3',bg='#eff5f6')
        self.heading.place(x=690,y=550)

        #Gravitation results:
        self.result2=Entry()
        self.result2.place(x=690, y=600)

        self.result2.insert(END,"tada") #<---------For Gravity info, place variable in tada as string result
        
        # =============================================
        # =============================================
        #===============Body frame 4========================
        #==============================================

        self.bodyframe4 = Frame(self.window,bg='#ffcb1f')
        self.bodyframe4.place(x=1030, y=495,width=310,height=220)

        #Fuel:
        self.heading = Label(self.window, text='Fuel level',font=("",13,"bold"), fg='#0064d3',bg='#eff5f6')
        self.heading.place(x=1040,y=550)

        #Fuel results:

        self.result3=Entry()
        self.result3.place(x=1040, y=600)

        self.result3.insert(END,"tada") #<---------For Fuel info, place variable in tada as string result
        
        
        
def win():
    window = Tk()
    Dashboard(window)
    window.mainloop()

if __name__=="__main__":

    win()
