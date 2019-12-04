import sys
import argparse

from stm32_gfxmmu_tool.gfxmmu import *
from stm32_gfxmmu_tool.shape_round import *
from stm32_gfxmmu_tool.gen import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument( "xsize", type=int, help="number of pixel in x direction")
    parser.add_argument( "ysize", type=int, help="number of pixel in y direction")

    parser.add_argument("-s", "--shape", help="the shape of the display (round)")
    parser.add_argument("-o", "--output", help="output file prefix, defaults to 'stm32_gfxmmu'")
    parser.add_argument("-c", "--color", help="color mode (" + ColorMode.avail() + ") default: 'RGB888'")
    parser.add_argument("-b", "--bmode", help="block mode, either 192 (default) or 256")

    args = parser.parse_args()

    ctx = Context(args.xsize, args.ysize)

    if args.output:
        ctx.output = args.output

    if args.color:
        found = False
        for name, member in ColorMode.__members__.items():
            if name == args.color:
                found = True
                ctx.color_mode = member
                break
        if not found:
            print("Unknown color mode\n", file=sys.stderr)
            parser.print_help(sys.stderr)
            sys.exit(2)

    if args.bmode:
        if args.bmode == "192":
            ctx.block_mode = BlockMode.BM192
        elif args.bmode == "256":
            ctx.block_mode = BlockMode.BM256
        else:
            print("Unknown block mode\n", file=sys.stderr)
            parser.print_help(sys.stderr)
            sys.exit(2)

    shape = "round"
    if args.shape:
        shape = args.shape

    if shape == "round":
        if ctx.xsize != ctx.ysize:
            print("xsize and ysize must be equal for round display shapes", file=sys.stderr)
            sys.exit(2)
        ctx.lines = shape_round(ctx)
    else:
        print("Unknown shape\n", file=sys.stderr)
        parser.print_help(sys.stderr)
        sys.exit(2)

    calc_line_offsets(ctx)
    gen_sources(ctx)

if __name__ == "__main__":
    main()