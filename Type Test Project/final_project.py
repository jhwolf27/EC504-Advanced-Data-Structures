
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 19:22:30 2014

@author: jax
"""

#Type the colour and not the word

#import the modules we need, for creating a GUI...
import tkinter
#...and for creating random numbers.
import random

#the list of possible words.
#don't need, can move to label config
filename=open('long_list.txt')
x=filename.read().splitlines()
word_list=[]
for line in x:
    word_list.append(line)
#the player's score, initially 0.
score=0
#the game time left, initially 30 seconds.
timeleft=60 #change to time_remaining

#move the GUI stuff before the variables
#a function that will start the game.
def startGame(event): #change variable name 

    #if there's still time left...
    if timeleft == 60:
        #start the countdown timer.
        countdown() #change variable name
        
    #run the function to choose the next colour.
    nextword() #cvn

#function to choose and display the next colour.
def nextword(): #cvn 

    #use the globally declared 'score' and 'play' variables above.
    global score
    global timeleft

    #if a game is currently in play...
    if timeleft > 0:

        #...make the text entry box active.
        e.focus_set() #cvn of e
        #if the colour typed is equal to the colour of the text...
        if e.get()==str(word_list[0]):
            #...add one to the score.
            score += 1

        #clear the text entry box.
        e.delete(0, tkinter.END)
        #shuffle the list of colours
        random.shuffle(word_list)
        #change the colour to type, by changing the text _and_ the colour to a random colour value
        label.config(fg='black', text=str(word_list[0]))
        #update the score.
        scoreLabel.config(text="Score: " + str(score))

#a countdown timer function. 
def countdown():

    #use the globally declared 'play' variable above.
    global timeleft

    #if a game is in play...
    if timeleft > 0:

        #decrement the timer.
        timeleft -= 1
        #update the time left label.
        timeLabel.config(text="Time left: " + str(timeleft))
        #run the function again after 1 second.
        timeLabel.after(1000, countdown)
    if timeleft==0:
        times_up.config(text="TIMES UP!")
        
    
#create a GUI window.
root = tkinter.Tk()
#set the title.
root.title("J3CS")
#set the size.
root.geometry("1000x300")
root.config(bg='blue')

 #bg color
#add an instructions label.
instructions = tkinter.Label(root, text="Type in the words!", font=('Helvetica', 24), bg='blue')
instructions.pack()

#add a score label.
scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 20), bg='blue')
scoreLabel.pack()

#add a time left label.
timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12), bg='blue')
timeLabel.pack()

#add a label for displaying the colours.
label = tkinter.Label(root, font=('Helvetica', 60), bg='yellow')
label.pack()

times_up = tkinter.Label(root, font=('Helvetica', 24), bg='blue')
times_up.pack()
#add a text entry box for typing in colours.
e = tkinter.Entry(root)
#run the 'startGame' function when the enter key is pressed.
root.bind('<Return>', startGame)
e.pack()
#set focus on the entry box.
e.focus_set()

#start the GUI
root.mainloop()
