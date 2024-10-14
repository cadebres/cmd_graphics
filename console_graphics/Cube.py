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

    def makeCube(self):
        v1 = Vertex.Vertex(-1, -1, -1)
        v2 = Vertex.Vertex(-1, -1, 1)
        v3 = Vertex.Vertex(1, 1, -1)
        self.__triangles.append(Triangle.Triangle(v1, v2, v3))