import cairo
OUTPUT_DIRECTORY = "image_output/"
# set up pycairo
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# set line color and width
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(5)

# 1
ctx.move_to(100, 50)
ctx.line_to(500, 50)
ctx.set_dash([20])
ctx.stroke()

# 2
ctx.move_to(100, 100)
ctx.line_to(500, 100)
ctx.set_dash([20, 10])
ctx.stroke()

# 3
ctx.move_to(100, 150)
ctx.line_to(500, 150)
ctx.set_dash([20, 5, 5, 5])
ctx.stroke()

# 4
ctx.move_to(100, 200)
ctx.line_to(500, 200)
ctx.set_dash([5, 5, 10])
ctx.stroke()

ctx.set_line_width(10)
ctx.set_line_cap(cairo.LINE_CAP_ROUND)

# 5
ctx.move_to(100, 250)
ctx.line_to(500, 250)
ctx.set_dash([10, 20])
ctx.stroke()

# 6
ctx.move_to(100, 300)
ctx.line_to(500, 300)
ctx.set_dash([0, 20])
ctx.stroke()

# Save the image to a file
surface.write_to_png(f'{OUTPUT_DIRECTORY}dashline.png')

