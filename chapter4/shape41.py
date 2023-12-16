import cairo
OUTPUT_DIRECTORY = "../image_output/"
# surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 800, 700)
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
for x in range(0, 900, spacing):
    ctx.move_to(x, 0)
    ctx.line_to(x, 850)
    ctx.stroke()

# polygon
ctx.move_to(80, 70)
ctx.line_to(100, 150)
ctx.line_to(50, 200)
ctx.line_to(170, 350)
ctx.line_to(400, 200)
ctx.line_to(400, 50)
ctx.close_path()
ctx.set_source_rgb(0.5, 0.5, 1)
ctx.fill_preserve()
ctx.stroke()

surface.write_to_png(f"{OUTPUT_DIRECTORY}shape41.png")
