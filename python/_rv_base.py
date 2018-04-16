# coding=utf-8
from abc import ABC

from engine import RV_Engine


class RV_Base(ABC):
    """Helper methods to get objects from engine.
    Private. Should not be required by Intercept python users (mod creators).
    """
    def __init__(self, engine:RV_Engine=RV_Engine()):raise NotImplementedError

    def __getattr__(self, item): raise NotImplementedError # default behaviour if attr does not exist

    def __getattribute__(self, item): raise  NotImplementedError #get attribute if it exists
        # dig into Intercept and get value

    def __setattr__(self, key, value): raise NotImplementedError