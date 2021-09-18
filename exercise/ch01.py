class FieldElement:
    def __init__(self, num: int, prime: int):
        if num >= prime or num < 0:
            error = 'Num {} not in field ranfe 0 to {}'.format(num, prime - 1)
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self) -> str:
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, other: any) -> bool:
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other: any) -> bool:
        if other is None:
            return False
        return self.num != other.num and self.prime != other.prime

    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in differnt Fields.')
        num = (self.num + other.num) % self.prime
        return __class__(num, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in differnt Fields.')
        num = (self.num - other.num) % self.prime
        return __class__(num, self.prime)


if __name__ == '__main__':
    a = FieldElement(7, 13)
    b = FieldElement(6, 12)

    print((95*45*31)%97)
    print((17*13*19*44)%97)
    print((12**7)*(77**49)%97)

    d = []
    for i in [1,3,7,13,18]:
        for j in range(19):
            d.append((i * j) % 19)
        print(d)
        d = []