from pygame.locals import *
import pygame
import datetime


# class meaningless for now
class AttackAnimation:
    def __init__(self,arg_startup_end,arg_active_end,arg_recover_end) -> None:
        self.startup_end = arg_startup_end 
        self.active_end = arg_active_end
        self.recover_end = arg_recover_end
        self.image_array=[]
    def set_image_array(self,i_array):
        self.image_array = i_array

class Attack:

    def __init__(self,arg_key,arg_animation=None,arg_cancelable=False)->None:
         self.key = arg_key
         # the same attack instances can have different animations
         self.animation = arg_animation # meaningless for now
         self.cancelable = arg_cancelable # meaningless for now
        
class Combo:
    def __init__(self):
        self.attacks = []
        self.current_attack = 0
    def add_attack(self,arg_attack):
        self.attack.append(arg_attack)
    
class InputBuffer:
    def __init__(self) -> None:
        self.inputs = []
    def clean_olds(self):
        for input,idx in enumerate(self.inputs):
            if((input.emit_time-datetime.datetime.now()).microseconds > 1000000):
                self.inputs[idx]=None

# Constant existing for the whole combat
# creation & initialization when you choose the fighter having it
# cleaned when fight end

s_d_combo = Combo()
d_after_s_animation = None
s_d_combo.add_attack(Attack(arg_key='s'))
s_d_combo.add_attack(Attack(arg_key='d',arg_animation=d_after_s_animation))




class ComboHandler:
    def __init__(self) -> None:
        self.inputs = []
    def clean_olds(self):
        pass