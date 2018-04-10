from typing import Sequence

from .object import RV_Object

class RV_Building(RV_Object):

    def __init__(self):
        super().__init__()

    def building_exit(self, index:int)->Sequence:raise NotImplementedError # todo

    def building_pos(self, index:int)->Sequence: raise NotImplementedError # todo
