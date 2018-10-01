from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def move_to_goal(target_x, target_y):
    global boy_x, boy_y, face, frame
    global move
    move = True
    divide_x = (target_x - boy_x) / 40
    divide_y = (target_y - boy_y) / 40
    for i in range(1, 40 + 1):
        if move:
            if divide_x < 0:
                face =0
            else:
                face = 1
            clear_canvas()
            kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
            character.clip_draw(frame * 100, 100 * face, 100, 100, boy_x, boy_y)
            hand.draw_now(x + 20, y - 25)
            update_canvas()
            boy_x += divide_x
            boy_y += divide_y
            frame = (frame + 1) % 8
            handle_events()
            delay(0.05)
    move = False

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            move_to_goal(x, y)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
move = False
face = 0
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
target_x, target_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
boy_x, boy_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    if move == False:
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * face, 100, 100, boy_x, boy_y)
        hand.draw_now(x + 20, y- 25)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
        handle_events()

close_canvas()




