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

    def is_anagram(self, s: str, t: str) -> bool:
        # fmt: off
        """
            Description:    Given two strings s,t find out if they are anagrams of eachother
                            (anagram is a word that is formed by rearranging the letters in another word, 
                            each letter is used exactly once)
            s,t:            s,t are strings to check for anagram
            return:         True if s,t are anagrams, False otherwise
        """
        # fmt: on

        # check if length of s,t matches
        length = len(s)
        if length != len(t):
            return False
        
        # only 26 characters in English letters
        char = [0] * 26

        for i in range(length):
            # calculate occurances of each letter, 
            # index in ascii is -97 for when a=0
            char[ord(s[i])-97] +=1
            char[ord(t[i])-97] -=1
        
        # True if all elements in char is 0 otherwise False
        return all([True if ele == 0 else False for ele in char])


if __name__ == "__main__":
    s = str_solutions()

    s1 = "anagram"
    s2 = "nagaran"
    print(s.is_anagram(s1,s2))