"""
.. currentmodule:: graphene.gl.program

"""


class Program:

    def __init__(self, vertex_shader, fragment_shader):
        self.vertex_shader = vertex_shader
        self.fragment_shader = fragment_shader

        
