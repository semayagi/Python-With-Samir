class Rectangle:
    def __init__(self, width: int = 0, height: int = 0, points: list[tuple]):
        self.width = width
        self.height = height
        self.points = points
        
    def area(): # Забыли self
        return self.width * self.height
    
    @classmethod
    def from_square(cls, side):
        return Rectangle(side, side)
    
    @staticmethod
    def is_valid(rect):
        return rect.width > 0 and rect.height > 0 and type(rect) is Rectangle
    
    
r1 = Rectangle(2, 3)
r2 = Rectangle.from_square(5)
r3 = Rectangle()
Rectangle.points.append((0, 0))
print(r1.area(), r2.area(), r3.area())