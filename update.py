from component_managers import position_manager, render_data_manager, \
    intersection
from components import Position, RenderData


def neighbors(pos):
    return [(x, y)
            for x in range(pos.x - 1, pos.x + 2)
            for y in range(pos.y - 1, pos.y + 2)
            if not (x == pos.x and y == pos.y)
            if 0 <= x < 80 and 0 <= y < 25]


def update(field):
    live_queue = []
    dead_queue = []
    pos_rend_manager = intersection(position_manager, render_data_manager)
    for cell in pos_rend_manager.all_entities():
        pos_rend = pos_rend_manager.get(cell)
        pos = pos_rend[0]
        rend = pos_rend[1]
        neighbor_list = neighbors(pos)
        num_neighbors = 0
        for neighbor in neighbor_list:
            entity_in_field = field[neighbor[0]][neighbor[1]]
            if entity_in_field is not None:
                if render_data_manager.get(entity_in_field).glyph == '#':
                    num_neighbors += 1

        if rend.glyph == "#":
            if 2 <= num_neighbors < 4:
                live_queue.append(cell)
            else:
                dead_queue.append(cell)
        else:
            if num_neighbors == 3:
                live_queue.append(cell)

    for cell in live_queue:
        render_data_manager.replace(RenderData('#', None), cell)

    for cell in dead_queue:
        render_data_manager.replace(RenderData(' ', None), cell)


if __name__ == "__main__":
    from ecs import Entity
    cells = [Entity.create() for _ in range(4)]
    position_manager.add(Position(10, 10), cells[0])
    position_manager.add(Position(11, 10), cells[1])
    position_manager.add(Position(10, 11), cells[2])
    position_manager.add(Position(11, 11), cells[3])
    render_data_manager.add(RenderData('#', None), cells[0])
    render_data_manager.add(RenderData('#', None), cells[1])
    render_data_manager.add(RenderData('#', None), cells[2])
    render_data_manager.add(RenderData(' ', None), cells[3])
    field = [[None for y in range(100)] for x in range(100)]
    for entity in position_manager.all_entities():
        pos = position_manager.get(entity)
        field[pos.x][pos.y] = entity
    
    update(field)
