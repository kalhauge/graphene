"""
The context is used to query the state of the opengl
engine
"""

import OpenGL

from OpenGL.GL import *

class ContextInfo:
  
    def __init__(self):
        self.vendor = glGetString(GL_VENDOR).decode('ascii')
        self.renderer = glGetString(GL_RENDERER).decode('ascii')
        self.version = glGetString(GL_VERSION).decode('ascii')
        self.shading_language_version = glGetString(GL_SHADING_LANGUAGE_VERSION).decode('ascii')
        self.extensions = set(glGetString(GL_EXTENSIONS).decode('ascii').split())
        self.major_version = glGetInteger(GL_MAJOR_VERSION)
        self.minor_version = glGetInteger(GL_MINOR_VERSION)

    def __str__(self):
        return "\n".join([
            'OpenGL {major_version}.{minor_version} Context Info:', 
            'Vendor: {vendor}',
            'Renderer: {renderer}', 
            'Version: {version}',
            'Shader Version: {shading_language_version}',
            'Extensions: {extensions}'
            ]).format(**vars(self))
    

def context_info():
    """ Wrapper around context """
    return ContextInfo()

