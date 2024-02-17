from ocp_vscode import show, show_object, reset_show, set_port, set_defaults, get_defaults
set_port(3939)
from build123d import *


pts = [
    (13, 0),
    (13,10),
    ( 9,10),
    ( 9, 8),
    ( 7, 8),
    ( 7,12),
    (22,27),
    (22,35),
    (24,35),
    (24,27),
    (15,18),
    (15, 0)
]

with BuildPart() as funnel:
    with BuildSketch(Plane.XZ) as ex23_sk:
        with BuildLine() as ex23_ln:
            l1 = Polyline(*pts)
            l2 = Line(l1 @ 1, l1 @ 0)
        make_face()
    revolve(axis=Axis.Z, revolution_arc=360)
    edges = funnel.edges().filter_by_position(Axis.Z, minimum=12, maximum=27)
    fillet(edges[:2], radius=3)
    fillet(edges[-2:], radius=5)

show_object(funnel)

funnel.part.export_step("funnel.step")