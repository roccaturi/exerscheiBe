#!/usr/bin/env python

"""Exercise.py includes the main functionality of ExerScheiBe: acquisition and handling of the regime script's data, control of flow through the regime, and calls to both the os and media applications (through imported modules such as iTunesContoller).""" 

import os
import time
from iTunesController import *    # Functions pause(), play(), and move() belong to iTunesController.

repeat = False
logfile = open("logfile.txt", "w")

def main():
    """Asks user which line of the exercise regime they want to start with and controls flow through the regime to completion."""
    global repeat
    regime = collect()
    start = int(raw_input("Which line of the exercise script would you like to begin with? ")) - 1
    regime = regime[start:]
    pause()
    say("Ready?")
    time.sleep(1)
    for exercise in regime:
        coach(exercise[:-1])
        while repeat:
            repeat = False
            coach(exercise[:-1])
    say("Session complete.")

def collect(filename=None):
    """Assumes filename of type str or requests filename from the user if none provided.  Returns contents of filename as a list of lines.""" 
    if not filename:
        filename = str(raw_input("What is the name of the file (including extentions) for the exercise regime you would like to run? "))
    read_only_file = open(filename, 'r')
    file_contents = read_only_file.readlines()
    return file_contents

def coach(exercise):
    """Assumes exercise is of type list and of format (ID int, name str, duration int, duration unit str).  Prints exercise to screen and gives auditory cues regarding the exercise."""
    num, name, duration, unit = exercise.split(",")
    say(name)
    print exercise
    if unit == " reps":
        say(duration + "repetitions. Press Enter when complete.")
        play()
        await_cmd(exercise)
        pause()
    elif unit == " sec":
        say(duration + "seconds. Press Enter when ready to begin.")
        await_cmd(exercise)
        say("Begin")
        play()
        time.sleep(float(duration))
        pause()
        say("Stop.  Press Enter to continue.")
        await_cmd(exercise)
    elif unit == " adv":
        play()
        time.sleep(float(duration))
        pause()
    else:
        raise ValueError("Variable unit is not recognized.")

def say(msg):
    """Assumes msg is of type str.  Calls os method say to convert msg to speech."""
    os.system("say " + msg)

def await_cmd(exercise):
    global repeat
    done = False
    while not done:
        key_press = raw_input("Press ENTER or special command. ") 
        if key_press == '':
            done = True
        elif key_press == "h":
            help()
        elif key_press == "r":
            repeat = True
        elif key_press == 'm':
            move()
        elif key_press == "l":
            log(exercise)

def help():
    """Does nothing important at the moment."""
    print "Help comes to those who ask"

def log(exercise):
    """Assumes exercise is of type list and of format (ID int, name str, duration int, duration unit str).  Requests a message from the user and writes it to a logfile on a line following the current exercise."""
    global logfile
    msg = raw_input("Enter your message. ")
    logfile.write(exercise + " >>> " + msg + "\n")

main()
