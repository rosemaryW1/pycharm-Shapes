import cairo
import math
OUTPUT_DIRECTORY = "../image_output/"

"""set up surface"""
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# grid
# Set background color
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

# Set grid line color and width
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(1)

# Define the grid spacing
spacing = 50

# Draw horizontal grid lines
for y in range(0, 900, spacing):
    ctx.move_to(0, y)
    ctx.line_to(900, y)
    ctx.stroke()

# Draw vertical grid lines
for x in range(0, 700, spacing):
    ctx.move_to(x, 0)
    ctx.line_to(x, 850)
ctx.stroke()

ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(10)

"""Relative Drawing Function"""
a = 0.523599
r = 200
ctx.move_to(300, 200)
ctx.rel_line_to(r*math.cos(a), r*math.sin(a))
ctx.stroke()

surface.write_to_png(f"{OUTPUT_DIRECTORY}RelativeDrawing.png")
