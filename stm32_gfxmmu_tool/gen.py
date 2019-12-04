import os
from mako.template import Template
import pkgutil

def gen_sources(ctx):
    files = [
        ".h", 
        ".c"
    ]
    for f in files:
        res = pkgutil.get_data(__package__, "templates/stm32_gfxmmu" + f).decode()
        template = Template(res)
        outpath = os.path.join(ctx.output, ctx.basename)
        fo = open(outpath + f, "w+")
        fo.write(template.render(ctx=ctx))
        fo.close
