from components import Position, RenderData
from ecs import ComponentManager, Entity


def intersection(*managers):
    entities = set(range(Entity.cur_id + 1))
    for manager in managers:
        entities = entities.intersection(set(manager.all_entities()))
    all_classes = [manager.cls for manager in managers]
    all_manager = ComponentManager(tuple(all_classes))
    for entity in entities:
        all_component = tuple([m.get(entity) for m in managers])
        all_manager.add(all_component, entity)

    return all_manager


position_manager = ComponentManager(Position)
render_data_manager = ComponentManager(RenderData)


if __name__ == "__main__":
    from collections import namedtuple
    for i in range(10):
        e = Entity.create()
        position_manager.add(Position(i, i), e)
        render_data_manager.add(RenderData(chr(65 + i), "blue"), e)

    print(intersection(position_manager,
                       render_data_manager))
