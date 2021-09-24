class Point:
    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = y
        self.y = y

        if self.x is None and self.y is None:
            return
        if self.y**2 != self.x**3 + a * x + b:
            raise ValueError('({}, {}) is not on the curve.'.format(x, y))
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b

    def __ne__(self, other):
        return not(self == other)

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise ValueError('Points {}, {} are not on the same curve.'.format(self, other))
        
        if self.x is None:
            return other
        if other.x is None:
            return self
        if self.x == other.x and self.y != other.y:
            return self.__class__(None, None, self.a, self.b)


if __name__ == '__main__':
    def on_curve(x, y):
        return y**2 == x**3 + 5 * x + 7

    print(on_curve(2,4))
    print(on_curve(-1,-1))
    print(on_curve(18,77))
    print(on_curve(5,7))
