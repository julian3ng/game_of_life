from ecs import Entity
from components import Position, RenderData
from component_managers import position_manager, render_data_manager


def read_map(mapfile):
    field = [[Entity.create() for x in range(25)] for y in range(80)]

    for x, row in enumerate(field):
        for y, cell in enumerate(row):
            position_manager.add(Position(x, y), cell)
            render_data_manager.add(RenderData(" ", None), cell)


    with open(mapfile, 'r') as the_map:
        for y, line in enumerate(the_map):
            if y > 25:
                break
            for x, char in enumerate(line):
                if x > 80:
                    break
                if char not in ["#", " "]:
                    render_data_manager.replace(RenderData(" ", None),
                                                field[x][y])
                else:
                    render_data_manager.replace(RenderData(char, None),
                                                field[x][y])

    return field
