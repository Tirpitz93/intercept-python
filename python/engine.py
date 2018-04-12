from abc import ABC

from .libs.singleton import Singleton


class RV_Engine(ABC, Singleton):
    def __init__(self):
        """Get the RV engine to carry out all operations on.
        """
        raise NotImplementedError