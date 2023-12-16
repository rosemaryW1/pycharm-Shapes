import cairo
OUTPUT_DIRECTORY = "image_output/"

# Define surface

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.move_to(50, 200)
ctx.line_to(100, 300)
ctx.set_source_rgb(1, 0, 0)
ctx.stroke()

ctx.move_to(50, 200)
# ctx.curve_to(200, 50, 50, 450, 200, 200)
ctx.curve_to(200, 100, 400, 300, 500, 200)
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(5)
ctx.stroke()

ctx.move_to(350, 120)
ctx.line_to(500, 200)
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(2.0)
ctx.stroke()

surface.write_to_png(f"{OUTPUT_DIRECTORY}shape1.png")
