class b_solutions:
    def two_int_sum(self, a: int, b: int) -> int:
        # fmt: off
        """
            Description: Given two int, perform summation without using "+" or "-" operators
            a,b:         Two int to be added
            return:      Int sum of a,b
        """
        # fmt: on

        carry,sum = 1,0
        # iterate when there is a bit to carry forward
        while carry != 0:
            # carry calculation
            carry = (a&b)<<1
            # sum calculation
            sum = a^b
            a=sum
            b=carry
        
        return sum

if __name__ == "__main__":
    b=b_solutions()
    print(b.two_int_sum(3,4))
