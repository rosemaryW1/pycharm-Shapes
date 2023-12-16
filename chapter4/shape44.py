import cairo

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

# triangle 1
ctx.move_to(150, 50)
ctx.line_to(300, 50)
ctx.line_to(200, 150)
ctx.close_path()
ctx.set_source_rgb(0.8, 0, 0.8)
ctx.fill_preserve()
ctx.stroke()

# triangle 2
ctx.move_to(200, 150)
ctx.line_to(170, 200)
ctx.line_to(220, 200)
ctx.close_path()
ctx.set_source_rgb(0.8, 0, 0.8)
ctx.fill_preserve()
ctx.stroke()

# triangle 3
ctx.move_to(220, 200)
ctx.line_to(290, 200)
ctx.line_to(250, 250)
ctx.close_path()
ctx.set_source_rgb(0.8, 0, 0.8)
ctx.fill_preserve()
ctx.stroke()

# triangle 4
ctx.move_to(250, 250)
ctx.line_to(100, 350)
ctx.line_to(300, 350)
ctx.close_path()
ctx.set_source_rgb(0.8, 0, 0.8)
ctx.fill_preserve()
ctx.stroke()
# save image

surface.write_to_png(f"{OUTPUT_DIRECTORY}shape44.png")
