import sdl2 as _s
from enum import Enum
from .core import get_error

class Attribute(Enum):
    green_size = _s.SDL_GL_GREEN_SIZE
    blue_size = _s.SDL_GL_BLUE_SIZE
    alpha_size = _s.SDL_GL_ALPHA_SIZE
    buffer_size = _s.SDL_GL_BUFFER_SIZE
    doublebuffer = _s.SDL_GL_DOUBLEBUFFER
    depth_size = _s.SDL_GL_DEPTH_SIZE
    stencil_size = _s.SDL_GL_STENCIL_SIZE
    accum_red_size = _s.SDL_GL_ACCUM_RED_SIZE
    accum_green_size = _s.SDL_GL_ACCUM_GREEN_SIZE
    accum_blue_size = _s.SDL_GL_ACCUM_BLUE_SIZE
    accum_alpha_size = _s.SDL_GL_ACCUM_ALPHA_SIZE
    stereo = _s.SDL_GL_STEREO
    multisamplebuffers = _s.SDL_GL_MULTISAMPLEBUFFERS
    multisamplesamples = _s.SDL_GL_MULTISAMPLESAMPLES
    accelerated_visual = _s.SDL_GL_ACCELERATED_VISUAL
    retained_backing = _s.SDL_GL_RETAINED_BACKING
    context_major_version = _s.SDL_GL_CONTEXT_MAJOR_VERSION
    context_minor_version = _s.SDL_GL_CONTEXT_MINOR_VERSION
    context_flags = _s.SDL_GL_CONTEXT_FLAGS
    context_profile_mask = _s.SDL_GL_CONTEXT_PROFILE_MASK
    share_with_current_context = _s.SDL_GL_SHARE_WITH_CURRENT_CONTEXT
    framebuffer_srgb_capable = _s.SDL_GL_FRAMEBUFFER_SRGB_CAPABLE

def set_attribute(**kwargs):
    for name, value in kwargs.items():
        retval = _s.SDL_GL_SetAttribute(Attribute[name].value, value)
        assert retval == 0, error(retval)

class Context:

    def __init__(self, handle):
        assert not handle is None, get_error()
        self._handle = handle

    @classmethod
    def create(cls, window):
        handle = _s.SDL_GL_CreateContext(window._handle)
        return cls(handle)

    def destroy(self):
        self.delete()

    def delete(self):
        _s.SDL_GL_DeleteContext(self._handle)

def create_context(window):
    return Context.create()


