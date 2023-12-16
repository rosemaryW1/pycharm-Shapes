import cairo
import math
OUTPUT_DIRECTORY = "image_output/"

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 900, 1000)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.arc(250,250,150,0,2*math.pi)
ctx.set_source_rgb(0,0,0)
ctx.set_source_rgb(0,0,0)
ctx.fill_preserve()
ctx.set_line_width(10)
ctx.stroke()

# arc
ctx.arc(250,250,150,0,math.pi/2)
ctx.set_source_rgb(0,1,0)
ctx.set_line_width(20)
ctx.set_line_cap(cairo.LINE_CAP_ROUND)
ctx.stroke()

# crossing lines
ctx.set_source_rgb(0,1,0)
ctx.set_line_width(20)
ctx.move_to(250,100)
ctx.line_to(250,400)
ctx.set_line_cap(cairo.LINE_CAP_ROUND)
ctx.stroke()

ctx.set_source_rgb(0,1,0)
ctx.set_line_width(20)
ctx.move_to(100,250)
ctx.line_to(400,250)
ctx.set_line_cap(cairo.LINE_CAP_ROUND)
ctx.stroke()

file_path = "shape3.png"
surface.write_to_png(file_path)

surface.write_to_png(f"{OUTPUT_DIRECTORY}shape3.png")
