# axis pin for laptopstand
# ========================


# core cylinder for pin

core = cq.Workplane("front").circle(11.7).extrude(40)

#.rect(0.5, 0.75).extrude(0.5)


# cylinder end stop
# can use .translate( (0, 0, -5)) or .workplane(offset=-5)
stop = cq.Workplane("front").workplane(offset=-5).circle(22).extrude(5)

# cylinder top head
head = cq.Workplane("front").workplane(offset=40).circle(13).workplane(offset=3.0).circle(11.7)
head = head.loft()

pin = core.union(stop).union(head)

# pin cutout
cutout = cq.Workplane("front").rect(15 * 2, 5).extrude(45)

pin  = pin .cut(cutout)

#show_object(pin)

cq.exporters.export(pin, '/home/mhermans/tmp/laptopstand_pin.stl')