import cairo
OUTPUT_DIRECTORY = "image_output/"
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 400, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.move_to(200, 50)
ctx.line_to(200, 300)
ctx.set_line_width(10)
ctx.set_source_rgb(0, 1, 0)
ctx.stroke()

ctx.move_to(50,180)
ctx.line_to(350,180)
ctx.set_line_width(10)
ctx.set_source_rgb(0, 1, 0)
ctx.stroke()


surface.write_to_png(f"{OUTPUT_DIRECTORY}shape31.png")
