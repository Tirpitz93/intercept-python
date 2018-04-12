# coding=utf-8
"""

"""
from abc import ABC


class RV_Namespace(ABC):
    def __get__(self, instance, owner):raise NotImplementedError

    def __init__(self): raise NotImplementedError

