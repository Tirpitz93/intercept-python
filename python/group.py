from python.object import RV_Object
from python.unit import RV_Unit
from python.definitions import RV_side

class RV_Group(RV_Object):
    """
    Group object.
    """

    def __init__(self):
        super().__init__()
        raise NotImplementedError

    def add_unit(self, unit:RV_Unit)->None:raise NotImplementedError

    @property
    def units(self):
        raise NotImplementedError

    @property
    def side(self)->RV_side:raise NotImplementedError
