"""

:author: Christian Gram Kalhauge 

An wraper around SDL, to make it more pythonic.

"""
import sdl2 as _s
from . import utils
from enum import Enum

class SubSystem(utils.Flags):
    timer = _s.SDL_INIT_TIMER
    audio = _s.SDL_INIT_AUDIO
    video = _s.SDL_INIT_VIDEO
    joystick = _s.SDL_INIT_JOYSTICK
    haptic = _s.SDL_INIT_HAPTIC
    gamecontroller = _s.SDL_INIT_GAMECONTROLLER
    events = _s.SDL_INIT_EVENTS
    everything = _s.SDL_INIT_EVERYTHING
    noparachute = _s.SDL_INIT_NOPARACHUTE 

def init(flags={}) -> None:
    """ SDL_Init """
    retval = _s.SDL_Init(SubSystem.process(flags))
    assert retval == 0, error(retval) 

def init_sub_system(flags={}) -> None:
    retval = _s.SDL_InitSubSystem(SubSystem.process(flags))
    assert retval == 0, error(retval)

def quit() -> None:
    retval = _s.SDL_Quit()

def quit_sub_system(flags={}) -> None:
    _s.SDL_QuitSubSystem(SubSystem.process(flags))

def get_error() -> str:
    return bytes(_s.SDL_GetError()).decode('UTF-8')

def error(retval):
    return "Error {}: {}".format(retval, get_error())

