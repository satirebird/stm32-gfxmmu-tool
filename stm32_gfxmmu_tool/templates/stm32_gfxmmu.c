/* 
 * DO NOT EDIT. This file is generated
 * 
 * The following tabel contains the data for the GFXMMU lookup table.
 */

#include "${ctx.output}.h"

static const uint32_t stm32_gfxmmu_lut[STM32_GFXMMU_LUT_LENGTH] = {
% for l in ctx.lines:
    ${l.get_lreg()}, // GFXMMU_LUT${l.get_line_nr()}L
    ${l.get_hreg()}, // GFXMMU_LUT${l.get_line_nr()}H
% endfor
};

const uint32_t *stm32_gfxmmu_get_lut(void)
{
    return stm32_gfxmmu_lut;
}
