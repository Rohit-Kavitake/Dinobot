#Program to automate the trex dinosaur game
#project By ROHIT KAVITAKE

#open http://www.trex-game.skipser.com/ to play this game
#make sure repplay button appears before execution


#modules needed
import pyautogui       
from PIL import ImageGrab, ImageOps
import time
from numpy import *
import os

#GAthering co-ordinates of replay button and our dino
#co-ordinates changes as there is change in the display size of screen
#this one are suitable for 1600*900 resolution display
#Before execution be sure that these co-ordinates suit ur display
class Coordinates():
    replay = (400,450)
    dino = (185,452)
    #x=240
    #y=465

    #startgame function to click the replay button at start of the execution
def startgame():
    pyautogui.click(Coordinates.replay)

#jump function used to make the dino jump
def jump():
    pyautogui.keyDown('space')
    time.sleep(0.01)
    pyautogui.keyUp('space')

#imagegrab function is used tpo check the presence of tree by recognizing the pixel colors
def imageGrab():
    box = (Coordinates.dino[0]+60,Coordinates.dino[1],Coordinates.dino[0]+140,Coordinates.dino[1]+38)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return(a.sum())

# this is main function
def main():
    count = 0
    startgame()
    while True:
        if (imageGrab()!=3287):
            jump()
            count+=1
            print("Jumping",count,"th Times ..")



main()