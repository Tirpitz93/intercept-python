from typing import Sequence


class RV_Marker(object):
    @property
    def pos(self)->Sequence:raise NotImplementedError

    @property
    def name(self)->str:raise NotImplementedError

    @property
    def size(self)-> float: raise NotImplementedError

    @property
    def bounds(self)->Sequence: raise NotImplementedError

    def position_in(self, position:Sequence)->bool: raise NotImplementedError