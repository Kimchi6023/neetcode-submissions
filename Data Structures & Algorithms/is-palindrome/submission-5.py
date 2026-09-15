class Solution:
    def isPalindrome(self, s: str) -> bool:
        # make a new string with ust alphanumeric characters (so just letters and numbers)
        newStr = ''
        # if the character is a alphanum, add it to the new string
        for c in s:
            if c.isalnum():
                newStr += c.lower()

        # checks if the newStr is the same as the reverse
        return newStr == newStr[::-1]
        