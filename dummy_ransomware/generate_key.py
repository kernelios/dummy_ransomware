import random
import hashlib


class GenerateKey:
    """
    generate new random key using a math trick:
        http://mathforum.org/library/drmath/view/67061.html
        http://www.math-only-math.com/divisible-by-9.html
    """

    def __sum_digits(self, x):
        """summarize the digits of given number"""
        sum = 0
        for num in str(x):
            sum += int(num)
        return sum

    def __recursive_sum(self, x):
        """recursively summarize the digits of given number"""
        if len(str(x)) == 1:
            return x
        return self.__recursive_sum(self.__sum_digits(x))

    def generate_key(self):
        """
        1. generate random number k.
        2. do: k=3k+3, k=3k random number of iteration.
        3. send k to __recursive_sum.
        4. md5 of the returned value from "__recursive_sum"
        """
        k = random.randint(1, 30000)
        for i in range(random.randint(571, 46755)):
            k *= 3
            k += 3
            k *= 3
        k = self.__recursive_sum(k)
        return hashlib.md5(str(k).encode('utf-8')).hexdigest()
