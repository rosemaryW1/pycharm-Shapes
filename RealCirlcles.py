import cairo
import math
OUTPUT_DIRECTORY = "image_output/"
# setting up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# small circle
ctx.arc(300, 200, 50, 0, 2*math.pi)
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(10)
ctx.stroke()

# medium circle
ctx.arc(300, 200, 100, 0, 2*math.pi)
ctx.set_source_rgb(1, 0, 1)
ctx.set_line_width(10)
ctx.stroke()

# large circle
ctx.arc(300, 200, 150, 0, 2*math.pi)
ctx.set_source_rgb(1, 1, 1)
ctx.set_line_width(10)
ctx.stroke()

surface.write_to_png(f"{OUTPUT_DIRECTORY}RealCircles.png")
