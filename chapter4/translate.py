import cairo
OUTPUT_DIRECTORY = "../image_output"
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 600)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.set_source_rgb(0, 0, 0)
ctx.translate(200, 300)
ctx.rectangle(-100, -100, 200, 200)
ctx.fill()

ctx.set_source_rgb(0, 0, 0)
ctx.translate(200, 100)
ctx.rectangle(-100, -100, 200, 200)
ctx.fill()

surface.write_to_png(f"{OUTPUT_DIRECTORY}translate.png")
