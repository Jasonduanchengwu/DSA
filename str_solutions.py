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

    def is_palindrome(self, s: str)->bool:
        """
            Description:    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
                            and removing all non-alphanumeric characters, 
                            it reads the same forward and backward. Alphanumeric characters include letters and numbers.
            s:              Input string
            return:         whether string is a palindrome
        """
        s = s.lower()
        res = ""
        for ele in s:
            if 97<=ord(ele)<=122 or 48 <=ord(ele)<=57:
                res += ele
        return res == res[::-1]
    
    def max_balanced_substring(self, s: str) -> int:
        """
            Description:    Given a balanced string s containing "L" and "R", determine the maxed number of balanced substrings in s
            s:              balanced String
            return:         max number of balanced substrings
        """

        s_list = []
        start_index = 0
        char_dict = {
            "L" : 0,
            "R" : 0
        }
        for i in range(len(s)):
            char_dict[s[i]] += 1
            if char_dict["L"] == char_dict["R"] and char_dict[s[i]] is not 0:
                s_list.append(s[start_index:i+1])
                start_index = i+1
                char_dict["L"] =0
                char_dict["R"]=0
        return len(s_list)
        
    def count_divisible_digits(self, num: int) -> int:
        """
            Descriptions:   Given a integer num, count the number of divisiable digits in num by num
            num:            Integer given
            return:         number of divisiable digits
        """
        # List comprehension to list of int digits
        digits = [int(d) for d in str(num)]
        div_count = 0
        for ele in digits:
            if num%ele is 0:
                div_count +=1
        return div_count

    def decode_messages(self, keys: str, message: str) -> str:
        """
            Descriptions:   Given a set of keys and message, translate the message into human readables english
            keys:           keys representing increasing alphabetical letters
            message:        message to be decoded
            return:         decoded message
        """
        # remove repeat letters and spaces for keys
        def remove_repeat_chars(s:str):
            # list for keys
            char = []
            s = s.replace(" ","")
            for ele in s:
                ele = ele.lower()
                # only register once per letter
                if ele not in char:
                    char.append(ele)
            return char

        # key and value space is unchanged
        decode_dict = {
            " ": " "
        }

        # register values for keys in alphabetical order
        for index, ele in enumerate(remove_repeat_chars(keys)):
            decode_dict[ele] = chr(index+97)

        decoded_message =""
        # decode message
        for ele in message:
            decoded_message += decode_dict[ele]
        return decoded_message

    def length_of_last_word(self, s: str)->int:
        """
            Descriptions:   Given a string, return the length of the last word in the string
            s:              String given
            return:         length of the last word 
        """
        return len(s.split()[-1])
        
if __name__ == "__main__":
    s = str_solutions()

    s1 = "anagram"
    s2 = "nagaran"
    print(s.is_anagram(s1,s2))