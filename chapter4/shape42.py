import cairo
import math
OUTPUT_DIRECTORY = "../image_output/"
# surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 800, 700)
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
# triangle
ctx.move_to(100, 200)
ctx.line_to(280, 200)
ctx.line_to(50, 400)
ctx.close_path()
ctx.set_source_rgb(0, 0.7, 0)
ctx.fill_preserve()
ctx.stroke()


# arc
ctx.arc(155, 289, 147, 15*math.pi/4, 3*math.pi/4)
ctx.set_source_rgb(0, 0.7, 0)
ctx.fill_preserve()
ctx.stroke()


surface.write_to_png(f"{OUTPUT_DIRECTORY}shape42.png")
