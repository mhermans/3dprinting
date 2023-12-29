# Parametric storage boxes for parts
# ##################################

import cadquery as cq

box_with    = 100     # x-axis
box_depth   = 100    # y-axis
box_height  = 75     # z-axis
wall_with   = 1

tab_width = box_depth/2 # default tag along half the wall
tab_depth = 13 # 13mm is Dymo tag height
tab_height = 2
tab_slope_depth = 12

# create box
# ----------
box = cq.Workplane("XY").box(box_with, box_depth, box_height)
box = box.faces(">Z").shell(- wall_with) # create shell with top Z-face open
box = box.edges('|Z').fillet(1) # fillet all edges parallel to Z-axis
box = box.edges('<Z').fillet(1) # fillet edges at bottom of Z-axis
box = box.faces("<Z[-2]").fillet(1) # fillet second to last bottom face of Z-axis (inner edges at bottom)

# create tab
# ----------
tab = cq.Workplane("XY").box(tab_depth, tab_width , tab_height)

# tab slope (suffciently sloping to avoid supports)
tab = tab.faces('<Z').rect(tab_depth, tab_width) # start top of slope on bottom face of tab

# draw end rectangle of slope lower and sloping towards the wall of the box
tab = tab.workplane(offset = tab_slope_depth).moveTo(-(tab_depth/2), 0).rect(0.1, tab_width)
tab = tab.loft(combine=True) # loft between two rectangles, creating slope for tab

# move tab & slope against wall
tab_align_top = (box_height / 2) - (tab_height / 2)
tab_align_wall = (box_with / 2) - (tab_depth / 2) - wall_with
tab = tab.translate( (-tab_align_wall, 0, tab_align_top) )

box = box.union(tab)
show_object(box)

fn = ''.join(['storagebox_', str(box_with), 'x', str(box_depth), 'x', str(box_height), '.stl'])
cq.exporters.export(box , ''.join(['/home/mhermans/projects/learning_3d/storagebox/', fn]) )