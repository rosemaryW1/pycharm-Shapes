import cairo
OUTPUT_DIRECTORY = "image_output/"
# set up pycairo
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# beizer curve
ctx.move_to(100, 100)
ctx.curve_to(200, 0, 400, 200, 500, 100)
ctx.line_to(500, 300)
ctx.curve_to(400, 400, 200, 200, 100, 300)
ctx.close_path()
ctx.set_source_rgb(1, 0, 0)
ctx.set_dash([40, 10])
ctx.set_line_width(10)
ctx.stroke()

# Save the image to a file
surface.write_to_png(f'{OUTPUT_DIRECTORY}dashedBezier.png')
