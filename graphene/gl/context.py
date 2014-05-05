"""
The context is used to query the state of the opengl
engine
"""

import re

import OpenGL
from OpenGL.GL import *

class ContextInfo:

    instance = None

    @staticmethod
    def get():
        """ Get a buffered version of the Context info or create it."""
        if ContextInfo.instance is None:
            ContextInfo.instance = ContextInfo()
        return ContextInfo.instance
  
    def __init__(self):
        self.vendor = glGetString(GL_VENDOR).decode('ascii')
        self.renderer = glGetString(GL_RENDERER).decode('ascii')
        self.version = glGetString(GL_VERSION).decode('ascii')
        self.shading_language_version = glGetString(GL_SHADING_LANGUAGE_VERSION).decode('ascii')
        self.extensions = set(glGetString(GL_EXTENSIONS).decode('ascii').split())
        try:
            self.major_version = glGetInteger(GL_MAJOR_VERSION)
            self.minor_version = glGetInteger(GL_MINOR_VERSION)
        except KeyError as e:
            # Problem in some versions of gl, major and minor, does not exists
            major, minor = re.match(r'(\d+).(\d+)', self.version).groups()
            self.minor_version = int(minor)
            self.major_version = int(major) 

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
    return ContextInfo.get()

