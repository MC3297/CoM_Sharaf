from svgpathtools import svg2paths, Path
import numpy as np

def real(z):
    try: return np.poly1d(z.coeffs.real)
    except AttributeError: return z.real
def imag(z):
    try: return np.poly1d(z.coeffs.imag)
    except AttributeError: return z.imag
def get_coms(self):
    def x_com_sum(path):
        region = 0
        for seg in path:
            x = real(seg.poly())
            y = imag(seg.poly())
            dx = real(seg.poly()).deriv()
            integrand = x*y*dx
            integral = integrand.integ()
            region += integral(1) - integral(0)
        return region
    def y_com_sum(path):
        region = 0
        for seg in path:
            x = real(seg.poly())
            y = imag(seg.poly())
            dy = imag(seg.poly()).deriv()
            integrand = y*x*dy
            integral = integrand.integ()
            region += integral(1) - integral(0)
        return region
    path = [seg for seg in self]
    return (abs(x_com_sum(Path(*path))), abs(y_com_sum(Path(*path))))

paths, attributes = svg2paths("edited.svg")
areas, xcomsum, ycomsum = [], [], []
region_id = 0
for path in paths:
    A = Path.area(path)#equivalent to using x*dy in above functions
    areas.append(A)
    K = get_coms(path)
    xcomsum.append(K[0])
    ycomsum.append(K[1])
    region_id += 1

total_area = areas[0] - sum(areas[1:])
print("total area:", total_area)
xcom = (xcomsum[0] - sum(xcomsum[1:])) / total_area
ycom = (ycomsum[0] - sum(ycomsum[1:])) / total_area

#shift coordinate system so origin lies on figure by subtracting 200
print("xcom and ycom are:", xcom-200, ycom-200)