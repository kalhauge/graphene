import sdl2

class Surface:

    def __init__(self, handle):
        assert not handle is None
        self._handle = handle

    @classmethod
    def load(cls, filename):
        if filename.lower().endswith('.bmp'):
            handle = sdl2.SDL_LoadBMP(filename.encode('ascii'))
            return cls(handle)


def blit(src, src_rect, dist, dist_rect):
    succ = sdl2.SDL_BlitSurface(
        src._handle, src_rect._handle if src_rect else None, 
        dist._handle, dist_rect._handle if dist_rect else None
    ) 
    assert succ == 0
