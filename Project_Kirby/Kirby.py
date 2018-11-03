import game_framework
from pico2d import *

import math
import random
import game_world

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, S_DOWN, SPACE, A_DOWN = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_s): S_DOWN,
    (SDL_KEYDOWN, SDLK_a): A_DOWN,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}

class IdleState:

    @staticmethod
    def enter(kirby, event):
        if event == RIGHT_DOWN:
            kirby.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            kirby.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            kirby.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            kirby.velocity += RUN_SPEED_PPS
        kirby.timer = get_time()

    @staticmethod
    def exit(kirby, event):
        pass

    @staticmethod
    def do(boy):
        pass

    @staticmethod
    def draw(boy):
        pass


class RunState:

    @staticmethod
    def enter(kirby, event):
        if event == RIGHT_DOWN:
            kirby.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            kirby.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            kirby.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            kirby.velocity += RUN_SPEED_PPS
        kirby.dir = clamp(-1, kirby.velocity, 1)

    @staticmethod
    def exit(kirby, event):
        pass

    @staticmethod
    def do(kirby):
        pass

    @staticmethod
    def draw(kirby):
        pass



class JumpState:

    @staticmethod
    def enter(kirby, event):
        if event == RIGHT_DOWN:
            kirby.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            kirby.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            kirby.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            kirby.velocity += RUN_SPEED_PPS
        kirby.dir = clamp(-1, kirby.velocity, 1)

    @staticmethod
    def exit(kirby, event):
        pass

    @staticmethod
    def do(kirby):
        pass

    @staticmethod
    def draw(kirby):
        pass


class AttackState:

    @staticmethod
    def enter(kirby, event):
        pass

    @staticmethod
    def exit(kirby, event):
        pass

    @staticmethod
    def do(kirby):
        pass

    @staticmethod
    def draw(kirby):
        pass


class AbsortionState:

    @staticmethod
    def enter(kirby, event):
       pass

    @staticmethod
    def exit(kirby, event):
        pass

    @staticmethod
    def do(kirby):
        pass

    @staticmethod
    def draw(kirby):
        pass


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, A_DOWN: AttackState, SPACE: JumpState,
                S_DOWN: AbsortionState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState},
    JumpState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, SPACE: IdleState},
    AbsortionState: {S_DOWN: AbsortionState},
    AttackState: {A_DOWN: AttackState}
}


class kirby:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('kirby.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)



    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
