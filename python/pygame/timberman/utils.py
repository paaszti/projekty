from static import slice_wood, slice_wood_origin

def scale_to(objects: list, old, new, change_pos=True):
    for obj in objects:
        obj.scale(old, new, change_pos)

def bring_back_slice_wood():
    slice_wood.x = slice_wood_origin.x
    slice_wood.y = slice_wood_origin.y