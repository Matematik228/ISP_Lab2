class Vector:
    def __init__(self, *args):
        self.measures = [int(x) for x in args]

    def __getitem__(self, item):
        return self.measures[item]

    def __len__(self):
        return len(self.measures)

    def __abs__(self):
        val = 0
        for i in self:
            val += i ** 2
        return val ** 0.5

    def add(self, other):
        assert len(self) == len(other)
        for i in range(len(self)):
            self.measures[i] += other.measures[i]

    def __iadd__(self, other):
        self.add(other)
        return self

    def __add__(self, other):
        new = Vector()
        new.measures = self.measures.copy()
        new.add(other)
        return new

    def __neg__(self):
        new = Vector()
        new.measures = self.measures.copy()
        for i in range(len(new)):
            new.measures[i] *= -1
        return new

    def sub(self, other):
        self.add(-other)

    def __isub__(self, other):
        self.sub(other)
        return self

    def __sub__(self, other):
        new = Vector()
        new.measures = self.measures.copy()
        new.sub(other)
        return new

    def mul(self, other):
        for i in range(len(self)):
            self.measures[i] *= other

    def scalar_mul(self, other):
        assert len(self) == len(other)
        mul = 0
        for i in range(len(self)):
            mul += self.measures[i] * other.measures[i]
        return mul

    def __imul__(self, other):
        assert isinstance(other, int)
        self.mul(other)
        return self

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.scalar_mul(other)
        new = Vector()
        new.measures = self.measures.copy()
        new.mul(other)
        return new

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self.measures[i] != other.measures[i]:
                return False
        return True

    def __ne__(self, other):
        return not(self == other)

    def __str__(self):
        result = '{'
        for x in self:
            result += str(x) + ', '
        return result[:-2] + '}'


if __name__ == '__main__':
    v1 = Vector(3, 4, 5)
    v2 = Vector(1, 2, 3)
    v2 *= -3
    print(v1 - v2)
