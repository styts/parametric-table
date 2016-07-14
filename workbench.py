from solid import *  # noqa
from lib import *  # noqa
from bom import print_bom

TABLE_HEIGHT = 790
TABLE_WIDTH = 1600
OFFSET_X = 50  # spacing between legs and surface edges


###########
#  Parts  #
###########


class Surface(Part):
    lumber = BD20040
    boards = 4
    length = TABLE_WIDTH
    height = lumber.width * boards

    def render(self):
        return left(OFFSET_X)(back(Leg.spacing_y)(up(Leg.length)(
            cube([Surface.length, Surface.height, Surface.lumber.height]))))


class Leg(Part):
    lumber = KR8080
    flip = True
    color = Green
    length = TABLE_HEIGHT - Surface.lumber.height
    spacing_x = Surface.length - lumber.width - 100
    spacing_y = (Surface.height - lumber.height) / 2


class Support(Part):
    lumber = KR8050
    count = 4
    offset = (Surface.length - lumber.height - OFFSET_X * 2) / (count - 1)
    color = Red
    length = Surface.height - 2 * Leg.lumber.height

    def render(self):
        return (forward(Support.length/2 + Leg.lumber.width/2)(
            up(Leg.length)(rotate([90, 90, 0])(
                super(Support, self).render()))))


class SideSupport(Part):
    lumber = KR8050
    color = Cyan
    length = TABLE_WIDTH - 2 * Leg.lumber.height - OFFSET_X * 2

    def render(self):
        return right(Leg.lumber.height)(up(Leg.length)(rot_z_to_x(
            super(SideSupport, self).render())))


leg = Leg().render()
legs = forward(Leg.spacing_y)(leg) + back(Leg.spacing_y)(leg) + \
    forward(Leg.spacing_y)(right(Leg.spacing_x)(leg)) + \
    back(Leg.spacing_y)(right(Leg.spacing_x)(leg))


def supports():
    # surface
    results = []
    support = Support().render()
    for i in xrange(Support.count):
        results.append(right(i * Support.offset)(support))

    # side
    side_support = SideSupport().render()
    results.append(forward(Support.length / 2 + 40)(side_support))
    results.append(back(Support.length / 2 + 10)(side_support))

    return (results)


# ######## -----------


bom_items = [
    (4, Leg),
    (2, SideSupport),
    (Support.count, Support),
    (Surface.boards, Surface)
]
"""
buying = {
    "KR8080": 1,
    "KR8050": 2,
    "BD20040": 4,
}
print_bom(bom_items, buying)
"""
print_bom(bom_items)
world = legs + Surface().render() + supports()
print(scad_render(world))
