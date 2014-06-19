
import sdl2 as _s

from . import utils

class WindowFlags(utils.Flags):
    fullscreen = _s.SDL_WINDOW_FULLSCREEN 
    fullscreen_desktop = _s.SDL_WINDOW_FULLSCREEN_DESKTOP
    opengl = _s.SDL_WINDOW_OPENGL
    shown = _s.SDL_WINDOW_SHOWN
    borderless = _s.SDL_WINDOW_BORDERLESS
    resizable = _s.SDL_WINDOW_RESIZABLE
    minmized = _s.SDL_WINDOW_MINIMIZED
    maximized = _s.SDL_WINDOW_MAXIMIZED 
    input_grabbed = _s.SDL_WINDOW_INPUT_GRABBED
    input_focus = _s.SDL_WINDOW_INPUT_FOCUS
    mouse_focus = _s.SDL_WINDOW_MOUSE_FOCUS
    foreign = _s.SDL_WINDOW_FOREIGN
    allow_highdpi = _s.SDL_WINDOW_ALLOW_HIGHDPI


class Window:
    
    POS_CENTER = {
        True: _s.SDL_WINDOWPOS_CENTERED, 
        False: _s.SDL_WINDOWPOS_UNDEFINED
    }

    def __init__(self, handle):
        assert not handle is None
        self._handle = handle

    def destroy(self):
        """
        SDL_DestroyWindow.
        """
        _s.SDL_DestroyWindow(self._handle)

    @staticmethod
    def create(title, center=(False, False), size=(600, 600), flags={}):
        """
        SDL_CreateWindow.
       
        Args:
            title: A String with the title
            center: A tuple indicating wether to center or not.
            size: the size in a tuple, in pixels.
            flags: a set of names, as described in SLD_WINDOW_*

        >>> create_window('MyWindow', (True, True), (100, 100), 
        ...               {'opengl','shown'})
        """
        x, y = center
        h, w = size
       
        whandle = _s.SDL_CreateWindow(
            title.encode('UTF-8'),
            Window.POS_CENTER[x], Window.POS_CENTER[y],
            h, w,
            WindowFlags.process(flags)
        )

        return Window(whandle)

    @property
    def surface(self):
        from .surface import Surface
        return Surface(_s.SDL_GetWindowSurface(self._handle))

    def update(self):
        _s.SDL_UpdateWindowSurface(self._handle)

def create_window(title, center, size, **kwargs) -> Window:
    """
    Creates an window, equivlent to :func:`Window.create`
    """
    return Window.create(title, center, size, **kwargs)
