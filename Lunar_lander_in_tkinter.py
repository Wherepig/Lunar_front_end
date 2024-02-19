from tkinter import *
from PIL import Image, ImageTk
from datetime import *
import time
#import the lander





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

        #Sidebar_clickable buttons:

        #mission_text:
        self.mission_text = Button(self.window,text='Mission',bg='#32cf8e',font=("",15,"bold"),bd=0,fg='white',cursor='hand2',activebackground='#32cf8e')
        self.mission_text.place(x=28, y=50)
        #Launch_team:
        self.launch_team = Button(self.window,text='Launch Team',bg='#32cf8e',font=("",15,"bold"),bd=0,fg='white',cursor='hand2',activebackground='#32cf8e')
        self.launch_team.place(x=28, y=100)
        #rocket:
        self.rocket = Button(self.window,text='Rocket',bg='#32cf8e',font=("",15,"bold"),bd=0,fg='white',cursor='hand2',activebackground='#32cf8e')
        self.rocket.place(x=28, y=150)
        #Launch_site:
        self.launch_site = Button(self.window,text='Launch Site',bg='#32cf8e',font=("",15,"bold"),bd=0,fg='white',cursor='hand2',activebackground='#32cf8e')
        self.launch_site.place(x=28, y=200)

        #Mode button:
        self.launch_site = Label(self.window, text='Mode:',font=("",20,"bold"), fg='#0064d3',bg='#eff5f6')
        self.launch_site.place(x=28, y=400)

            #manned:
        self.launch_site = Label(self.window, text='Manned:',font=("",15,"bold"), fg='#000000')
        self.launch_site.place(x=50, y=450)

            #                                                                                                                                                            |
            #Start_button: <------------------------------------------Enter initiative sequence for manned operation =============================game loop command here V
            #Enter command prompt for pygame loop       
        self.launch_site = Button(self.window,text='Start',bg='#f44336',font=("",14,"bold"),bd=0,fg='white',cursor='hand2',activebackground='#32cf8e', command = pygame_loop)
        self.launch_site.place(x=200, y=450)
        
            #unmanned:
        self.launch_site = Label(self.window, text='Unanned:',font=("",15,"bold"), fg='#000000')
        self.launch_site.place(x=50, y=500)


        
            #Start_button: <------------------------------------------Enter initiative sequence for manned operation
        self.launch_site = Button(self.window,text='Start',bg='#f44336',font=("",14,"bold"),bd=0,fg='white',cursor='hand2',activebackground='#32cf8e')
        self.launch_site.place(x=200, y=500)
        

        #Mode buttons:
        
        

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
        self.bodyframe2.place(x=328, y=495,width=1030,height=220)#<--------changing body-frame2-size

        #Altitude:

        self.heading = Label(self.window, text='Altitude:',font=("",13,"bold"), fg='#0064d3',bg='#eff5f6')
        self.heading.place(x=338,y=500)

        #Altitude results:

        #self.result1 = Label(win)
        #self.result1.place(x=338 , y=500)
        self.result1=Entry()
        self.result1.place(x=338, y=550)


        
        self.result1.insert(END,"tada") #<---------For Altitude info, place variable in tada as string result

        #Velocity:
        self.heading = Label(self.window, text='Velocity/sec:',font=("",13,"bold"), fg='#0064d3',bg='#eff5f6')
        self.heading.place(x=338,y=600)

        self.result1_half=Entry()
        self.result1_half.place(x=338, y=650)


        
        self.result1_half.insert(END,"tada") #<---------For Velocity info, place variable in tada as string result
        

        # =============================================
        # =============================================
        #===============Body frame 3========================
        #==============================================

        #self.bodyframe3 = Frame(self.window,bg='#e21f26')
        #self.bodyframe3.place(x=680, y=495,width=310,height=220)
        
        #Gravitation accel:

        self.heading = Label(self.window, text='Gravitational Accel.:',font=("",13,"bold"), fg='#0064d3',bg='#eff5f6')
        self.heading.place(x=518,y=500)

        #Gravitation results:
        self.result2=Entry()
        self.result2.place(x=518, y=550)

        self.result2.insert(END,"tada") #<---------For Gravity info, place variable in tada as string result

        #Temperature:
        self.heading = Label(self.window, text='Temperature:',font=("",13,"bold"), fg='#0064d3',bg='#eff5f6')
        self.heading.place(x=518,y=600)


        #Temperature results:
        self.result2=Entry()
        self.result2.place(x=518, y=650)

        self.result2.insert(END,"tada") #<---------For Temp. info, place variable in tada as string result

        #Fuel:
        self.heading = Label(self.window, text='Fuel:',font=("",13,"bold"), fg='#0064d3',bg='#eff5f6')
        self.heading.place(x=708,y=500)


        #Fuel results:
        self.result2=Entry()
        self.result2.place(x=708, y=550)

        self.result2.insert(END,"tada") #<---------For fuel info, place variable in tada as string result

        #Weight:
        self.heading = Label(self.window, text='Weight:',font=("",13,"bold"), fg='#0064d3',bg='#eff5f6')
        self.heading.place(x=708,y=600)


        #Weight results:
        self.result2=Entry()
        self.result2.place(x=708, y=650)

        self.result2.insert(END,"tada") #<---------For Weight info, place variable in tada as string result
        
        # =============================================
        # =============================================
        #===============Body frame 4========================
        #==============================================

        #self.bodyframe4 = Frame(self.window,bg='#ffcb1f')
        #self.bodyframe4.place(x=1030, y=495,width=310,height=220)

        #Pressure:
        self.heading = Label(self.window, text='Pressure:',font=("",13,"bold"), fg='#0064d3',bg='#eff5f6')
        self.heading.place(x=898,y=500)

        #Pressure results:

        self.result3=Entry()
        self.result3.place(x=898, y=550)

        self.result3.insert(END,"tada") #<---------For Pressure info, place variable in tada as string result






#game_loop for the lunar interface:
def pygame_loop():        

    #import Lunar_lander
    #exec(open("Lunar_lander.py").read(), globals())

    
    import Lunar_lander
    exec(open("Lunar_lander.py").read(),globals())
    altitude = getAlt()
  
        
def win():
    window = Tk()
    Dashboard(window)
    window.mainloop()

if __name__=="__main__":

    win()
