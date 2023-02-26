class num_solutions:
    def num_of_matches(self, n: int)->int:
        match = 0
        while n > 1:
            if n%2 == 1:
                match += (n-1)//2+1
                n=(n-1)//2
            else:
                match += n//2
                n //=2
        return match

if __name__ == "__main__":
    no = num_solutions()
    n = 7
    print(no.num_of_matches(n))