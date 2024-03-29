class num_solutions:
    def num_of_matches(self, n: int)->int:
        # fmt: off
        """
            Descriptions:   find the number of matches played with n number of competitors
                            (Even n competitors will be paired in two
                            odd n competitors will have 1 person advance randomly
                            the rest of the even pairs compete)
            n:              number of competitors
            return:         num of matches
        """
        # fmt: on
        match = 0
        while n > 1:
            if n%2 == 1:
                match += (n-1)//2+1
                n=(n-1)//2
            else:
                match += n//2
                n //=2
        return match

    def num_of_common_factors(self, a: int, b: int) -> int:
        """
            Descriptions:    find the number of common factors of a and b
            a,b:             two int
            return:          the number
        """
        def smaller_int(a: int, b: int) -> int:
            if a>=b:
                return b
            else: return a
        # trading slightly lower TC for readability
        return len([i for i in range(1,smaller_int(a,b)+1) if a%i==0 and b%i==0])
    
    def self_dividing_numbers(self, left: int, right: int) -> list[int]:
        """
            Descriptions:   find a list of self-dividing numbers with the range from left to right
                            (Ex. 128 is self dividing as 128%1==0, 128%2==0, 128%8==0)
            left:           left boundary
            right:          right boundary
            return:         list of self dividing numbers
        """
        res = []
        for num in range(left, right+1):
            # skip over numbers that contains 0, as you cannot divide by 0
            if "0" in  str(num):
                continue
            if all(num%int(ele)==0 for ele in str(num) if ele is not "0"):
                res.append(num)
        return res
    
if __name__ == "__main__":
    no = num_solutions()
    n = 7
    print(no.num_of_matches(n))