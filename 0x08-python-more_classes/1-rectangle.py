#!/usr/bin/python3
""" Define a Rectangle class """


class Rectangle:
    """ Represent a rectangle """
    def __init__(self, width=0, height=0):
        """ Checks the parameters and initializes some values.
        Args:
            width (:obj:int, optional): The width of the Rectangle.
            height (:obj:int, optional): The height of the Rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get the width of the Rectangle """
        return self.__width

    @width.setter
    def width(slf, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(slf):
        """ Get/set the height of the Rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
