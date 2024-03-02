# Lunar Lander
import tkinter as tk
import os
import math
import pgzrun
from pgzero.builtins import Actor, animate, keyboard

import pygame 
#
from pygame import image, Color
import time
import sys


#root = tk.Tk()
#button_win = tk.Frame(root, width = 500, height = 25)
#button_win.pack(side = tk.TOP)

#name_alt = tk.Label(root, text ='Altitude:',font=("",13,"bold"), fg='#0064d3',bg='#eff5f6')
#name_alt.pack(side = tk.LEFT)


pygame.init()
start_time = time.time()





backgroundImage = image.load('background.png')


lander = Actor('lander',(50,30))

#lander_direction:
lander.angle = lander.direction = -80

#lander_thrust:
lander.thrust = 0.5

#gravity:
gravity = 0.8

#speed of craft:
lander.burn = speedDown = gameState = gameTime = 0




#fuel once database is set up then replace it with a variable that
# draws from that data base: 
fuel_left = 1000

#wieght variable:
weight_of_craft = 2000



#temperature:
temp = 68

pressure = float(14.69)


def draw():
    global gameTime
    #window = (900,600)
    #screen = pygame.display.set_mode(window)
    #screen.blit('screen.png',(0,0))


    screen.blit('background.png',(0,0))
    screen.blit('space',(0,0))
    r = lander.angle
    if(lander.burn > 0):
        lander.image = "landerburn"
    else:
        lander.image = "lander"
    lander.angle = r
    lander.draw()
    if gameState == 0:
        gameTime = int(time.time() - start_time)
    #Altitude:
    screen.draw.text("Altitude : "+ str(getAlt()), topleft=(650, 10), owidth=0.5, ocolor=(255,0,0), color=(255,255,0) , fontsize=25)
    #velocity:
    screen.draw.text("Velocity : "+ str(round(move_point(abs(speedDown),2),2)), topleft=(650, 30), owidth=0.5, ocolor=(255,0,0), color=(255,255,0) , fontsize=25)
    
    #Pressure:
    screen.draw.text("Pressure PSI: "+ str(pressure), topleft=(650, 50), owidth=0.5, ocolor=(255,0,0), color=(255,255,0) , fontsize=25)

    #Weight:
    screen.draw.text("Weight : "+ str(weight_of_craft), topleft=(650, 70), owidth=0.5, ocolor=(255,0,0), color=(255,255,0) , fontsize=25)
    #Fuel:
    screen.draw.text("Fuel : "+ str(fuel_left), topleft=(650, 90), owidth=0.5, ocolor=(255,0,0), color=(255,255,0) , fontsize=25)
    #Temperature:
    screen.draw.text("Temp.F': "+ str(temp), topleft=(650, 110), owidth=0.5, ocolor=(255,0,0), color=(255,255,0) , fontsize=25)
    #Time:
    screen.draw.text("Time : "+ str(gameTime), topleft=(40, 10), owidth=0.5, ocolor=(255,0,0), color=(255,255,0) , fontsize=25)
    if gameState == 2:
        screen.draw.text("Congratulations \nThe League Has Landed", center=(400, 50), owidth=0.5, ocolor=(255,0,0), color=(255,255,0) , fontsize=35)
        #play_restart_window()

        
    if gameState == 1:
        time.sleep(0.5)
        screen.draw.text("Crashed", center=(400, 50), owidth=0.5, ocolor=(255,0,0), color=(255,255,0) , fontsize=35)
        #adding a kill statement to kill program after the lander crashes
        #time.sleep(0.2)

        
        
        pygame.quit()
        play_restart_window()

        sys.exit()
        
        

    

def play_restart_window():
    import pulling_lunar_from_file


def you_died():
    screen.draw.text("Congratulations \nThe Eagle Has Landed", center=(400, 50), owidth=0.5, ocolor=(255,0,0), color=(255,255,0) , fontsize=35)

def update():
    global gameState, speedDown, fuel_left, weight_of_craft
    if gameState == 0:


        #Control of fuel and burn of craft:
    
        
        if keyboard.up and (fuel_left >= 1):
            
            lander.thrust = limit(lander.thrust+0.01,0,1)
            changeDirection()
            lander.burn = 1
            fuel_left-=lander.burn
            weight_of_craft-=lander.burn

    
        if keyboard.left: lander.angle += 1
        if keyboard.right: lander.angle -= 1
 
        oldPos = lander.center
        lander.y += gravity
        newPos = calcNewXY(lander.center, lander.thrust, math.radians(90-lander.direction))
        lander.center = newPos
        speedDown = newPos[1] - oldPos[1]
            
        lander.thrust = limit(lander.thrust-0.001,0,1)
        lander.burn = limit(lander.burn-0.05,0,1)

        
        if speedDown < 0.2 and getAlt() == 1 and lander.angle > -5 and lander.angle < 5:
            gameState = 2
        if getAlt() == 0:
            gameState = 1

def changeDirection():
    if lander.direction > lander.angle: lander.direction -= 1
    if lander.direction < lander.angle: lander.direction += 1

def limit(n, minn, maxn):
    return max(min(maxn, n), minn)

def calcNewXY(xy,speed,ang):
    newx = xy[0] - (speed*math.cos(ang))
    newy = xy[1] - (speed*math.sin(ang))
    return newx, newy

def move_point(number,shift,base=10):

    return number*base**shift


def getAlt():
    testY = lander.y+8
    height = 0;
    while testPixel((int(lander.x),int(testY))) == Color('black') and height < 600:
        testY += 1
        height += 1
    return height

def testPixel(xy):
    if xy[0] >= 0 and xy[0] < 800 and xy[1] >= 0 and xy[1] < 600:
        return backgroundImage.get_at(xy)
    else:
        return Color('black')
pgzrun.go()
