from __future__ import division, print_function

import game

window = None

def setup():
    global window
    frameRate(120)
    size(game.WIDTH, game.HEIGHT)
    rectMode(CORNERS)
    imageMode(CENTER)
    textMode(CENTER)
    textAlign(CENTER, CENTER)
    window = game.Window()

    

def draw():
    background(game.BACKGROUND_COLOR)
    window.on_draw()
    window.on_update()
    

"""
def keyPressed():
    if key == CODED:
        window.on_key_press(keyCode)
    else:
        window.on_key_press(key)

def keyReleased():
    if key == CODED:
        window.on_key_release(keyCode)
    else:
        window.on_key_release(key)
"""

"""def mousePressed():
    window.on_mouse_press(mouseX, mouseY, mouseButton)
    clicking is for noobs


def mouseReleased():
    window.on_mouse_release
"""
def mouseClicked():
    window.on_mouse_clicked(mouseX, mouseY)
    
