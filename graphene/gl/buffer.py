"""

.. currentmodule:: graphene.gl.buffer

Controlls the different buffers of the system.

* Framebuffers
* Renderbuffers
* Vectorbuffers

"""
import OpenGL
from OpenGL.GL import *

class BufferType(Enum):
    array = GL_ARRAY_BUFFER
    copy_read = GL_COPY_READ_BUFFER 
    copy_write = GL_COPY_WRITE_BUFFER
    element_array = GL_ELEMENT_ARRAY_BUFFER 
    pixel_pack = GL_PIXEL_PACK_BUFFER 
    pixel_unpack = GL_PIXEL_UNPACK_BUFFER
    texture = GL_TEXTURE_BUFFER 
    transform_feedback = GL_TRANSFORM_FEEDBACK_BUFFER
    uniform = GL_UNIFORM_BUFFER

class Frequency(Enum):
    stream = 0
    static = 1
    dynamic = 2

class Nature(Enum):
    draw = 0
    read = 1
    copy = 2

access = {
    (Frequency.stream, Nature.draw) = GL_STREAM_DRAW
    (Frequency.stream, Nature.read) = GL_STREAM_READ
    (Frequency.stream, Nature.copy) = GL_STREAM_COPY
    (Frequency.static, Nature.draw) = GL_STATIC_DRAW
    (Frequency.static, Nature.read) = GL_STATIC_READ
    (Frequency.static, Nature.copy) = GL_STATIC_COPY
    (Frequency.dynamic, Nature.draw) = GL_DYNAMIC_DRAW
    (Frequency.dynamic, Nature.read) = GL_DYNAMIC_READ
    (Frequency.dynamic, Nature.copy) = GL_DYNAMIC_COPY
}


class Buffer:

    def __init__(self, handle):
        self.handle = handle

    def data(self, buffer_type, data, usage):


class ArrayBuffer: 
    buffer_type = BufferType.array

    def data(self, data, usage):
        Buffer.data(self, self.buffer_type, data, usage)
        
         

