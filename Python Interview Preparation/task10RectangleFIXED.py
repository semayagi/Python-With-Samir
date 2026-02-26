class Rectangle:
    def __init__(self, width: int = 0, height: int = 0, points: list[tuple] | None = None): # 1. Корректная инициализация
        self.width = width
        self.height = height
        self.points = points | []
        
    def area(self): # 2. Забыли self
        return self.width * self.height
    
    @classmethod
    def from_square(cls, side):
        return cls(side, side) # 3. Нужно использовать cls
    
    @staticmethod
    def is_valid(rect):
        # 4. isinstance вместо type() is + поменять порядок во избежание лишних проверок
        return isinstance(rect, Rectangle) and rect.width > 0 and rect.height > 0
    
    
r1 = Rectangle(2, 3)
r2 = Rectangle.from_square(5)
r3 = Rectangle()
Rectangle().points.append((0, 0)) # 5. points - поле объекта класса, а не самого класса => создадим экземпляр (добавили ())
print(r1.area(), r2.area(), r3.area())