# coding=utf-8
from typing import Sequence

from python.group import RV_Group
from .object import RV_Object


class RV_Unit(RV_Object):

    @property
    def group(self) -> RV_Object:
        """
        Group object that this unit belongs to.
        """
        raise NotImplementedError  # possibly requires now class for groups

    @group.setter
    def group(self,
              group: RV_Group) -> None: raise NotImplementedError  # if group is a group then add to, else add to group of unit.

    @property
    def skill(self, skill_type: str = None) -> float: raise NotImplementedError

    @skill.setter
    def skill(self, skill: float) -> None: raise NotImplementedError

    def skill_final(self, sub_skill: str) -> float: raise NotImplementedError

    def knows_about(self, target: RV_Object) -> float: raise NotImplementedError

    def move(self, position: Sequence) -> None: raise NotImplementedError



    @property
    def name(self)->str:raise NotImplementedError




