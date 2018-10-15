"""
    Priscilla Short's Fraction Class
"""

def gcd(m, n):
    
    """
        Optional gcd method
    """
    
    while m%n != 0:
        oldm = m
        oldn = n
            
        m = oldn
        n = oldm%oldn
    return n

class Fraction:

    def __init__(self, num=1, den=1):
        
        """
            Fraction Constructor
        """

        if den == 0:
            raise ValueError("Denomenator cannot be zero")
        
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError("Numerator and Denominator must be type int")
        
        if den < 0:
            if num < 0:
                num = abs(num)
            else:
                num *= -1
            den = abs(den)
            
        dev = Fraction.gcd(num, den)
        self.num = num // dev
        self.den = den // dev

    def __str__(self):

        """
            Overloaded string method
        """
        
        return str(self.num) + '/' + str(self.den)

    __repr__ = __str__

    def show(self):

        """
            Optional show method
        """
        
        print(self.num,"/",self.den)

    def __add__(self, other):

        """
            Overloaded + method
        """
        
        return Fraction((self.num * other.den + self.den * other.num), (self.den * other.den))

    __radd__ = __add__

    def __sub__(self, other):

        """
            Overloaded - method
        """
        
        return Fraction((self.num * other.den - self.den * other.num), (self.den * other.den))

    def __mul__(self, other):

        """
            Overloaded * method
        """
        
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):

        """
            Overloaded / method
        """
        
        return Fraction(self.num * other.den, self.den * other.num)

    def __iadd__(self, other):

        """
            Overloaded += method
        """
        
        self = self + other
        return self

    def __eq__(self, other):

        """
            Overloaded = method
        """
        
        return self.num == other.num and self.den == other.den

    def __lt__(self, other):

        """
            Overloaded < method
        """
        
        firstnum = self.num / self.den
        secondnum = other.num / other.den
        return firstnum < secondnum

    def __gt__(self, other):

        """
            Overloaded > method
        """
        
        firstnum = self.num / self.den
        secondnum = other.num / other.den
        return firstnum > secondnum

    def __le__(self, other):

        """
            Overloaded <= method
        """
        
        firstnum = self.num / self.den
        secondnum = other.num / other.den
        return firstnum <= secondnum

    def __ge__(self, other):

        """
            Overloaded >= method
        """
        
        firstnum = self.num / self.den
        secondnum = other.num / other.den
        return firstnum >= secondnum

    def __ne__(self, other):

        """
            Overloaded != method
        """
        
        return self.num != other.num or self.den != other.den

    @staticmethod
    def gcd(a, b):

        """
            Static (in class) gcd method
        """
        
        if b != 0:
            return Fraction.gcd(b, a % b)
        else:
            return abs(a)
        
