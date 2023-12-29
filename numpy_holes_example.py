import numpy as np
import cadquery as cq

y_sh = np.array([14.5,15,15,14.5,29.5,62.3,70,70,119,119,125,125,129.8,131.8,132,132]) - 100./2.
z_sh = np.array([22.5,39.5,89.5,107.5,15.9,122.5,22.5,107.5,22.5,107.5,39.5,89.5,140.,15.9,108,126]) - 150./2.
dsh = np.array([7,5,7,7,5,5,7,7,7,7,7,7,5,5,5,5]) 

cq_object = cq.Workplane('XY').box(5, 200, 150)

for dh in np.unique(dsh):
    ysh = y_sh[dsh==dh]
    zsh = z_sh[dsh==dh]
    yzsh = [(y,z) for y,z in zip(ysh.flatten(), zsh.flatten())]
    print('dh, ysh, zsh = ', dh, ysh, zsh)
    print('yzsh = ', yzsh)
    cq_object = cq_object.faces('<X').workplane().pushPoints(yzsh).hole(dh)
    
show_object(cq_object)