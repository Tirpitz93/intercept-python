from python.object import RV_Object
from python.vehicle import RV_Vehicle
from .unit import RV_Unit

class RV_Man(RV_Unit):
    raise NotImplementedError

    def add_magazine(self, name:str, ammo_count:float = 1)->None:raise NotImplementedError

    def play_move(self,name:str)->None:raise NotImplementedError

    def play_move_now(self, name:str)->None:raise NotImplementedError

    def remove_all_weapons(self)->None:raise NotImplementedError

    def remove_magazine(self, name:str)->None:raise NotImplementedError

    def remove_magazines(self, name:str)->None:raise NotImplementedError

    def remove_weapon(selfweapon:str)->None:raise NotImplementedError

    @property
    def hands_hit(self)->float:raise NotImplementedError

    def move_in_cargo(self,vehicle:RV_Vehicle)->None:raise NotImplementedError

    @property
    def primary_weapon(self)->RV_Object:raise NotImplementedError

    @property
    def vehicle(self)->RV_Object:raise NotImplementedError



