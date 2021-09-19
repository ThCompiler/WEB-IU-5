from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    r = Rectangle(6, 6, *(0, 0, 255))
    c = Circle(6, *(0, 255, 0))
    s = Square(6, *(255, 0, 0))
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()