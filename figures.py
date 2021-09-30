
from mymath import *

class Material(object):
    #difuse represents colors with a V3
    def __init__(self, diffuse = None, specular = 1, type = 0, ior = 1):
        self.diffuse = diffuse
        self.specular = specular
        self.type = type
        self.ior = ior


class Intersect(object):
    def __init__(self, distance, sceneObj, point, normal):
        self.distance = distance
        self.refObj = sceneObj
        self.point = point
        self.normal = normal

class Sphere(object):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, orig, dir):
        L = sub(self.center, orig)
        l = L.x*L.x+L.y*L.y+L.z*L.z
        tca = dot(L, dir)
        d = (l - tca**2) 

        if d > self.radius*self.radius:
            return None

        thc = (self.radius**2 - d) ** 0.5
        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0:
            t0 = t1

        if t0 < 0:
            return None

        point = segmentoRecta(orig, t0, dir)
        normal = norm(sub(point, self.center))
        return Intersect( distance = t0, point = point, normal=normal, sceneObj=self )

