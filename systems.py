from bearlibterminal import terminal as blt
from render import initialize_render, render, terminate_render
from read_map import read_map
from update import update


def game_loop():
    field = read_map("map.txt")
    speed = 100
    initialize_render()
    while True:
        if blt.has_input():
            key = blt.read()
            if key == blt.TK_A:
                speed = 1000
            if key == blt.TK_S:
                speed = 500
            if key == blt.TK_D:
                speed = 100
            if key == blt.TK_F:
                speed = 10
                
            if key == blt.TK_CLOSE or key == blt.TK_Q:
                break
        update(field)
        render()
        blt.delay(speed)
    terminate_render()


if __name__ == "__main__":

    game_loop()
