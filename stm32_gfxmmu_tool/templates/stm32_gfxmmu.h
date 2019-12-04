/* 
 * DO NOT EDIT. This file is generated.
 */
#ifndef __STM32_GFXMMU_H
#define __STM32_GFXMMU_H

#ifdef __cplusplus
 extern "C" {
#endif

#include <stdint.h>

#define STM32_GFXMMU_LCD_SIZE    (${len(ctx.lines)})
#define STM32_GFXMMU_LUT_LENGTH  (2 * ${len(ctx.lines)})
#define STM32_GFXMMU_BUFFER_SIZE (${ctx.buf_size})
#define STM32_GFXMMU_BYTE_PER_PIXEL (${ctx.color_mode.bytes_per_pixel()})
#define STM32_GFXMMU_BLOCK_MODE GFXMMU_${ctx.block_mode.value}BLOCKS

#define VIRTUAL_BUFFER_WIDTH    (${ctx.block_mode.value} * 16 / STM32_GFXMMU_BYTE_PER_PIXEL)
#define VIRTUAL_BUFFER_HEIGHT   (${len(ctx.lines)})

#define STM32_GFXMMU_PIXEL_FORMAT LTDC_PIXEL_FORMAT_${ctx.color_mode.name}


const uint32_t *stm32_gfxmmu_get_lut(void);

#ifdef __cplusplus
}
#endif

#endif //__STM32_GFXMMU_H
