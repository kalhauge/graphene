import sdl2 as _s
import ctypes

from enum import Enum

class EventType(Enum):
    firstevent = _s.SDL_FIRSTEVENT
    quit = _s.SDL_QUIT
    app_terminating = _s.SDL_APP_TERMINATING
    app_low_memory = _s.SDL_APP_LOWMEMORY
    app_will_enter_background = _s.SDL_APP_WILLENTERBACKGROUND
    app_did_enter_background = _s.SDL_APP_DIDENTERBACKGROUND
    app_will_enter_foreground = _s.SDL_APP_WILLENTERFOREGROUND
    app_did_enter_foreground = _s.SDL_APP_DIDENTERFOREGROUND
    window_event = _s.SDL_WINDOWEVENT
    sys_wm_event = _s.SDL_SYSWMEVENT
    key_down = _s.SDL_KEYDOWN
    key_up = _s.SDL_KEYUP
    text_editing = _s.SDL_TEXTEDITING
    text_input = _s.SDL_TEXTINPUT
    mouse_motion = _s.SDL_MOUSEMOTION
    mouse_button_down = _s.SDL_MOUSEBUTTONDOWN
    mouse_button_up = _s.SDL_MOUSEBUTTONUP
    mouse_wheel = _s.SDL_MOUSEWHEEL
    joy_axis_motion = _s.SDL_JOYAXISMOTION
    joy_ball_motion = _s.SDL_JOYBALLMOTION
    joy_hat_motion = _s.SDL_JOYHATMOTION
    joy_button_down = _s.SDL_JOYBUTTONDOWN
    joy_button_up = _s.SDL_JOYBUTTONUP
    joy_device_added = _s.SDL_JOYDEVICEADDED
    joy_device_removed = _s.SDL_JOYDEVICEREMOVED
    controller_axis_motion = _s.SDL_CONTROLLERAXISMOTION
    controller_button_down = _s.SDL_CONTROLLERBUTTONDOWN
    controller_button_up = _s.SDL_CONTROLLERBUTTONUP
    controller_device_added = _s.SDL_CONTROLLERDEVICEADDED
    controller_devicere_moved = _s.SDL_CONTROLLERDEVICEREMOVED
    controller_devicere_mapped = _s.SDL_CONTROLLERDEVICEREMAPPED
    finger_down = _s.SDL_FINGERDOWN
    finger_up = _s.SDL_FINGERUP
    finger_motion = _s.SDL_FINGERMOTION
    dollar_gesture = _s.SDL_DOLLARGESTURE
    dollar_record = _s.SDL_DOLLARRECORD
    multigesture = _s.SDL_MULTIGESTURE
    clipboard_update = _s.SDL_CLIPBOARDUPDATE
    drop_file = _s.SDL_DROPFILE
    #render_targets_reset = _s.SDL_RENDER_TARGETS_RESET
    #render_device_reset = _s.SDL_RENDER_DEVICE_RESET
    user_event = _s.SDL_USEREVENT
    last_event = _s.SDL_LASTEVENT

    def create(self, event):
        try:
            return TYPES[self](getattr(event, TYPES[self].field))
        except KeyError:
            import warnings
            warnings.warn("{} not yet implemented.".format(self))


class Event:

    def __init__(self, handle):
        assert not handle is None
        self._handle = handle

    @classmethod
    def poll(cls):
        """ SDL_PollEvent """
        event = _s.SDL_Event()
        retval = _s.SDL_PollEvent(ctypes.byref(event))
        if retval == 0:
            return None
        else:
            return EventType(event.type).create(event)

def poll_event():
    """ SDL_PollEvent """
    return Event.poll()

def pending_events():
    while True:
        event = Event.poll()
        if event is None:
            break
        else:
            yield event


class Quit (Event):
    field = 'quit'

    @property
    def timestamp(self):
        return self._handle.timestamp

class WindowEventId(Enum):
    none = _s.SDL_WINDOWEVENT_NONE
    shown = _s.SDL_WINDOWEVENT_SHOWN
    hidden = _s.SDL_WINDOWEVENT_HIDDEN
    exposed = _s.SDL_WINDOWEVENT_EXPOSED
    moved = _s.SDL_WINDOWEVENT_MOVED
    resized = _s.SDL_WINDOWEVENT_RESIZED
    changed = _s.SDL_WINDOWEVENT_SIZE_CHANGED
    minimized = _s.SDL_WINDOWEVENT_MINIMIZED
    maximized = _s.SDL_WINDOWEVENT_MAXIMIZED
    restored = _s.SDL_WINDOWEVENT_RESTORED
    enter = _s.SDL_WINDOWEVENT_ENTER
    leave = _s.SDL_WINDOWEVENT_LEAVE
    gained = _s.SDL_WINDOWEVENT_FOCUS_GAINED
    lost = _s.SDL_WINDOWEVENT_FOCUS_LOST
    close = _s.SDL_WINDOWEVENT_CLOSE

class WindowEvent (Event):
    field = 'window'

    def __init__(self, handle):
        super(WindowEvent, self).__init__(handle)
        self.event = WindowEventId(self._handle.event)

    @property
    def timestamp(self):
        return self._handle.timestamp
  
    @property
    def window_id(self):
        return self._handle.window_id 

    @property
    def data1(self):
        return self._handle.data1

    @property
    def data2(self):
        return self._handle.data2


TYPES = {
    EventType.quit: Quit,
    EventType.window_event: WindowEvent
}
