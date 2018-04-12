# coding=utf-8
"""
Location class
"""
from abc import ABC
from typing import Sequence

from .marker import RV_Marker


class RV_Location(RV_Marker):

    @property
    def type(self)->str:raise NotImplementedError


