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

        # python method using list comprehension and in build func
        # l = []
        # l.append(a)
        # l.append(b)
        # return sum(l)

    def min_bit_flips(self, start: int, goal: int) -> int:
        """
            Descriptions:   Given start, determine the minimum bit flips to get to the goal
            start:          int
            goal:           int
            return:         minimum bit flips
        """
        # str of binary start and goal
        s,g = bin(start)[2:],bin(goal)[2:]
        # Trade MC for TC
        s_len, g_len = len(s), len(g)
        
        # if length does not match, append 0 at the front abs difference about of times
        if s_len != g_len:
            if s_len>g_len:
                g="0"*(s_len-g_len)+g
            else:
                s="0"*(g_len-s_len)+s
        flips = 0
        for i, ele in enumerate(s):
            if ele is not g[i]:
                flips+=1
        return flips
    
if __name__ == "__main__":
    b=b_solutions()
    print(b.two_int_sum(3,4))
