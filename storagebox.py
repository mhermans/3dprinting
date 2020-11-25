# Parametric storage boxes for parts
# ##################################

import cadquery as cq

box_with    = 50     # x-axis
box_depth   = 50    # y-axis
box_height  = 50   # z-axis
wall_with   = 1

tab_width = 25
tab_depth = 13 # 13mm is Dymo tag height
tab_height = 2

# create box
box = cq.Workplane("XY").box(box_with, box_depth, box_height)
box = box.faces(">Z").shell(- wall_with) # create shell with top Z-face open
box = box.edges('|Z').fillet(1) # fillet all edges parallel to Z-axis
box = box.edges('<Z').fillet(1) # fillet edges at bottom of Z-axis
box = box.faces("<Z[-2]").fillet(1) # fillet second to last bottom face of Z-axis (inner edges at bottom)

# create tab
tab = cq.Workplane("XY").box(tab_depth, tab_width , tab_height)
tab = tab.faces('<Z').rect(tab_depth, tab_width ).workplane(offset=12.0).moveTo(-6.4, 0).rect(0.1, tab_width).loft(combine=True)
tab = tab.translate( (-18.5, 0, 24))

box = box.union(tab)
show_object(box)

fn = ''.join(['storebox_', str(box_with), 'x', str(box_depth), 'x', str(box_height), '.stl'])
cq.exporters.export(box , ''.join(['/home/mhermans/tmp/', fn]) )