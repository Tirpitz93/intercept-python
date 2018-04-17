# coding=utf-8
from abc import ABC

from engine import RV_Engine


class RV_Base(ABC):
    """Helper methods to get objects from engine.
    Private. Should not be required by Intercept python users (mod creators).
    """
    def __init__(self, slug:str ="player", engine:RV_Engine=RV_Engine()):
        self._slug =  slug
        self._engine = engine
        self._ptr =None
        raise NotImplementedError

    def __getattr__(self, item): raise NotImplementedError # default behaviour if attr does not exist

    def __getattribute__(self, item): raise  NotImplementedError #get attribute if it exists

        # dig into Intercept and get value


    def __setattr__(self, key, value): raise NotImplementedError

    def get_variable(self, variable:str, default=None):
        return sqf.misc.get_variable(self._ptr, variable, default)