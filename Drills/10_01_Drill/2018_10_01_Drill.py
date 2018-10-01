import turtle
import random
from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def move_point_to_point(p1, p2):
    global x, y, face, frame
    global move
def draw_line(p1, p2):
    global x, y

    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = (1-t)*p1[0]+t*p2[0]
        y = (1-t)*p1[1]+t*p2[1]


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
running = True
x = 0
y = 0
size = 10
points = [(random.randint(-500, 500), random.randint(-350, 350)) for i in range(size)]
n = 1

while running:
    clear_canvas()
    draw_line(points[n-1], points[n])
    n = (n+1) % size
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.05)

turtle.done()
close_canvas()