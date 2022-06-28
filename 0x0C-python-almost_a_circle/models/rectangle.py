#!/usr/bin/python3
"""
Base Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Get width
        """
        return self.__width

    @property
    def height(self):
        """
        Get height
        """
        return self.__height

    @property
    def x(self):
        """
        Get x
        """
        return self.__x

    @property
    def y(self):
        """
        Get y
        """
        return self.__y

    @width.setter
    def width(self, new_data):
        """
        Set width
        """
        if type(new_data) is not int:
            raise TypeError("width must be an integer")
        if new_data <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_data

    @height.setter
    def height(self, new_data):
        """
        Set height
        """
        if type(new_data) is not int:
            raise TypeError("height must be an integer")
        if new_data <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_data

    @x.setter
    def x(self, new_data):
        """
        Set x
        """
        if type(new_data) is not int:
            raise TypeError("x must be an integer")
        if new_data < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_data

    @y.setter
    def y(self, new_data):
        """
        Set y
        """
        if type(new_data) is not int:
            raise TypeError("y must be an integer")
        if new_data < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_data

    def area(self):
        """
        Area of a rectangle
        """
        return(self.width * self.height)

    def display(self):
        """
        Prints the stdout with the character # taking in consideration x & y
        """
        if self.height == 0 or self.width == 0:
            print("")
            return
        for x in range(self.y):
            print("")
        for x in range(self.height):
            for y in range(self.x):
                print(" ", end="")
            for y in range(self.width):
                print("#", end="")
            print("")
        return

    def __str__(self):
        """
        Prints the rectangle details
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """
        Override instance of rectangle
        """
        if args and len(args) > 0:
            index = 0
            for arg in args:
                if index == 0:
                    if arg is None:
                        self.__init__(
                            self.width,
                            self.height,
                            self.x,
                            self.y)
                    else:
                        self.id = arg
                if index == 1:
                    self.width = arg
                if index == 2:
                    self.height = arg
                if index == 3:
                    self.x = arg
                if index == 4:
                    self.y = arg
                index += 1
        elif kwargs and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "width":
                    self.width = v
                if k == "height":
                    self.height = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v
                if k == "id":
                    if v is None:
                        self.__init__(
                            self.width,
                            self.height,
                            self.x,
                            self.y)
                    else:
                        self.id = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
