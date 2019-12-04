from enum import Enum

BYTES_PER_BLOCK = 16

class BlockMode(Enum):
    BM192 = 192
    BM256 = 256


class ColorMode(Enum):
    RGB888 = (0, 3)
    ARGB8888 = (1, 4)
    RGB565 = (2, 2)
    ARGB1555 = (3, 2)
    ARGB4444 = (4, 2)
    L8 = (5, 1)
    AL44 = (6, 1)
    AL88 = (7, 2)

    def __init__(self, n, size,):
        self.n = n
        self.size = size

    def bytes_per_pixel(self):        
        return self.size

    @staticmethod
    def avail():
        first = True
        for name, member in ColorMode.__members__.items():
            if first:
                first = False
                s = name
            else:
                s = s + ", " + name
        return s

class Line:    
    def __init__(self, line_nr, first_visable_block, last_visable_block):
        self.line_nr = line_nr
        self.first_visable_block = first_visable_block
        self.last_visable_block = last_visable_block
        self.offset = 0

    def set_offset(self, offset):
        self.offset = offset

    def rep(self):
        print("Line: %03d: %03d -> %03d" % (self.line_nr, self.first_visable_block, self.last_visable_block))    

    def get_lreg(self):
        return "0x00%02X%02X01" % (self.last_visable_block, self.first_visable_block)

    def get_hreg(self):
        return "0x%08X" % (self.offset)

    def get_line_nr(self):
        return self.line_nr

class Context:
    def __init__(self, xsize, ysize):
        self.xsize = xsize
        self.ysize = ysize
        self.block_mode = BlockMode.BM192
        self.color_mode = ColorMode.RGB888
        self.lines = []
        self.buf_size = 0
        self.output = ""
        self.basename = "stm32_gfxmmu"

def calc_line_offsets(ctx):
    """
    Calculate the start pixel and the end pixel of a given block 
    in x direction

    Parameters:

    ctx (Context): The context containing the list of lines
    """
    block_off = 0
    for l in ctx.lines:
        offset = (block_off - l.first_visable_block) * BYTES_PER_BLOCK
        offset &= 0x3fffff
        block_off += l.last_visable_block - l.first_visable_block + 1
        l.set_offset(offset)

    ctx.buf_size = block_off * BYTES_PER_BLOCK


def pixel_of_xblock(block, color_mode):
    """
    Calculate the start pixel and the end pixel of a given block 
    in x direction

    Parameters:

    block (int): The block number
    color_mode (ColorMode): The color mode


    Returns:

    (int, int): The start and the end pix for the given block
    """
    px_start = (block * BYTES_PER_BLOCK) // color_mode.bytes_per_pixel()
    px_end = (((block + 1) * BYTES_PER_BLOCK) - 1) // color_mode.bytes_per_pixel()
    return (px_start, px_end)
