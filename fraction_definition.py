import math
import fractions


class InvalidArgumentException(Exception):
    def __init__(self, exp_str):
        Exception.__init__(self)
        self.exp_str = exp_str


class Fraction:
    def __init__(self, numerator=None, denominator=None):
        """

        :type numerator: int float str
        """
        self.numerator = numerator
        self.denominator = denominator

        if numerator is None:
            self.numerator = 0
        else:
            self.fraction()

    def __str__(self):
        if self.denominator is not None:
            return str(self.numerator) + "/" + str(self.denominator)
        else:
            return str(self.numerator)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.numerator == other.numerator and self.denominator == other.denominator
        elif isinstance(other, str):
            return True if str(self.numerator) + "/" + str(self.denominator) == other else False
        elif isinstance(other, float):
            return True if self.numerator / self.denominator == other else False

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            if self.args_not_none() and other.args_not_none():
                return self.numerator / self.denominator < other.numerator / other.denominator
            elif self.args_not_none():
                return self.numerator / self.denominator < other.numerator
            elif other.args_not_none():
                return self.numerator < other.numerator / other.denominator
            else:
                return self.numerator < other.numerator

    def __le__(self, other):
        if isinstance(other, self.__class__):
            if self.args_not_none() and other.args_not_none():
                return self.numerator / self.denominator <= other.numerator / other.denominator
            elif self.args_not_none():
                return self.numerator / self.denominator <= other.numerator
            elif other.args_not_none():
                return self.numerator <= other.numerator / other.denominator
            else:
                return self.numerator <= other.numerator

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            if self.args_not_none() and other.args_not_none():
                return self.numerator / self.denominator >= other.numerator / other.denominator
            elif self.args_not_none():
                return self.numerator / self.denominator >= other.numerator
            elif other.args_not_none():
                return self.numerator >= other.numerator / other.denominator
            else:
                return self.numerator >= other.numerator

    def __repr__(self):
        if self.denominator is not None:
            return str(self.numerator) + "/" + str(self.denominator)
        else:
            return str(self.numerator)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.add_objects(other)
        else:
            return None

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self.sub_objects(other)
        else:
            return None

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return self.mul_objects(other)
        else:
            return None

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return self.div_objects(other)
        else:
            return None

    def __abs__(self):
        return Fraction(abs(self.numerator))

    def __ceil__(self):
        if self.args_not_none():
            return Fraction(math.ceil(self.numerator / self.denominator))
        else:
            return Fraction(math.ceil(self.numerator))

    def __floor__(self):
        if self.args_not_none():
            return Fraction(math.floor(self.numerator / self.denominator))
        else:
            return Fraction(math.floor(self.numerator))

    def fraction(self):
        if self.denominator is not None:
            self.convert_to_fraction()
        else:
            if isinstance(self.numerator, float):
                self.set_denominator()
            elif isinstance(self.numerator, str):
                if "/" in self.numerator:
                    arg_list = self.numerator.strip().split("/")
                    try:
                        self.numerator = int(arg_list[0])
                        self.denominator = int(arg_list[1])
                    except Exception:
                        raise InvalidArgumentException("Invalid argument")

                    self.convert_to_fraction()
                elif "." in self.numerator:
                    self.numerator = float(self.numerator)
                    self.set_denominator()
                else:
                    try:
                        self.numerator = int(self.numerator)
                    except Exception:
                        raise InvalidArgumentException("Invalid argument")

    def set_denominator(self):
        flt = str(self.numerator)
        mul = 10 ** (len(flt) - flt.find(".") - 1)
        self.numerator = int(self.numerator * mul)
        self.denominator = mul
        self.convert_to_fraction()

    def convert_to_fraction(self):
        gcd = math.gcd(self.numerator, self.denominator)

        self.numerator = math.floor(self.numerator / gcd)
        self.denominator = math.floor(self.denominator / gcd)

        if self.denominator == 1:
            self.denominator = None

    def args_not_none(self):
        return self.numerator is not None and self.denominator is not None

    def add_objects(self, other):
        if self.args_not_none() and other.args_not_none():
            return Fraction((self.numerator * other.denominator + other.numerator * self.denominator), (self.denominator * other.denominator))
        elif self.args_not_none():
            return Fraction((self.numerator + self.denominator * other.numerator) / self.denominator)
        elif other.args_not_none():
            return Fraction((other.denominator * self.numerator + other.numerator) / other.denominator)
        else:
            return Fraction(self.numerator + other.numerator)

    def sub_objects(self, other):
        if self.args_not_none() and other.args_not_none():
            return Fraction((self.numerator * other.denominator - other.numerator * self.denominator), (self.denominator * other.denominator))
        elif self.args_not_none():
            return Fraction((self.numerator - self.denominator * other.numerator), self.denominator)
        elif other.args_not_none():
            return Fraction((-other.denominator * self.numerator + other.numerator), other.denominator)
        else:
            return Fraction(self.numerator - other.numerator)

    def mul_objects(self, other):
        if self.args_not_none() and other.args_not_none():
            return Fraction(self.numerator * other.numerator, other.denominator * self.denominator)
        elif self.args_not_none():
            return Fraction((self.numerator * other.numerator), self.denominator)
        elif other.args_not_none():
            return Fraction(other.numerator * self.numerator, other.denominator)
        else:
            return Fraction(self.numerator * other.numerator)

    def div_objects(self, other):
        if self.args_not_none() and other.args_not_none():
            return Fraction(self.numerator * other.denominator, other.numerator * self.denominator)
        elif self.args_not_none():
            return Fraction(self.numerator, (self.denominator * other.numerator))
        elif other.args_not_none():
            return Fraction(other.denominator * self.numerator, other.numerator)
        else:
            return Fraction(self.numerator / other.numerator)


def test():
    assert Fraction(3 / 4) == Fraction('0.75') == Fraction(0.75) == Fraction('3/4')
    assert Fraction(1) * Fraction(5) == Fraction(5)

    assert Fraction(1) < Fraction(2)

    assert Fraction(1 / 2) == 1 / 2

    assert Fraction(1) <= Fraction(2.8)
    assert Fraction(1) <= Fraction(1)

    assert Fraction(4) >= Fraction(2)
    assert Fraction(4) >= Fraction(4)

    assert abs(Fraction(-1)) == Fraction(1)

    half = Fraction(0.5)
    one = Fraction(1)

    assert math.ceil(half) == one

    assert Fraction(3, 10) + Fraction(5, 10) == Fraction(4 / 5)
    assert Fraction(1, 2) + Fraction(5, 3) == Fraction(13, 6)

    assert Fraction(1, 2) - Fraction(5, 3) == Fraction(-7, 6)
    assert Fraction(3 / 10) - Fraction(-5 / 10) == Fraction(4 / 5)

    assert Fraction(1, 2) * Fraction(5, 3) == Fraction(5, 6)
    assert Fraction(1, 2) * Fraction(5) == Fraction(5, 2)

    assert Fraction(1, 2) / Fraction(5) == Fraction(1, 10)
    assert Fraction(1, 2) / Fraction(5, 3) == Fraction(3, 10)

    assert math.floor(half) == Fraction(0)


if __name__ == "__main__":
    test()
