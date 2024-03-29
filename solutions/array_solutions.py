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
    
    def max_prod_diff_pairs(self, n: list[int]) -> int:
        """
            Descriptions:   find the max difference between the product of two pairs
            n:              a list of int
            return:         the max difference
        """
        # sort to have min pair be first two index and max pair to be last two
        n=sorted(n)
        return n[-1]*n[-2]-n[0]*n[1]
    
    def sort_people(self, names: list[str], heights: list[int]) -> list[str]:
        """
            Descriptions:   find list of names in descending height
            names:          list of names
            heights:        list of heights
            return:         list of ordered names
        """
        # zips names,height, sort base on height in descending and return list of names
        return [ele[0] for ele in sorted([ele for ele in zip(names,heights)], key=lambda x:x[1], reverse= True)]
    
    def flip_and_invert_image(self, image: list[list[int]]) -> list[list[int]]:
        """
            Descriptions:   flip and invert pixel values of an image
            image:          binary matrix n x m with 0 or 1 pixel values
            return:         n x m matrix
        """
        for i in range(len(image)):
            image[i]=image[i][::-1]
            for j in range(len(image[i])):
                # using bool
                image[i][j]=int(not(image[i][j]))
        return image

    def diagonal_sum(self, mat: list[list[int]]) -> int:
        """
            Descriptions:   find the summation of the both the diagonals of the matrix
            mat:            a n x n matrix
            return:         the sum
        """
        length, res, j = len(mat[0]), 0, 0
        for i in range(length):
            # when n is odd in a nxn matrix, the middle row number will only be added once
            if length%2==1 and i==length//2: res+=mat[i][j]
            else: res=res+mat[i][j]+mat[i][-(j+1)]
            j+=1
        return res
    
    def max_product(self, nums: list[int]) -> int:
        """
            Descriptions:   find the maximum product between 2 (elements-1)
            nums:           array of int
            return:         max product
        """
        m=max(nums)
        nums.remove(m)
        return (m-1)*(max(nums)-1)
    
    def pivot_integer(self, n: int)-> int:
        """
            Descriptions:   find the int where sum <= element == sum >= element smaller than n
                            Ex. if n=8, 1+2+3+4+5+6 = 6+7+8 = 21
            n:              int
            return:         int
        """
        # TODO: could be improved with simplified equations
        res=[]
        # create a list of integers from 1 to n
        [res.append(i) for i in range(1,n+1)]
        # include only int where sum before == sum after
        r = [ele for i,ele in enumerate(res) if sum(res[:i])==sum(res[i+1:])]
        if r == []: return -1
        else: return r[0]

    def subset_xor_sum(self, nums: list[int]) -> int:
        """
            Descriptions:   find the XOR sum of all the possible subsets in the list
            nums:           list of int
            return:         the total sum
        """
        # TODO: could be improved with OR bitwise calculations
        x,stack,res = len(nums), [],0
        masks = [1 << i for i in range(x)]
        # creating a list of all possible sublists
        for i in range(1 << x):
            stack.append([ss for mask, ss in zip(masks, nums) if i & mask])
        # perform XOR on all sublists elements and sum them
        for i in stack:
            t,r=0,0
            for j in i:
                r=j^t
                t=r
            res+=r
        return res
    
    def separate_digits(self, nums: list[int]) -> list[int]:
        """
            Descriptions:   find the list of digits in the list of numbers given
            nums:           list of numbers given
            return:         list of digits
        """
        # turn list of nums into a string of all digits, then put every char into a list
        return [int(ele) for ele in "".join([""+str(ele) for ele in nums])]
    
    def largest_altitude(self, gain: list[int]) -> int:
        """
            Descriptions:   find the max altitude reached if starting altitue is 0
            gain:           list of changes of altitude
            return:         max altitude reached
        """
        max_alt,cur_alt=0, 0
        for ele in gain:
            cur_alt+=ele
            max_alt=max(max_alt,cur_alt)
        return max_alt

    def min_time_to_visit_all_points(self, points: list[list[int]]) -> int:
        """
            Descriptions:   find the minimum time to visit all nodes in the order of the given array
                            ,given each travel takes one unit of time
            points:         list of coordinates
            return:         time taken to visit all nodes
        """
        # max maginitude of difference of x,y from the points is the minimum time needed to travel from one point to another
        # take the maximum of the maginitude of difference of x,y from the points, sum the differences
        return sum([max(abs(points[i+1][0]-points[i][0]), abs(points[i+1][1]-points[i][1])) for i in range(len(points)-1)])

    def num_of_largest_square(self, rects: list[list[int]]) -> int:
        """
            Descriptions:   find the number of largest squares in a list of rectangles
                            (rect = [length, width])
            rects:          list of rect
            return:         num of largest squares
        """
        rects=[min(rect) for rect in rects]
        return rects.count(max(rects))

    def min_operations(self, nums: list[int]) -> int:
        """
            Descriptions:   find the total increments for the list to be ascending
                            (Ex. [1,3,3,2,4] -> [1,3,4,5,6])
            nums:           list of int
            return:         total increment
        """
        count=0
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                # save increment as nums[i+1] changes
                increment=nums[i]-nums[i+1]+1
                nums[i+1]+=increment
                count+=increment
        return count

    def vowel_strings(self, words: list[str], left: int, right: int) -> int:
        """
            Descriptions:   count the number of words that starts and ends with a vowel (a,e,i,o,u) from within the left and right index
            words:          list of words
            left:           left index
            right:          right index
            return:         number of matched words
        """
        vowels= {"a", "e", "i", "o", "u"}
        count=0
        for word in words[left:right+1]:
            if word[0] in vowels and word[-1] in vowels:
                count+=1
        return count
    
if __name__ == "__main__":
    arr = array_solutions()

    nums = [7,16,4,23,1]
    print(arr.magitude_of_ele_sum_and_digit_sum(nums))