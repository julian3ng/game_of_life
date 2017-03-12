from typing import TypeVar, Dict, Generic, ValuesView, KeysView, List, Optional


class Entity(object):
    cur_id: int = -1

    @staticmethod
    def create() -> int:
        Entity.cur_id += 1
        return Entity.cur_id


T = TypeVar('T')


class ComponentManager(Generic[T]):
    def __init__(self, cls: T) -> None:
        self.cls: T = cls
        self.table: Dict[int, T] = {}

    def add(self, comp: T, entity: int) -> None:
        if not self.table.get(entity):
            self.table[entity] = comp

    def replace(self, comp: T, entity: int) -> None:
        if self.table.get(entity):
            self.table[entity] = comp
        else:
            raise IndexError("Entity has no component of this type")

    def rm(self, entity: int) -> None:
        del(self.table[entity])

    def get(self, entity: int) -> Optional[T]:
        return self.table.get(entity)

    def has(self, entity: int) -> bool:
        return self.table.get(entity) is not None

    def all_components(self) -> ValuesView[T]:
        return self.table.values()

    def all_entities(self) -> KeysView[int]:
        return self.table.keys()

    def __str__(self) -> str:
        return "\n".join("{!s}: {!s}".format(k, v)
                         for k, v in self.table.items())
