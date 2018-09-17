from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

Point_List = [[203, 535], [132, 243], [535, 470], [477, 203], [715, 136], [316, 225], [510, 92], [692, 518],
                [682, 336], [712, 349], [203, 535]]

def move_right(divided_x, divided_y, index):
    frame = 0
    x = Point_List[index][0]
    y = Point_List[index][1]
    repeat = 0

    while repeat != 30:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += divided_x
        y += divided_y
        repeat += 1
        delay(0.05)
        get_events()

def move_reft(divided_x, divided_y, index):
    frame = 0
    x = Point_List[index][0]
    y = Point_List[index][1]
    repeat = 0

    while repeat != 30:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += divided_x
        y += divided_y
        repeat += 1
        delay(0.05)
        get_events()

def move_point_to_point(index):
    divided_x = (Point_List[index + 1][0] - Point_List[index][0]) / 30
    divided_y = (Point_List[index + 1][1] - Point_List[index][1]) / 30
    if divided_x < 0:
        move_reft(divided_x, divided_y, index)
    elif divided_x >0:
        move_right(divided_x, divided_y, index)



index = 0

while True:
    move_point_to_point(index)
    if index < 9:
        index += 1
    elif index >= 9:
        index = 0

