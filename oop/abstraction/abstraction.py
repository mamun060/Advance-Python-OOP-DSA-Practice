def total_area(shapes):
    # Any object with .area() works: Circle, Rectangle, Polygon, etc.
    return sum(shape.area() for shape in shapes)
