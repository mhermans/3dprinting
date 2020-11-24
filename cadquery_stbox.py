import cadquery as cq


box_with = 50     # x-axis
box_depth = 50    # y-axis
box_height = 50   # z-axis
wall_with = 4

innerbox_height = box_height
innerbox_width = box_with - ( wall_with / 2)
innerbox_depth = box_depth - ( wall_with / 2)

fillet_size = box_depth / 10

# .edges("|Z") # edges that are parallel to the Z-axis

# define outer box
outbox = cq.Workplane().box(box_with, box_depth, box_height, combine = False) # (X, Y, Z)
outbox = outbox.edges("<Z").fillet(fillet_size)
#show_object(outbox)

inbox = cq.Workplane().box(innerbox_width, innerbox_depth, innerbox_height, combine = False)
inbox = inbox.edges("<Z").fillet(fillet_size)

inbox = inbox.translate( (0, 0, ( wall_with / 4) ))

box = outbox.cut(inbox)


#tab = cq.Workplane('XZ').moveTo(-20, 24).box(10, 2, 25)
tab = cq.Workplane("XY").box(10, 20, 2)
tab = tab.faces('<Z').rect(10, 20).workplane(offset=3.0).moveTo(-4,0).rect(2, 20).loft(combine=True)
tab = tab.translate( (-20, 0, 24))

show_object(tab)

#tab_slope = cq.Workplane('XZ').moveTo(-20, 22).rect(2, 4).moveTo(-20, 12).rect(2, 4).loft()
#tab = tab.move( (-2, 0) ).rect(2, 4).workplane(offset=-10).rect(2, 4).loft()

#tab = cq.Workplane().workplane(offset=26.0).rect(10, 25).workplane(offset=-10).rect(10, 25).sweep()

#tab = cq.Workplane().workplane(offset=26.0).rect(10, 25).extrude(2).edges("Z").fillet(0.5)
#tab = tab.workplane(offset=-1).rect(10, 25).workplane(offset=-10).rect(10, 25).loft()

#tab = cq.Workplane().box(10, 25, 1).translate( ( -20, 0, 24.5) )
#tab = cq.Workplane().workplane(offset=26.0).box(10, 25, 2).edges("Z").fillet(0.5)
#tab = tab.translate((0, 0, -2)).rect(10, 25).translate((-5, 0, -10)).rect(1,25,1).loft()
#tab = tab.translate( (-19, 0, 0))
#tab = cq.Workplane().workplane(offset=25.0).rect(10, 25)
#tab = tab.translate((-5, 0, -10)).rect(1,25,1).loft()
#tab = tab.translate( (-19, 0, 0))

box = box.union(tab)
#box = box.union(tab_slope)
show_object(box)

#show_object(tab )

#show_object(box)
fn = ''.join(['storebox_', str(box_with), 'x', str(box_depth), 'x', str(box_height), '.stl'])
cq.exporters.export(box , ''.join(['/home/mhermans/tmp/', fn]) )
