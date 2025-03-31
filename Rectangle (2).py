class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, width=100, height=200, corner=None):
        self.width = width
        self.height = height
        self.corner = corner if corner else Point()

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width / 2
    p.y = rect.corner.y + rect.height / 2
    return p

box = Rectangle()

center = find_center(box)
print(f"Center of the rectangle is at ({center.x}, {center.y})")