import cadquery as cq


box_with = 117     # x-axis
box_depth = 50    # y-axis
box_height = 47   # z-axis
wall_with = 4

innerbox_height = box_height
innerbox_width = box_with - ( wall_with / 2)
innerbox_depth = box_depth - ( wall_with / 2)

fillet_size = box_depth / 10

# .edges("|Z") # edges that are parallel to the Z-axis

# define outer box
outbox = cq.Workplane().box(box_with, box_depth, box_height, combine = False) # (X, Y, Z)
outbox = outbox.edges("<Z").fillet(fillet_size )
#show_object(outbox)

inbox = cq.Workplane().box(innerbox_width, innerbox_depth, innerbox_height, combine = False)
inbox = inbox.edges("<Z").fillet(fillet_size )

inbox = inbox.translate( (0, 0, ( wall_with / 4) ))

box = outbox.cut(inbox)
show_object(box)
fn = ''.join(['storebox_', str(box_with), 'x', str(box_depth), 'x', str(box_height), '.stl'])
cq.exporters.export(box , ''.join(['/home/mhermans/tmp/', fn]) )