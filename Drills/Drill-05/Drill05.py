from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

Point_List = [[203, 535], [132, 243], [535, 470], [477, 203], [715, 136], [316, 225], [510, 92], [692, 518], [682, 336],
              [712, 349]]

def move_right(divided_x, divided_y, index):
    frame = 0
    x = Point_List[index][0]
    y = Point_List[index][1]
    repeat = 0
    pass

def move_reft(divdivided_x, divided_y, index):
    frame = 0
    x = Point_List[index][0]
    y = Point_List[index][1]
    repeat = 0
    pass

def move_point_to_point(index):
    divided_x = (Point_List[index+1][0] - Point_List[index][0]) / 30
    divided_y = (Point_List[index + 1][1] - Point_List[index][1]) / 30
    pass
close_canvas()

