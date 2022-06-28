#!/usr/bin/python3
"""
Base Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Prints the square details
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        """
        Get size
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Set size
        """
        self.width = size
        self.height = size

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
                            self.size,
                            self.x,
                            self.y)
                    else:
                        self.id = arg
                if index == 1:
                    self.size = arg
                if index == 2:
                    self.x = arg
                if index == 3:
                    self.y = arg
                index += 1
        elif kwargs and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "size":
                    self.size = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v
                if k == "id":
                    if v is None:
                        self.__init__(
                            self.size,
                            self.x,
                            self.y)
                    else:
                        self.id = v

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
