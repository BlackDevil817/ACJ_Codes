class point:
    """Represents a point"""
class Rectangle:
    """Represents a rectangle.
    attributes: width, height, corner.
    """
box=Rectangle()
box.width=200
box.height=100
box.corner=point()
box.corner.x=0
box.corner.y=0
def find_center(rect):
    p=point()
    p.x=rect.corner.x+rect.width/2
    p.y=rect.corner.y+rect.height/2
    return p
def print_point(p):
    print(f"({p.x}, {p.y})")
center=find_center(box)
print_point(center)