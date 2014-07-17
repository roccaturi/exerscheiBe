#!/usr/bin/env python

"""iTunesController.py provides functions to pause, play, and move position within an audio or video file selected in iTunes."""

import commands

def state_update():
    return commands.getoutput("osascript -e 'tell application \"iTunes\" to player state as string'")

state = state_update()

def play():
    """Plays the current track at current position (if paused) and prints a message to the screen noting the change (or lack of change).""" 
    global state
    if state == "paused":
        commands.getoutput("osascript -e 'tell application \"iTunes\" to play'")
    state = state_update()

def pause():
    """Pauses the current track at current position (if playing) and prints a message to the screen noting the change (or lack of change)."""
    global state
    if state == "playing":
        commands.getoutput("osascript -e 'tell application \"iTunes\" to pause'")
    state = state_update()

def move():
    """Requests the user to supply a +/-  modifier and a value and then moves the current track forward of backward by the supplied value."""
    modifier = raw_input("Where to?  (Example: '+ 30' for thirty seconds forward, '- 10' for ten second back.) ")
    direc, dist = modifier[0], int(modifier[1:])
    commands.getoutput("osascript -e 'tell application \"iTunes\" to set player position to (player position " + modifier + ")'")
