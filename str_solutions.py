class str_solutions:
    def longest_substring_without_repeating_char(self, s: str) -> int:
        # fmt: off
        """
            Description:    Given a string find the length of the longest substring without repeating characters.
                            s consists of English letters, digits, symbols and spaces.
            s:              s is the string to search in
            return:         length of substring found
        """
        # fmt: on

        # 128 characters in the set
        char = [None]*128

        left = right = length = 0

        while right < len(s):
            # current character
            cur = s[right]

            # index acts as the index of the occurance of said element when it was the current element
            index = char[ord(cur)]

            # when element is repeated before the element will be not None and 
            # if the element repeated is in within the current longest substring then
            if index is not None and left<=index<right:
                # update the left to that repeated index + 1
                left = index+1

            # update current appearing elements's index as right is the current index in the iteration
            char[ord(cur)] = right

            # find maximum length
            length = max(length, right-left+1)
            right+=1

        return length

if __name__ == "__main__":
    s = str_solutions()

    test = "abba"
    print(s.longest_substring_without_repeating_char(test))