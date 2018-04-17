# coding=utf-8
"""
OOP API to RV engine.
Functional API in SQF
Wishlist;
    refactor to includ mixins for common attributes that may not share and ancestor.
"""
__author__ = "Lonja Selter"
__credits__ = ["Lonja Selter"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Lonja Selter"
__email__ = "LoenjaSelter@gmail.com"
__status__ = "Development"

from .man import RV_Man
from . import sqf
player = sqf.player() #create module wide reference to player object
