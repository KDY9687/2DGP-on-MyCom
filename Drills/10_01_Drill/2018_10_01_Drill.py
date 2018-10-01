import turtle
import random
from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def move_point_to_point(p1, p2):
    global x, y, face, frame
    global move
    divide_x = (p1[0] - p2[0])
    for i in range(0, 100 + 1, 2):
        t = i /100
        x = (1-t)*p1[0]+t*p2[0]
        y = (1-t)*p1[1]+t*p2[1]
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        if p1[0] < p2[0]:
            face = 1
        else:
            face = 0
        character.clip_draw(frame * 100, face * 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
size = 20
frame = 0
face = 0
points = [(random.randint(0, 1280), random.randint(0, 1024)) for i in range(size)]
n = 0

while running:
    clear_canvas()
    move_point_to_point((x, y), points[n])
    n += 1
    update_canvas()
    frame = (frame + 1) % 8
    if n == 20 - 1:
        n = 0
    delay(0.05)

turtle.done()
close_canvas()