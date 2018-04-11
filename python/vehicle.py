# coding=utf-8
"""
    Vehicle object api.
    wishlist:
        get_passengers
        get_driver
        get_gunner/get_gunners
        get_inventory/set_inventory


"""

from typing import Sequence

from python.object import RV_Object
from .unit import RV_Unit
from python.definitions import RV_RadarRule


class RV_Vehicle(RV_Unit):

    def set_vehicle_position(self, position:Sequence,markers:Sequence)->None:raise NotImplementedError # todo

    def can_vehicle_cargo(self, object:RV_Object)->Sequence:raise NotImplementedError # todo

    def set_radar_rule(self, RV_RadarRule)->RV_RadarRule:raise NotImplementedError # todo

    @property
    def ropes(self)->Sequence:raise NotImplementedError # todo

    def rope_create(self, from_point, to_obj, to_point, segments, length:float=None)->RV_Object:raise NotImplementedError # todo

    def is_engine_on(self)->bool:raise NotImplementedError # todo should this be a property with which you can set motor on/off?

    @property
    def allow_get_in(self)->bool:raise NotImplementedError

    @property
    def crew(self)->Sequence: raise NotImplementedError

    def assign_as_cargo(self, unit:RV_Unit)->None: raise NotImplementedError

    def assign_role(self, unit:RV_Unit, role): raise NotImplementedError