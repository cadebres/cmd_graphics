"""Class: Vertex

Author: Cade Breslow
Version: 10/14/2024
"""


class Vertex:
    __x = 0
    __y = 0
    __z = 0

    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y