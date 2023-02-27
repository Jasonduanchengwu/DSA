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

    def sort_sentence(self, s: str) -> str:
        """
            Description:    Given a unsorted string with index appended to the back of each word, 
                            sort the string to its intended sentence
            s:              String given
            return:         Sorted string
        """
        # create array structure to utilize index
        s = s.split()
        result = [""]*len(s)

        # place the corresponding substrings into their index location
        for ele in s:
            # index provided starts from 1, 
            # substring without index and includes space
            result[int(ele[-1]-1)] = ele[:-1] + " "

        # saves memory
        s = ""
        for ele in result:
            # turn back to string
            s += ele

        # return without last space
        return s[:-1]

    def truncate_sentences(self, s: str, c: int) -> str:
        """
            Description:    Given a string and c no of words to truncate, return modified string
            s:              String to be modified
            s:              Count of words to include in modified string
            return:         Modified String
        """
        # split word to count len of c no of word with space, sum them and subtract the last space
        return s[:sum([len(d)+1 for d in s.split()[:c]])-1]
    
    def count_asterisk(self, s: str) -> int:
        """
            Description:    Given a string s, count the number of "*" in the substrings 
                            that is separated by "|", skipping every alternative substring
            s:              String given
            return:         Number of asterisks
        """
        return sum(d.count("*") for d in s.split("|")[::2])
    
    def to_lowercase(self, s: str) -> str:
        """
            Description:    Given a string s, convert all letters to lowercase. With not using .lower() solution
            s:              String given
            return:         Lowercase string
        """
        # python lib
        # return s.lower()

        for ele in s:
            # ascii numbers of uppercase letters
            if 64<ord(ele)<91:
                s=s.replace(ele,chr(ord(ele)+25))
        return s
    
    def is_list_string_equal(self, list1: list[str], list2: list[str])->bool:
        """
            Description:    Given 2 lists of strings, determine if both list has the same string 
                            if the elements are combined together
            list1:          list of string
            list2:          list of string
            return          True if both string is equal, False otherwise
        """
        # concatenate both list of string, then compare
        return "".join(list1)=="".join(list2)
    
    def is_pangram(self, s: str) -> bool:
        """
            Description:    Given a string s, determine if s is a pangram 
                            (all letters of the english alphabet appears at least once)
            s:              Given string
            return:         True if pangram otherwise False
        """
        # length must be more than 26 for all letters to appear at least 1
        if len(s)<26:
            return False
        
        # check all letters
        for i in range(26):
            # return False when 1 letter does not exist
            if s.__contains__(chr(i+97)) is False:
                return False
        # else all existed
        return True
    
    def max_nest_parentheses_depth(self, s: str) -> int:
        """
            Description:    Given a string of mathematical equation, find out the maximum nesting depth of the parentheses
                            given parentheses are always closed
            s:              Given string
            return:         Maximum nesting depth of the parentheses
        """
        max_depth = 0
        for i,ele in enumerate(s):
            # when the ele is not '(' or ')'
            if ele is not '(' or ele is not ')':
                # locate the inner most ele
                # take the max of difference of the left side of the ele and difference of the right side of the ele
                max_depth = max(max_depth, s[:i].count(')')-s[:i].count('('), s[i+1:].count(')')-s[i+1:].count('('))
        return max_depth
    
    def count_consistent_string(self, allowed: str, words: list[str]) -> int:
        """
            Description:    Given some allowed letters, determine how many of the words are consistent
                            (consistency refers to if a string contains only letters that are allowed)
            allowed:        Letters allowed
            words:          list of words
            return:         count of consistent words
        """
        for ele in allowed:
            words = [w.replace(ele,"") for w in words]
        return words.count("")
    
    def reverse_words(self, s: str) -> str:
        """
            Descriptions:   Reverse all words in string s
            s:              Given string
            return:         string of reversed words
        """
        return " ".join([ele[::-1] for ele in s.split()])
    
if __name__ == "__main__":
    s = str_solutions()

    s1 = "anagram"
    s2 = "nagaran"
    print(s.is_anagram(s1,s2))