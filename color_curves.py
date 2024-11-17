from svgpathtools import svg2paths, Path, Line, QuadraticBezier, CubicBezier

paths, attributes = svg2paths("edited.svg")

def h(r,g,b):
    return r*256**2 + g*256 + b

colors = [h(255,50,50),h(255,100,34),h(255,218,33),h(51,221,0),h(57,101,204),h(255,192,200)]

fill_colors = [h(114,2,19),h(69,158,15),h(171,240,22),h(187,49,14),h(54,195,0),h(196,101,21),
               h(229,114,19),h(15,185,1),h(36,21,13),h(83,155,25),h(149,134,21),h(73,198,4),
               h(166,134,15),h(118,85,4),h(169,171,2),h(22,180,17),h(189,151,24),h(38,142,8),
               h(203,116,4),h(119,142,5),h(40,210,8),h(68,220,8),h(233,224,19),h(187,8,17),h(181,11,15)]

output = open("colored.svg","w")
output.write('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd"><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="1026px" height="835px" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd" xmlns:xlink="http://www.w3.org/1999/xlink">')
output.write('\n')

region_id = 0
for path in paths:
    print(f"{region_id:02d} | Segments: {len(path):02d} | Area: {Path.area(path):13f}")
    fill = "#"+hex(fill_colors[region_id])[2:].zfill(6)
    fill = "transparent"
    output.write(f"\n<g fill='{fill}'>\n")
    ind = -1
    for seg in path:
        #print(seg)
        if (ind == -1): color = h(0,0,0)
        else: color = colors[ind%len(colors)]
        output.write(f'<path d="M {seg.start.real} {seg.start.imag} C {seg.control1.real} {seg.control1.imag} {seg.control2.real} {seg.control2.imag} {seg.end.real} {seg.end.imag}" stroke="#{hex(color)[2:].zfill(6)}"/>')
        output.write('\n')
        ind += 1
    region_id += 1
    output.write('</g>\n')

print("total segments:", sum([len(i) for i in paths]))
output.write('</svg>')