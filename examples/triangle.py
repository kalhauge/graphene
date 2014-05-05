"""
Triangle
--------
:author: Christian Gram Kalhauge 

The purpose of this example is to draw a simple triangle.
"""

from graphene import sdl
from graphene import gl

SIZE = (600, 600)


def main():
    sdl.init({'video'})

    window = sdl.Window.create(
        title='Hello World',
        center=(True, True), 
        size=SIZE,
        flags={'opengl', 'shown'}
    )
    
    renderer = sdl.Renderer.create(
        window=window,
        index=-1,
        flags={'accelerated', 'targettexture'}
    )

    print(renderer.info())
    print(gl.context_info())
    
    running = True
    while running:
        for event in sdl.event.pending_events():
            if isinstance(event, sdl.event.Quit):
                print(event.timestamp)
                running = False
                break;
    
    window.destroy()
    renderer.destroy()
    sdl.quit() 
   
if __name__ == '__main__':
    main()
