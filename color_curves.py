from svgpathtools import svg2paths, Path, Line, QuadraticBezier, CubicBezier

paths, attributes = svg2paths("edited.svg")

def h(r,g,b):
    return r*256**2 + g*256 + b

colors = [h(209,0,0),h(255,102,34),h(255,218,33),h(51,221,0),h(17,51,204),h(34,0,102)]

print('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd"><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="1026px" height="835px" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd" xmlns:xlink="http://www.w3.org/1999/xlink">')

#run "py3 color_curves.py > colored.svg"

for path in paths:
    ind = 0
    for seg in path:
        #print(seg)
        color = colors[ind%len(colors)]
        if ind == 0:
            color = 0
        print(f'<path d="M {seg.start.real} {seg.start.imag} C {seg.control1.real} {seg.control1.imag} {seg.control2.real} {seg.control2.imag} {seg.end.real} {seg.end.imag}" fill="transparent" stroke="#{hex(color)[2:].zfill(6)}"/>')
        ind += 1

print('</svg>')