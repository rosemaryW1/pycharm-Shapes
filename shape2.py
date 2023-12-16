import cairo
OUTPUT_DIRECTORY = "image_output/"
# Define surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600,400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.move_to(50,20)
ctx.line_to(50, 100)
ctx.line_to(200, 100)
ctx.set_source_rgb(1, 0, 0)
ctx.close_path()
ctx.set_line_join(cairo.LINE_JOIN_ROUND)
ctx.set_line_width(5)
ctx.stroke()

ctx.move_to(50, 10)
ctx.line_to(200, 10)
ctx.line_to(200,90)
ctx.set_source_rgb(1, 0,0)
ctx.fill_preserve()
ctx.set_source_rgb(0, 0, 0)
ctx.close_path()
ctx.set_line_width(5)
ctx.stroke()

surface.write_to_png(f"{OUTPUT_DIRECTORY}shape2.png")
