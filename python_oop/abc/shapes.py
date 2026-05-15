#!/usr/bin/env python3
"""Defines a Circle class."""
import math
from shape import Shape   # ou BaseGeometry selon ton projet


class Circle(Shape):
    """Represents a circle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (abs(self.radius) ** 2)

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * abs(self.radius)


class Circle(Shape):
    """Classe représentant un cercle."""

    def __init__(self, radius):
        """Initialise un cercle avec son rayon.

        Args:
            radius: Le rayon du cercle.
        """
        self.radius = radius

    def area(self):
        """Retourne l'aire du cercle."""
        return math.pi * self.radius ** 2
        
def perimeter(self):
    return 2 * math.pi * abs(self.radius)



class Rectangle(Shape):
    """Classe représentant un rectangle."""

    def __init__(self, width, height):
        """Initialise un rectangle avec sa largeur et sa hauteur.

        Args:
            width: La largeur du rectangle.
            height: La hauteur du rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Retourne l'aire du rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Retourne le périmètre du rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Affiche l'aire et le périmètre d'une forme.

    Cette fonction utilise le duck typing : elle ne vérifie pas le type
    de l'objet, elle appelle simplement les méthodes attendues.

    Args:
        shape: Tout objet qui possède les méthodes area() et perimeter().
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
