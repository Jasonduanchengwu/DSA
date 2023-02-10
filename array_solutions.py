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
    
    def length_of_last_word(self, s: str)->int:
        """
            Descriptions:   Given a string, return the length of the last word in the string
            s:              String given
            return:         length of the last word 
        """
        return len(s.split()[-1])
        
if __name__ == "__main__":
    arr = array_solutions()

    nums = [7,16,4,23,1]
    print(arr.magitude_of_ele_sum_and_digit_sum(nums))