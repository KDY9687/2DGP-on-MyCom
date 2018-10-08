from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw (self):
        self.image.draw(400, 30)
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 560
        self.kinds = random.randint(0, 1)
        if self.kinds == 0:
            self.image1 = load_image('ball21x21.png')
        else:
            self.image2 = load_image('ball41x41.png')
        self.speed = random.randint(6, 10)

    def update(self):
        for i in range(self.speed):
            if self.y != 40:
                self.y -= 1

    def draw(self):
        if self.kinds == 0:
            self.image1.clip_draw(0, 0, 21, 21, self.x, self.y+21)
        else:
            self.image2.clip_draw(0, 0, 41, 41, self.x, self.y+30)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()
boy = Boy()
grass = Grass()
ball = Ball()

team = [Boy() for i in range(11)]
balls = [Ball() for i in range(21)]

running = True

while running:
    handle_events()

    for boy in team:
        boy.update()

    for ball in balls:
        ball.update()

    clear_canvas()
    grass.draw()

    for boy in team:
        boy.draw()

    for ball in balls:
        ball.draw()

    update_canvas()
    delay(0.05)

close_canvas()