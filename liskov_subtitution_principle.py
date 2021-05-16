class Rectangle:
    def __init__(self, width, height) -> None:
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self) -> str:
        return f'Width: {self._width}, height: {self._height}'

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value

# example of liskov subtitution violation
# because in this case will make rectange class
# won't work anymore where in liskov_subtitution_principle
# it should be still working
class Square(Rectangle):
    def __init__(self, size) -> None:
        Rectangle.__init__(self, size, size)
    
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value

def use_it(rc): 
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area}')

rc = Rectangle(2,3)
use_it(rc)