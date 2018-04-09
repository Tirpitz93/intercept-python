__author__ = "Lonja Selter"

"""
Base ingame object wrapper
provides pythonic interface to SQF engine

get_<propertyName>() is available as obj.<propertyName>
set_<propertName>(val) is available as obj.<propertyname> = val

todo: possibly add literal methods eg "get_pos()" as well as @property variants, the docorated methods seams cleaner and therefor more pythonic.
"""

class RV_Object(object): # todo: rename according to conventions???
    def __init__(self):
        # todo
        ## aliases
        self.pos_atl = self.pos
        self.position = self.pos
        pass



    #######################
    ## POSITIONAL STUFF
    #######################
    @property
    def pos(self)->tuple:pass

    @pos.setter
    def pos(self, pos:tuple)->None:pass

    # def get_pos(self)->tuple: pass # todo
    #
    # def set_pos(self, pos:tuple)->None: pass # todo

    @property
    def pos_asl(self)->tuple:pass # todo

    @pos_asl.setter
    def pos_asl(self, pos:tuple)->tuple:pass

    # def set_pos_asl(self, pos:tuple)->None:pass # todo
    #
    # def get_pos_asl(self)->tuple:pass # todo

    @property
    def pos_visual(self) -> tuple: pass # todo

    @pos_visual.setter
    def pos_visual(self, pos: tuple) -> None: pass # todo


    @property
    def pos_atl_visual(self)->tuple:pass # todo

    @pos_atl_visual.setter
    def pos_atl_visual(self, pos:tuple)->None:pass # todo

    @property
    def is_alive(self)->bool:pass # todo

    def detach(self)->None:pass # todo

    @property
    def action_ids(self)->list:pass # todo

    def attach_to(self)->None:pass # todo
    @property
    def alive(self)->bool: pass  # todo

    @property
    def velocity(self)->float:pass  # todo

    @property
    def name(self)->str:pass  # todo

    @property
    def type_of(self)->str:pass  # todo

    def inflame(self, burn)->None:pass  # todo

    @property
    def inflamed(self)->bool:pass  # todo

    def remove_action(self, index)->None:pass  # todo

    def reveal_target(self, target)->None:pass  # todo

    @property
    def object_parent(self)->object:pass  # todo: indicate correct class

    @property
    def every_container(self)->tuple:pass  # todo

    @property
    def every_backpack(self)->tuple:pass  # todo

    @property
    def damage(self)->float:pass # todo

    @damage.setter
    def damage(self, damage:float)->None:pass # todo

    @property
    def hit(self)->float:pass # todo

    @property
    def hit_point_damage(self)->float:pass # todo

    def allow_damage(self, allowDamage:bool)->None:pass # todo

    @property
    def damage_allowed(self)->bool:pass # todo

    @property
    def local(self)->bool:pass # todo