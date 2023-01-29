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
            opp = target - nums[i]
            if opp in nums:
                if opp is not nums[i]:
                    return [i,nums.index(opp)]

if __name__ == "__main__":
    arr = array_solutions()

    # nums = [2,7,11,15]
    # print(arr.two_sum(nums, 22))