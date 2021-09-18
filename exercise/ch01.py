import typing as tp

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
        if other == None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other: any) -> bool:
        if other == None:
            return False
        return self.num != other.num and self.prime != other.prime



if __name__ == '__main__':
    a = FieldElement(7, 13)
    b = FieldElement(6, 12)

    print(a==b)
    print(a==a)
    print(a!=b)
    print(a!=a)