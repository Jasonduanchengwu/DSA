class array_solutions:
    def two_sum(self, nums: list[int], target: int)-> list[int]:
        #fmt: off
        """
            Description:    Given an array of integers nums and an integer target, 
                            return indices of the two numbers such that they add up to target. 
                            There is exactly one solution and two numbers cannot be the same element.
            nums:           list of int in the array
            target:         the target sum of the two numbers
            return:         List of the two numbers that adds up to the target
        """
        #fmt: on

        for i in range(len(nums)):
            diff = target - nums[i]
            # check if current num and the difference exits in nums
            if diff in nums:
                # checks if they are not the same element
                if diff is not nums[i]:
                    # i always front of index of diff due to iteration
                    return [i,nums.index(diff)]

    def max_profit(self, prices: list[int]) -> int:
        #fmt: off
        """
            Description:    Given an array of prices of an item on each day, 
                            find the maximum profit if you were to buy one day and sell on a future date.             
            prices:         list of prices on different days
            return:         Maximum profit in int
        """
        #fmt: on

        left = right = profit = 0
        while right < len(prices):
            # update left index when price of next day is lower than previous
            if prices[right]<prices[left]:
                left = right
            profit = max(profit, prices[right]-prices[left])
            right+=1

        return profit

    def magitude_of_ele_sum_and_digit_sum(self, nums: list[int]) -> int:
        """
            Descriptions:   Given an positive Int array nums, 
                            return the absolute difference of the elements sum and the digit sums
            nums:           array of Integers
            return:         Absolute difference of the elements sum and the digit sums
        """
        digit_sum = 0
        for ele in nums:
            # only perform list comprehension when the element is more than 10
            if float(ele)/10>=1.0:
                digit_sum += sum([int(d) for d in str(ele)])
            else:
                digit_sum += ele
        return abs(sum(nums) - digit_sum)

    def remove_duplicate(self, nums: list[int]) -> tuple[int,list[int]]:
        """
            Descriptions:   Given an array of integers, remove any duplicate integers. In-space O(1) memory complexity
            nums:           Array of integers
            return:         both the count of non-duplicated element and the new array
        """
        temp = None
        count = 0
        length = len(nums)
        for i in range(length):
            # remove duplicates
            if nums[i] == temp:
                nums[i] = None   
            else:
                count += 1
                temp = nums[i]
        # remove None in list
        for i in range(length-count):
            nums.remove(None)
        return count, nums

    def remove_element(self, nums: list[int], val: int)-> tuple[int, list[int]]:
        """
            Descriptions:   Given a list of int, remove all occurance of val 
                            and return the number of val removed and the new list
            nums:           A list of integers
            val:            The value to be removed
            return:         The number of val removed and the new list
        """
        count = 0
        length = len(nums)
        while val in nums:
            nums.remove(val)
            count +=1
        return length - count, nums

    def plus_one(self, digits: list[int])->list[int]:
        """
            Descriptions:   produce a list of ints that was the comprehension of digits plus one
            digits:         list of int
            return          plus one list of int
        """
        whole = ""
        for ele in digits:
            whole+=str(ele)
        whole = str(int(whole)+1)
        digits = [int(d) for d in whole]
        return digits
    
    def xor_operation(self, n: int, s: int)->int:
        """
            Description:    Given two int parameter: n and s, find the xor outcome of nums, 
                            where nums is an array of size n and nums[i] = s + 2*i
            n:              size of array
            s:              starting displacement
            return:         XOR outcome
        """
        # populating nums
        nums = [0]*n
        for i in range(n):
            nums[i] = s + 2*i
        
        # perform XOR
        result = nums[0]
        for i in range(1,n):
            result = result ^ nums[i]
        return result

    def match_count(self, dict: list[list[str]], key: str, val: str)->int:
        """
            Description:    Given a 2d array that contains a list of list of values with different values 
                            in indexes represented by different corresponding keys. 
                            Find the number of matches given the key and val. The keys are type, color and name
            dict:           2d array
            key:            The key to search
            val:            The value to search
            return:         The number of matches
        """
        if key == "type":
            key = 0
        elif key == "color":
            key = 1
        else:
            key = 2
        
        m=0
        for ele in dict:
            if ele[key] is val:
                m +=1
        return m

    def arithmetic_triplets(self, nums: list[int], diff: int) -> int:
        """
            Descriptions:   Given an ascending array and a difference where 
                            indexes i<j<k and nums[j]-nums[i] = diff and nums[k]-nums[j] = diff
            nums:           List of numbers
            diff:           The difference
            return:         Number of arithmetic triplets
        """

        # the second set of diff exist only if first set of diff exist
        return sum(n-diff in nums and n-diff*2 in nums for n in nums)

    def left_right_difference(self, nums: list[int]) -> list[int]:
        """
            Descriptions:   Given an array of int, calculate the difference between the left subarray 
                            and the right subarray at every element position
            nums:           List of numbers
            return:         The difference array
        """
        length = len(nums)
        output = [0]*length
        for i in range(length):
            # for absolute values
            output[i] = abs(sum(nums[:i])-sum(nums[i+1:]))
        return output
    
    def min_moves_seats(self, seats: list[int], students: list[int]) -> int:
        """
            Descriptions:   Given two arrays which represents positions of the students and seats,
                            if each seat can only hold one student, determine the minimum moves of students
                            to make sure every students has a seat
            seats:          postions of seats
            students:       postions of students
            return:         num of moves
        """
        # min moves would be the sum of the abs diff of seats and students in order
        seats.sort()
        students.sort()
        return sum(abs(x-y) for x,y in zip(seats,students))
    
    def sum_max_row_value(self, grid: list[list[int]]) -> int:
        """
            Description:    Given a m x n grid, find the max of the maxes of every row and remove all maxes
                            until grid is empty
            grid:           two-dimensional array
            return:         sum of maxes
        """
        # sort every row, that way every comparison of ith ele in all tuple of every row will be paired
        # can simply get the max of same index ele on every row and sum the result
        grid = [sorted(row) for row in grid]
        return sum(max(ele) for ele in list[zip(*grid)])
    
if __name__ == "__main__":
    arr = array_solutions()

    nums = [7,16,4,23,1]
    print(arr.magitude_of_ele_sum_and_digit_sum(nums))