# coding=utf-8
from abc import ABC

from engine import RV_Engine


class RV_Base(ABC):
    """Helper methods to get objects from engine. Provides basic interfaces.
    Private. Should not be required by Intercept python users (mod creators).
    To set custom variables equivalent to SQF:
        _object setVariable ["variableName", "myValue"];
    use:
        >>> myObject= RV_Base()
        >>>myObject["variableName"] = "myValue"
        >>>myObject["variablename"] ## "myValue"
    for ease of adoption get_variable & set_variable is also provided:

        >>>myObject.set_variable("variableName", "myValue")
        >>>myObject.get_variable("variableName", default="fallbackValue") ## "myValue"
        >>>myObject.get_variable("anothervariableName", default="fallbackValue") ## "fallbackValue"

    """
    def __init__(self, slug:str ="player", engine:RV_Engine=RV_Engine()):
        self._slug =  slug
        self._engine = engine
        self._ptr =None
        raise NotImplementedError

    def __getattr__(self, item): raise NotImplementedError # default behaviour if attr does not exist

    def __setattr__(self, item, value): raise NotImplementedError

    def __getitem__(self, item, default = None):
        return  sqf.misc.get_variable(self._ptr, item, default) # fixme
        raise NotImplementedError

    def __setitem__(self, key, value):
        return  sqf.misc.set_variable(self._ptr, key, value) # fixme
        raise NotImplementedError


    def get_variable(self, variable:str, default=None):
        return self.__getitem__(item=variable, default=default)