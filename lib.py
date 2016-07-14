from solid.utils import *  # noqa
#############
#  Library  #
#############


class Lumber(object):

    def __init__(self, width, height, length, name, price):
        # TODO might be redundant
        self.width = width
        self.height = height
        self.length = length
        self.name = name
        self.price = price

    @classmethod
    def print_name(cls):
        return "{} {}x{}x{}, {} EUR".format(
            cls.name, cls.width, cls.height, cls.length, cls.price)


class Part(object):
    color = Yellow
    flip = False

    def __init__(self):
        pass

    def render(self):
        return color(self.color)(cube([
            getattr(self.lumber, "height" if self.flip else "width"),
            getattr(self.lumber, "width" if self.flip else "height"),
            self.length]))

###############
#  Warehouse  #
# Lumber dimensions, as available from you local hardware store or lumber yard
###############


class KR8080(Lumber):
    width = 80
    height = 80
    length = 3000
    name = "Kreuzrahmen Fichte/Tanne"
    price = 8.07


class KR8050(Lumber):
    width = 80
    height = 50
    length = 3000
    name = "Kreuzrahmen Fichte/Tanne"
    price = 3.57


class BD20040(Lumber):
    width = 200
    height = 40
    length = 3000
    name = "Baudiele Fichte/Tanne"
    price = 8.07
