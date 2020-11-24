import cadquery as cq

# The dimensions of the model. These can be modified rather than changing the
# object's code directly.
width = 50
height = 50
thickness = 2


n_cutout = 6
cutout_radius = 2
cutout_margin = 0.5
h_sep = cutout_radius * 2 + cutout_margin

plate_width =  2 * ( ( n_cutout * cutout_radius ) + ( n_cutout * cutout_margin ) )

# Create a plate with two polygons cut through it
result = cq.Workplane("front").box(width, width, thickness)

for idx in range(n_cutout):
    #result = result.workplane(offset=1, centerOption='CenterOfBoundBox').center(10,10-idx*h_sep).circle(5).cutThruAll()
    result = result.workplane().center(0, 0-idx*h_sep).circle(cutout_radius).cutThruAll()    

# Render the solid
show_object(result)

# 50 x 50 x 2 plaat met gaatjes van 



