from ocp_vscode import show, show_object, reset_show, set_port, set_defaults, get_defaults
set_port(3939)
from build123d import *

# custom parameters

outer_dia = 26.0
inner_dia = 18.0
inner_height = 2.0
outer_height = 10.0
wall_th = 1.6
top_dia = 44.0
top_height = 8.0
top_radius = 5
bottom_radius = 3

# dependend params

x1 = inner_dia/2 - wall_th
x2 = inner_dia/2
x3 = outer_dia/2
x4 = x3 + wall_th
x5 = top_dia/2
x6 = x5 + wall_th

y1 = 0
y2 = outer_height
y3 = outer_height - inner_height
y4 = outer_height + inner_height
y5 = y4 + (x5 - x1)
y6 = y5 + top_height
y7 = y5 - (x6 - x4)

pts = [
    (x3, y1), #  1
    (x3, y2), #  2
    (x2, y2), #  3
    (x2, y3), #  4
    (x1, y3), #  5
    (x1, y4), #  6
    (x5, y5), #  7
    (x5, y6), #  8
    (x6, y6), #  9
    (x6, y5), # 10
    (x4, y7), # 11
    (x4, y1), # 12
]

with BuildPart() as funnel:
    with BuildSketch(Plane.XZ) as ex23_sk:
        with BuildLine() as ex23_ln:
            l1 = Polyline(*pts)
            l2 = Line(l1 @ 1, l1 @ 0)
        make_face()
    revolve(axis=Axis.Z, revolution_arc=360)
    edges = funnel.edges().filter_by_position(Axis.Z, minimum=12, maximum=27)
    fillet(edges[-2:], radius=top_radius)
    fillet(edges[:2], radius=bottom_radius)

show_object(funnel)

funnel.part.export_step("funnel.step")