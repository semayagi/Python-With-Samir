# Кратчайший путь с операциями: +1, -1, *2

import math
def min_steps(start: int, target: int, way=None) -> int:
    if start == target:
        return 1
    
    if way == None:
        way = [start]
    elif start in way:
        return math.inf     # петля
    else:
        way = way[:]        # поверхностная копия
        way.append(start)
        
    if start == 0:
        return min_steps(start+1, target, way)
    else:
        return min(min_steps(start + 1, target, way), min_steps(start*2, target, way), min_steps(start-1, target, way))
    
    
print(min_steps(2, 9))