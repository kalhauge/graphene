import sdl2 as _s

from . import utils 
from .core import error
from enum import Enum

class RendererFlags(utils.Flags):
    software = _s.SDL_RENDERER_SOFTWARE
    accelerated = _s.SDL_RENDERER_ACCELERATED
    presentvsync = _s.SDL_RENDERER_PRESENTVSYNC
    targettexture = _s.SDL_RENDERER_TARGETTEXTURE


class Renderer:

    def __init__(self, handle):
        assert not handle is None
        self._handle = handle 

    @classmethod
    def create(cls, window, index=-1, flags={}):
        rhandle = _s.SDL_CreateRenderer(
            window._handle,
            index,
            RendererFlags.process(flags)
        )
        return Renderer(rhandle)

    def info(self):
        info = _s.SDL_RendererInfo()
        retval = _s.SDL_GetRendererInfo(self._handle, info)
        assert retval == 0, core.error(retval)
        return RendererInfo(info)

    def destroy(self):
        _s.SDL_DestroyRendere(self._handler)

class RendererInfo:
    
    def __init__(self, handle):
        self._handle = handle
        self.max_texture_width = handle.max_texture_width
        self.max_texture_height = handle.max_texture_height
        self.flags = RendererFlags.decode(handle.flags)
        self.name = handle.name.decode('UTF-8')
        self.texture_formats = [
            PixelFormat(handle.texture_formats[i]) 
            for i in range(handle.num_texture_formats)
        ]

    def __str__(self):
        return '\n'.join([
            "Render: {name}",
            "Flags: {flags}",
            "Texture formats: {texture_formats}",
            "Max texture width {max_texture_width}", 
            "Max texture height {max_texture_height}"
        ]).format(**vars(self))

    
        
class PixelFormat(Enum):
    unknown = _s.SDL_PIXELFORMAT_UNKNOWN
    index1lsb = _s.SDL_PIXELFORMAT_INDEX1LSB
    index1msb = _s.SDL_PIXELFORMAT_INDEX1MSB
    index4lsb = _s.SDL_PIXELFORMAT_INDEX4LSB
    index4msb = _s.SDL_PIXELFORMAT_INDEX4MSB
    index8 = _s.SDL_PIXELFORMAT_INDEX8
    rgb332 = _s.SDL_PIXELFORMAT_RGB332
    rgb444 = _s.SDL_PIXELFORMAT_RGB444
    rgb555 = _s.SDL_PIXELFORMAT_RGB555
    bgr555 = _s.SDL_PIXELFORMAT_BGR555
    argb4444 = _s.SDL_PIXELFORMAT_ARGB4444
    rgba4444 = _s.SDL_PIXELFORMAT_RGBA4444
    abgr4444 = _s.SDL_PIXELFORMAT_ABGR4444
    bgra4444 = _s.SDL_PIXELFORMAT_BGRA4444
    argb1555 = _s.SDL_PIXELFORMAT_ARGB1555
    rgba5551 = _s.SDL_PIXELFORMAT_RGBA5551
    abgr1555 = _s.SDL_PIXELFORMAT_ABGR1555
    bgra5551 = _s.SDL_PIXELFORMAT_BGRA5551
    rgb565 = _s.SDL_PIXELFORMAT_RGB565
    bgr565 = _s.SDL_PIXELFORMAT_BGR565
    rgb24 = _s.SDL_PIXELFORMAT_RGB24
    bgr24 = _s.SDL_PIXELFORMAT_BGR24
    rgb888 = _s.SDL_PIXELFORMAT_RGB888
    rgbx8888 = _s.SDL_PIXELFORMAT_RGBX8888
    bgr888 = _s.SDL_PIXELFORMAT_BGR888
    bgrx8888 = _s.SDL_PIXELFORMAT_BGRX8888
    argb8888 = _s.SDL_PIXELFORMAT_ARGB8888
    rgba8888 = _s.SDL_PIXELFORMAT_RGBA8888
    abgr8888 = _s.SDL_PIXELFORMAT_ABGR8888
    bgra8888 = _s.SDL_PIXELFORMAT_BGRA8888
    argb2101010 = _s.SDL_PIXELFORMAT_ARGB2101010
    yv12 = _s.SDL_PIXELFORMAT_YV12
    iyuv = _s.SDL_PIXELFORMAT_IYUV
    yuy2 = _s.SDL_PIXELFORMAT_YUY2
    uyvy = _s.SDL_PIXELFORMAT_UYVY
    yvyu = _s.SDL_PIXELFORMAT_YVYU
