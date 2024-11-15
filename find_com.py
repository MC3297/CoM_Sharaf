from svgpathtools import svg2paths, Path, Line, QuadraticBezier, CubicBezier
import numpy as np

def real(z):
    try:
        return np.poly1d(z.coeffs.real)
    except AttributeError:
        return z.real

def imag(z):
    try:
        return np.poly1d(z.coeffs.imag)
    except AttributeError:
        return z.imag

def weighted_area(self):
    
    def x_com_sum(path):
        area_enclosed = 0
        for seg in path:
            x = real(seg.poly())
            y = imag(seg.poly())
            dx = real(seg.poly()).deriv()
            integrand = x*y*dx
            integral = integrand.integ()
            area_enclosed += integral(1) - integral(0)
        return area_enclosed
    
    def y_com_sum(path):
        area_enclosed = 0
        for seg in path:
            x = real(seg.poly())
            y = imag(seg.poly())
            dy = imag(seg.poly()).deriv()
            integrand = y*x*dy
            integral = integrand.integ()
            area_enclosed += integral(1) - integral(0)
        return area_enclosed

    assert self.isclosed()

    path_approx = []
    for seg in self:
        path_approx.append(seg)
    return (abs(x_com_sum(Path(*path_approx))), abs(y_com_sum(Path(*path_approx))))

paths, attributes = svg2paths("edited.svg")

cnt = 0
areas = []
xcoms = []
ycoms = []
for path in paths:
    A = Path.area(path)
    areas.append(A)
    K = weighted_area(path)
    
    #xcom and ycom of this region
    #print(K[0]/A, K[1]/A)
    
    xcoms.append(K[0])
    ycoms.append(K[1])
    #print("Area:", A, "Segments:", len(path))
    cnt += 1
#<circle cx="484" cy="390" r="10" fill="red"/>

total_area = areas[0] - sum(areas[1:])
xsum = xcoms[0] - sum(xcoms[1:])
ysum = ycoms[0] - sum(ycoms[1:])

print("xcom and ycom are:", xsum/total_area, ysum/total_area)