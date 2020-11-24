import cadquery as cq

plate_width = 10
plate_height = 10
plate_thickness = 1

cut_radius = 1
cut_diameter = 2 * cut_radius
cut_margin = 0.5

startpoint = (plate_width / 2) - cut_margin - cut_radius

r = cq.Workplane()
r = r.box(plate_width , plate_height , plate_thickness )

#r = r.center(-startpoint, -startpoint).circle(1).cutThruAll()

for idx in range(3):
    r = result.workplane().center(-startpoint, (-startpoint - idx * h_sep).circle(cutout_radius).cutThruAll()