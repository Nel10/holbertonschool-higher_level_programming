#!/usr/bin/python3
"""
Created base class
"""
from models.base import Base


class Rectangle(Base):
    """Define Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """iniciatialize"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
