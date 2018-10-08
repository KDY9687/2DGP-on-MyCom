import turtle
import random
from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def draw_curved_line(p1, p2, p3, p4, start_point):

    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2

def move_point_to_point(p1, p2, p3, p4, start_point):
    global x, y, face, frame
    global move
    divide_x = (p1[0] - p2[0])
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        if p2[0] < p3[0]:
            face = 1
        else:
            face = 0
        character.clip_draw(frame * 100, face * 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)

number = 10
p = [(random.randint(0, 900), random.randint(0, 900)) for i in range(number)]

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
    move_point_to_point(p[0], p[1], p[2], p[3], p[1])
    move_point_to_point(p[1], p[2], p[3], p[4], p[2])
    move_point_to_point(p[2], p[3], p[4], p[5], p[3])
    move_point_to_point(p[3], p[4], p[5], p[6], p[4])
    move_point_to_point(p[4], p[5], p[6], p[7], p[5])
    move_point_to_point(p[5], p[6], p[7], p[8], p[6])
    move_point_to_point(p[6], p[7], p[8], p[9], p[7])
    move_point_to_point(p[7], p[8], p[9], p[0], p[8])
    move_point_to_point(p[8], p[9], p[0], p[1], p[9])
    move_point_to_point(p[9], p[0], p[1], p[2], p[0])
    n += 1
    update_canvas()
    frame = (frame + 1) % 8
    if n == 20 - 1:
        n = 0
    delay(0.05)


close_canvas()