"""Class: Triangle

Author: Cade Breslow
Version: 10/14/2024
"""


class Triangle:
    __v1 = None
    __v2 = None
    __v3 = None

    def __init__(self, v1, v2, v3):
        self.__v1 = v1
        self.__v2 = v2
        self.__v3 = v3
    
    def getV1(self):
        return self.__v1
    
    def getV2(self):
        return self.__v2
    
    def getV3(self):
        return self.__v3