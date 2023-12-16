import cairo
import math
OUTPUT_DIRECTORY = "../image_output/"

# surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 800, 900)
ctx= cairo.Context(surface)
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

# bezierCurve
ctx.move_to(100,100)
ctx.curve_to(200,0,400,200,500,100)
ctx.line_to(400,450)
ctx.set_source_rgb(1,0,1)
ctx.set_line_width(5)
ctx.stroke()

# arc
ctx.arc(50, 690, 140, 6*math.pi/4, 2*math.pi/4)
ctx.stroke()

# line2
ctx.move_to(400,450)
ctx.line_to(50, 550)
ctx.stroke()

surface.write_to_png(f"{OUTPUT_DIRECTORY}shape43.png")