"""
This example should show the minimal code required to draw a triangle.
"""

from graphene import sdl
from graphene import gl

from time import sleep

sdl.init({'video'})

window = sdl.Window.create('Hello World', flags={'opengl'})
renderer = sdl.Renderer.create(window, flags={'accelerated'})

while not isinstance(sdl.poll_event(), sdl.event.Quit):
    # Do NOT do this in real life.
    pass

renderer.destroy()
window.destroy()
sdl.quit()
