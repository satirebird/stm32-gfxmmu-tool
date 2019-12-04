from stm32_gfxmmu_tool.gfxmmu import *


def shape_round(ctx):    
    """
    Calculate the line definitions for a round shape display with the given
    diameter (px_size)

    Parameters:

    ctx (Context): The display context with the display parameters

    Returns:

    [Line]: A list of lines
    """
    r = ctx.xsize // 2
    r2 = r * r
    l = 0

    result_list = []

    for l in range(0, ctx.xsize):
        find_first = True
        for b in range(0, ctx.block_mode.value):
            # Calculate the start end the ed pixel for the block
            (ps, pe) = pixel_of_xblock(b, ctx.color_mode)
            # Calculate the tx, ty vector relative to the center of the circle
            tx = pe - r
            if pe > r:
                tx = ps - r
            ty = r - l - 1
            if l >= r:
                ty = r - l
            vis = False
            if ((tx * tx) + (ty * ty)) <= r2:
                vis = True
            
            # Check if the block is visable
            if find_first:
                if vis:
                    first = b
                    find_first = False
            else:
                if not vis:
                    last = b - 1
                    break
        ln = Line(l, first, last)
        result_list.append(ln)
    return result_list