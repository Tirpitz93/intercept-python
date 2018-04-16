# coding=utf-8
"""RV engine object, wraps arma 3 engine. provides engine wide commands and properties.
"""
from abc import ABC

from .libs.singleton import Singleton


class RV_Engine(ABC, Singleton):
    def __init__(self):
        """Get the RV engine to carry out all operations on.
        Singleton: Can only ever access one RV engine.
        """
        raise NotImplementedError