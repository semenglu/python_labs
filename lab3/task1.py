#вариант 3 Triangle(треугольник), Rectangle(прямоугольник), методы move(переместить объект на плоскости), compare(T1 t1, T2 t2) сравнение объектов по площади.


import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Shape:
    def __init__(self, id):
        self.id = id
        self.dx = 0  # Смещение по оси X
        self.dy = 0  # Смещение по оси Y

    def move(self, dx, dy):
        self.dx += dx
        self.dy += dy

    def draw(self):
        pass

    @staticmethod
    def compare(shape1, shape2):
        return shape1.area() == shape2.area()

    def area(self):
        raise NotImplementedError("Этот метод должен быть переопределён в подклассах.")


class Triangle(Shape):
    def __init__(self, id, base, height):
        super().__init__(id)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def draw(self):
        plt.gca().add_patch(
            patches.Polygon([(self.dx, self.dy), (self.dx + self.base, self.dy), (self.dx, self.dy + self.height)],
                            closed=True, edgecolor='r', facecolor='none'))


class Rectangle(Shape):
    def __init__(self, id, width, height):
        super().__init__(id)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def draw(self):
        plt.gca().add_patch(
            patches.Rectangle((self.dx, self.dy), self.width, self.height, edgecolor='b', facecolor='none'))


def get_triangle_data():
    base = float(input("Введите основание треугольника: "))
    height = float(input("Введите высоту треугольника: "))
    return base, height


def get_rectangle_data():
    width = float(input("Введите ширину прямоугольника: "))
    height = float(input("Введите высоту прямоугольника: "))
    return width, height


def get_movement_data():
    dx = float(input("На сколько единиц переместить по оси X? "))
    dy = float(input("На сколько единц переместить по оси Y? "))
    return dx, dy


def main():
    print("Треугольник")
    base, height = get_triangle_data()
    triangle = Triangle("треугольник1", base, height)

    print("Прямоугольник")
    width, height = get_rectangle_data()
    rectangle = Rectangle("прямоугольник1", width, height)

    triangle.move(*get_movement_data())
    rectangle.move(*get_movement_data())

    if Shape.compare(triangle, rectangle):
        print("Треугольник и прямоугольник имеют одинаковую площадь.")
    else:
        print("Площади треугольника и прямоугольника различны.")

    triangle.draw()
    rectangle.draw()
    plt.axis('scaled')
    plt.show()


if __name__ == "__main__":
    main()
