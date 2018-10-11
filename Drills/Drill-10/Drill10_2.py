import game_framework
from pico2d import *
import main_state


name = "Drill10_2"
image = None
count = 0

def enter():
    global image
    image = load_image('pause_2.png')


def exit():
    global image
    del(image)


def handle_events():
    global count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                count = 0
                game_framework.pop_state()

def draw():
    global count
    clear_canvas()
    main_state.boy.draw()
    main_state.grass.draw()
    if count == 0:
        image.draw(400, 300)
        count += 1
    elif count == 1:
        count -= 1
    delay(0.3)
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass






