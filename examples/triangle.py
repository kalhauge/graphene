"""
Triangle
--------
:author: Christian Gram Kalhauge 

The purpose of this example is to draw a simple triangle.
"""

from graphene import sdl
from graphene import gl
from graphene.sdl import gl as sdl_gl
SIZE = (600, 600)

def main():
    sdl.init({'video'})

    sdl_gl.set_attribute(
        context_major_version=3,
        context_minor_version=2,
        doublebuffer=1,
        depth_size=24
    )

    window = sdl.Window.create(
        title='Hello World',
        center=(True, True), 
        size=SIZE,
        flags={'opengl', 'shown'}
    )
    
    glcontext = sdl_gl.Context.create(window)
    print(glcontext._handle)
#    renderer = sdl.Renderer.create(
#        window=window,
#        index=-1,
#        flags={'accelerated', 'targettexture'}
#    )

#   print(renderer.info())
    
    print(gl.context_info())

    running = True
    while running:
        for event in sdl.event.pending_events():
            if isinstance(event, sdl.event.Quit):
                print(event.timestamp)
                running = False
                break;
    
    glcontext.delete()
    window.destroy()
#    renderer.destroy()
    sdl.quit() 
   
if __name__ == '__main__':
    main()
