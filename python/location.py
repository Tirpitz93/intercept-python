# coding=utf-8
"""
Location class
"""
from abc import ABC
from typing import Sequence


class RV_Location(ABC):

    @property
    def pos(self)->Sequence:raise NotImplementedError

    @property
    def name(self)->str:raise NotImplementedError

    @property
    def size(self)-> float: raise NotImplementedError

    @property
    def bounds(self)->Sequence: raise NotImplementedError

