from bearlibterminal import terminal as blt
from component_managers import position_manager, render_data_manager, \
    intersection


def initialize_render():
    pos_rend_manager = intersection(position_manager, render_data_manager)
    blt.open()
    for pos_rend in pos_rend_manager.all_components():
        blt.put(pos_rend[0].x, pos_rend[0].y, pos_rend[1].glyph)
    blt.refresh()


def render():
    pos_rend_manager = intersection(position_manager, render_data_manager)
    blt.clear()
    for pos_rend in pos_rend_manager.all_components():
        blt.put(pos_rend[0].x, pos_rend[0].y, pos_rend[1].glyph)
    blt.refresh()


def terminate_render():
    blt.close()


if __name__ == "__main__":
    from ecs import Entity
    from components import Position, RenderData
    for i in range(10):
        e = Entity.create()
        position_manager.add(Position(i, i), e)
        render_data_manager.add(RenderData(chr(65 + i), "foo"), e)
    initialize_render()
    while blt.read() != blt.TK_CLOSE:
        render()
    terminate_render()
