import cairo
import math
OUTPUT_DIRECTORY = "../image_output/"
# surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 800, 900)
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
for x in range(0, 800, spacing):
    ctx.move_to(x, 0)
    ctx.line_to(x, 850)
    ctx.stroke()

# rectangle1
ctx.rectangle(50, 100, 250, 450)
ctx.set_source_rgb(1, 0.5, 0)
ctx.fill_preserve()
ctx.stroke()


# curve 1
ctx.arc(176, 408, 140, 4*math.pi/4, 0*math.pi/4)
ctx.set_source_rgb(1, 1, 1)
ctx.set_line_width(20)
ctx.stroke()

# curve 2

# save image
surface.write_to_png(f"{OUTPUT_DIRECTORY}shape45.png")
