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

    def is_engine_on(self)->bool:raise NotImplementedError # todo should this be a property with which you can set motor on/off
