import cadquery as cq
clip = cq.Workplane('XY').box(20, 20, 40).faces('|Y or <Z').shell(2)
path = cq.Workplane("XZ").spline([(22, 1), (40, 13)])
clip = clip.faces('>X').workplane().circle(3.5).sweep(path).faces('>X').sphere(4)
cq.exporters.export(clip , '/home/mhermans/tmp/cliphook.stl')