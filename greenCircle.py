import cairo
import math
OUTPUT_DIRECTORY = "image_output/"

# Set up pycairo and the canvas
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 400, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.set_line_width(8)
ctx.set_source_rgb(0, 0, 0)

ctx.arc(200, 200, 120, 0, 2 * math.pi)

ctx.fill()
ctx.set_source_rgb(0, 1, 0)
ctx.move_to(80, 200)
ctx.arc(200, 200, 120, 0, math.pi / 2)
ctx.line_to(200, 320)
ctx.line_to(200, 80)
ctx.set_miter_limit(2)
ctx.set_line_join(cairo.LINE_JOIN_ROUND)

ctx.stroke()
surface.write_to_png(f"{OUTPUT_DIRECTORY}green_circle.png")
