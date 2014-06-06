"""
Triangle
--------
:author: Christian Gram Kalhauge 

The purpose of this example is to draw a simple triangle.
"""

from graphene import sdl
from graphene import gl

import numpy as np

SIZE = (600, 600)

POS = np.array([
    0, 0.75,
    -0.75, 0.5,
    -0.75, 0.5,
]).reshape([3,2])

COLORS = np.array([
    0,   0.5, 0.5,
    0.5, 0,   0.5,
    0.5, 0.5, 0,
]).reshape([3,3])

vs = gl.Shader("""



""")

fs = gl.Shader("""



""")

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
    
    triangle = gl.VertexArray(postion=POS, color=COLORS)
    program = gl.Program(vertex=vs, fragment=fs)

    running = True
    while running:
        program.draw(triangle, gl.SCREEN)
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
