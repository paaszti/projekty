import pgzrun
from pgzero.builtins import Actor, mouse, Rect
from pgzero.screen import Screen
import random
import sys
import time
screen: Screen

#SCREEN
WIDTH, HEIGHT = 800, 600

#COLOURS
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

#RECT
rects = [[Rect(random.randint(0, WIDTH-20), random.randint(0, HEIGHT-20), 20, 20), True]]

points = 0

now = time.time()

LOST = False

def on_mouse_down(pos, button):
    global points
    if button != mouse.LEFT:
        return
    for rect in rects:
        if rect[0].x <= pos[0] <= rect[0].x + 20 and rect[0].y <= pos[1] <= rect[0].y + 20 and rect[1]:
            points += 1
            rect[0].x = random.randint(0, WIDTH-20)
            rect[0].y = random.randint(0, HEIGHT-20)
            break

def update():
    global now
    global LOST
    time_in_game = time.time()
    remaining_time = int(round(60 - abs(now - time_in_game), 0))
    while True:
        if abs(now - time_in_game) >= 60:
            LOST = True
            break
        return remaining_time

def draw():
    global start, LOST, points
    screen.fill(BLACK)
    for rect in rects:
        if rect[1]:
            screen.draw.filled_rect(rect[0], GREEN)
            screen.draw.text(f'Points: {points}', (HEIGHT+20, 0), color=WHITE, fontsize=50, sysfontname='Arial')
            screen.draw.text(f'Remaining time: {update()}', (0, 0), color=WHITE, fontsize=50, sysfontname='Arial')
        if LOST == True:
            screen.draw.text(f'End of game. You have: {points} points', (HEIGHT/2 - 150, WIDTH/2 - 100), color=WHITE, fontsize=50, sysfontname='Arial')
pgzrun.go()
