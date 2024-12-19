import math

def triangle_area(a, b, c):
   
    s = (a + b + c) / 2
    if s <= a or s <= b or s <= c:  
        return 0 
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def are_triangles_equal_area(a1, b1, c1, a2, b2, c2):
  
    area1 = triangle_area(a1, b1, c1)
    area2 = triangle_area(a2, b2, c2)
    if area1 == 0 or area2 == 0: 
        return False
    return math.isclose(area1, area2) 


a1, b1, c1 = 1, 1, 1
a2, b2, c2 = 1, 1, 1

if are_triangles_equal_area(a1, b1, c1, a2, b2, c2):
    print("Treygolniki ravnovelikie")
else:
    print("Pathetic!!!")
