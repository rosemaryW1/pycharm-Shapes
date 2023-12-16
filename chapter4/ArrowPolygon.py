import cairo
import math

OUTPUT_DIRECTORY = "../image_output/"

def arrow(ctx, x, y, width, height, a, b):
    ctx.move_to(x, y + b)  # 1
    ctx.line_to(x, y + height - b)  # 2
    ctx.line_to(x + a, y + height - b)  # 3
    ctx.line_to(x + a, y + height)  # 4
    ctx.line_to(x + width, y + height / 2)  # 5
    ctx.line_to(x + a, y)  # 6
    ctx.line_to(x + a, y + b)  # 7
    ctx.close_path()

"""surface"""
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

"""Drawing different  arrows"""
ctx.set_source_rgb(0, 0, 0.5)
arrow(ctx, 20,20, 150, 150, 75, 50)
ctx.fill()
arrow(ctx, 220, 20, 150, 150, 50, 30)
ctx.fill()
arrow(ctx, 420, 20, 150, 150, 25, 20)
ctx.fill()
arrow(ctx, 70, 220, 75, 150, 0, 50)
ctx.fill()
arrow(ctx, 220, 220, 150, 150, 75, 0)
ctx.fill()
arrow(ctx, 420, 270,150,50, 100, 0)
ctx.fill()




surface.write_to_png(f"{OUTPUT_DIRECTORY}ArrowPolygon.png")
