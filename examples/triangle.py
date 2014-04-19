"""
Triangle
--------
:author: Christian Gram Kalhauge 

The purpose of this example is to draw a simple triangle.
"""

from graphene import sdl

SIZE = (600, 600)

def main():
    sdl.init()

    window = sdl.Window.create(
        title='Hello World',
        center=(True, True), 
        size=SIZE,
        flags={'opengl', 'shown'}
    )
    
    renderer = sdl.Renderer.create(
        window=window,
        flags={'accelerated', 'targettexture'}
    )

    print(renderer.info())



    running = True
    while running:
        event = sdl.poll_event()
        if isinstance(event, sdl.event.Quit):
            print(event.timestamp)
            break;
    
    window.destroy()
    renderer.destroy()
    sdl.quit() 
   
if __name__ == '__main__':
    main()
