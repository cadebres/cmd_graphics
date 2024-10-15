"""Class: Cube

Author: Cade Breslow
Verison: 10/14/2024
"""

import Vertex
import Triangle


class Cube:
    __triangles = []
    
    def __init__(self):
        self.makeCube()

    def __init__(self, triangles):
        for triangle in triangles:
            self.__triangles.append(triangle)

    def makeCube(self, value):
        v0 = Vertex.Vertex(value, value, value)
        v1 = Vertex.Vertex(-value, value, value)
        v2 = Vertex.Vertex(value, value, -value)
        v3 = Vertex.Vertex(-value, value, -value)
        v4 = Vertex.Vertex(value, -value, value)
        v5 = Vertex.Vertex(-value, -value, value)
        v6 = Vertex.Vertex(value, -value, -value)
        v7 = Vertex.Vertex(-value, -value, -value)
        self.__triangles.append(Triangle.Triangle(v0, v2, v3))
        self.__triangles.append(Triangle.Triangle(v0, v1, v3))
        self.__triangles.append(Triangle.Triangle(v0, v2, v3))
        self.__triangles.append(Triangle.Triangle(v0, v2, v3))
        self.__triangles.append(Triangle.Triangle(v0, v2, v3))
        self.__triangles.append(Triangle.Triangle(v0, v2, v3)) # TODO
        self.__triangles.append(Triangle.Triangle(v0, v2, v3))
        self.__triangles.append(Triangle.Triangle(v0, v2, v3))
        self.__triangles.append(Triangle.Triangle(v0, v2, v3))
        self.__triangles.append(Triangle.Triangle(v0, v2, v3))
        self.__triangles.append(Triangle.Triangle(v0, v2, v3))
        self.__triangles.append(Triangle.Triangle(v0, v2, v3))
