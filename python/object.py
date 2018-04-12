

from .rv_base import RV_Base

__author__ = "Lonja Selter"
"""
Base ingame object wrapper
provides pythonic interface to SQF engine

get_<propertyName>() is available as obj.<propertyName>
set_<propertName>(val) is available as obj.<propertyname> = val

todo: possibly add literal methods eg "get_pos()" as well as @property variants, the docorated methods seams cleaner and therefor more pythonic.
"""
from typing import Sequence
class RV_Object(RV_Base): # todo: rename according to conventions???
    def __init__(self, name: str, namespace: str= "missionNamespace")->None:
        self._name = name
        self._namespace = namespace
        # todo
        ## aliases
        self.pos_atl = self.pos  # default position is ATL
        self.position = self.pos # Position is an alias for pos
        self.set_position = self.set_pos # ditto
    def __get__(self, instance, owner):
        raise NotImplementedError
        # return  self.namespace.getvariable(name)



    #######################
    ## POSITIONAL STUFF
    #######################
    @property
    def pos(self)->Sequence:raise NotImplementedError

    @pos.setter
    def pos(self, pos:Sequence)->None:raise NotImplementedError

    def get_pos(self)->Sequence: raise NotImplementedError # todo

    def set_pos(self, pos:Sequence)->None: raise NotImplementedError # todo

    def set_pos_world(self, pos:Sequence)->None: raise NotImplementedError # todo


    @property
    def pos_asl(self)->Sequence:raise NotImplementedError # todo

    @pos_asl.setter
    def pos_asl(self, pos:Sequence)->Sequence:raise NotImplementedError

    def set_pos_asl(self, pos: Sequence) -> None: raise NotImplementedError  # todo

    def get_pos_asl(self) -> Sequence: raise NotImplementedError  # todo

    def set_pos_asl2(self, pos:Sequence)->None:raise NotImplementedError # todo what is this?


    @property
    def pos_aslw(self)->Sequence:raise NotImplementedError # todo

    @pos_aslw.setter
    def pos_aslw(self, pos:Sequence)->Sequence:raise NotImplementedError

    def set_pos_aslw(self, pos:Sequence)->None:raise NotImplementedError # todo

    def get_pos_aslw(self)->Sequence:raise NotImplementedError # todo


    @property
    def pos_visual(self) -> Sequence: raise NotImplementedError # todo

    @pos_visual.setter
    def pos_visual(self, pos: Sequence) -> None: raise NotImplementedError # todo


    @property
    def pos_atl_visual(self)->Sequence:raise NotImplementedError # todo

    @pos_atl_visual.setter
    def pos_atl_visual(self, pos:Sequence)->None:raise NotImplementedError # todo

    @property
    def is_alive(self)->bool:raise NotImplementedError # todo

    def detach(self)->None:raise NotImplementedError # todo

    @property
    def action_ids(self)->list:raise NotImplementedError # todo

    def attach_to(self)->None:raise NotImplementedError # todo
    @property
    def alive(self)->bool: raise NotImplementedError  # todo

    @property
    def velocity(self)->float:raise NotImplementedError  # todo


    @property
    def type_of(self)->str:raise NotImplementedError  # todo

    def inflame(self, burn)->None:raise NotImplementedError  # todo

    @property
    def inflamed(self)->bool:raise NotImplementedError  # todo

    def remove_action(self, index)->None:raise NotImplementedError  # todo

    def reveal_target(self, target)->None:raise NotImplementedError  # todo

    @property
    def object_parent(self)->object:raise NotImplementedError  # todo: indicate correct class

    @property
    def every_container(self)->Sequence:raise NotImplementedError  # todo

    @property
    def every_backpack(self)->Sequence:raise NotImplementedError  # todo

    @property
    def damage(self)->float:raise NotImplementedError # todo

    @damage.setter
    def damage(self, damage:float)->None:raise NotImplementedError # todo

    @property
    def hit(self)->float:raise NotImplementedError # todo

    @property
    def hit_point_damage(self)->float:raise NotImplementedError # todo

    def allow_damage(self, allow_damage:bool)->None:raise NotImplementedError # todo

    @property
    def damage_allowed(self)->bool:raise NotImplementedError # todo

    @property
    def local(self)->bool:raise NotImplementedError # todo

    @property
    def variable_name(self)->str: raise NotImplementedError