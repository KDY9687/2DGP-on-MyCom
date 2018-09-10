from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')



while(True):
    x = 400
    y = 90
    degree = 271
    while(x<780):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.01)
    while(y<560):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y + 2
        delay(0.01)
    while(x>20):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        delay(0.01)
    while(y>90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y - 2
        delay(0.01)
    while(x<400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.01)
    while(degree%360 != 270):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x+400, y+320)
        x = math.cos(math.radians(degree))*230
        y = math.sin(math.radians(degree))*230
        degree = degree + 1
        delay(0.01)

