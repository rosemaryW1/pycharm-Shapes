
import cairo
OUTPUT_DIRECTORY = "image_output/"
# set up surface

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Draw the image
ctx.rectangle(150, 100, 100, 240)
ctx.set_source_rgb(1, 0, 0)
ctx.fill()

ctx.rectangle(300, 100, 100, 240)
ctx.set_source_rgb(1.5, 0.5, 1.5)
ctx.set_line_width(5)
ctx.stroke()

ctx.rectangle(450, 100, 100, 100)
ctx.set_source_rgb(1, 1, 0)
ctx.fill_preserve()
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(10)
ctx.stroke()

surface.write_to_png(f"{OUTPUT_DIRECTORY}example.png")  # Output to PNG
