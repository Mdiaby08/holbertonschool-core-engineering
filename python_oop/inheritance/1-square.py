#!/usr/bin/env python3
"""Defines a Square class that inherits from Rectangle."""
Rectangle = __import__('rectangle').Rectangle


class Square(Rectangle):
    """Represents a square using Rectangle."""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
