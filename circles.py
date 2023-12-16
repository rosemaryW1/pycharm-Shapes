import cairo
import math
OUTPUT_DIRECTORY = "image_output/"

# set up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Draw an arc
ctx.arc(300, 200, 150, 0, math.pi/2)
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(10)
ctx.stroke()

surface.write_to_png(f"{OUTPUT_DIRECTORY}circles.png")
