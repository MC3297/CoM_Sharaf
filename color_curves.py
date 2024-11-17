from svgpathtools import svg2paths, Path, Line, QuadraticBezier, CubicBezier

paths, attributes = svg2paths("edited.svg")

def h(r,g,b):
    return r*256**2 + g*256 + b

col_names = {h(0,0,0):"black", h(255,50,50):"red", h(255,100,34):"orange", h(255,218,33):"yellow", h(51,221,0):"green", h(57,101,204):"blue", h(255,192,200):"pink"}
colors = [h(255,50,50),h(255,100,34),h(255,218,33),h(51,221,0),h(57,101,204),h(255,192,200)]

output = open("colored.svg","w")
output.write('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd"><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="1026px" height="835px" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd" xmlns:xlink="http://www.w3.org/1999/xlink">')
output.write('\n')

region_id = 0
for path in paths:
    print(f"Region: {region_id:02d}  | Segments: {len(path):02d}    | Area: {Path.area(path):04.3f}")
    print("S           | A               | B               | E           | Color")
    output.write(f"\n<g fill='transparent'>\n")
    ind = -1
    for seg in path:
        #print(seg)
        if (ind == -1): color = h(0,0,0)
        else: color = colors[ind%len(colors)]
        print(f'{seg.start.real:05.1f},{seg.start.imag:05.1f} | {seg.control1.real:07.3f},{seg.control1.imag:07.3f} | {seg.control2.real:07.3f},{seg.control2.imag:07.3f} | {seg.end.real:05.1f},{seg.end.imag:05.1f} | {col_names[color]}')
        output.write(f'<path d="M {seg.start.real} {seg.start.imag} C {seg.control1.real} {seg.control1.imag} {seg.control2.real} {seg.control2.imag} {seg.end.real} {seg.end.imag}" stroke="#{hex(color)[2:].zfill(6)}"/>')
        output.write('\n')
        ind += 1
    region_id += 1
    print('\n')
    output.write('</g>\n')

print("total segments:", sum([len(i) for i in paths]))
output.write('</svg>')

#run: python3 color_curves.py > data.txt