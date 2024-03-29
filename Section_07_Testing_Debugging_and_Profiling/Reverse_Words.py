"""
Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

Example 1:

Input:
S = i.like.this.program.very.much
Output: much.very.program.this.like.i
Explanation: After reversing the whole
string(not individual words), the input
string becomes
much.very.program.this.like.i

Algorithm:

Initially, reverse the individual words of the given string one by one, for the above example, after reversing
individual words the string should be 'i.ekil.siht.margorp.yrev.hcum'.
"""


def reverse_words(s):
    # init
    result = ""
    words = []
    currWord = ""

    # loop through string
    for i in range(len(s)):
        if s[i] == ".":
            words.append(currWord)
            currWord = ""
        else:
            currWord += s[i]

    words.append(currWord)

    for i in range(len(words) - 1, -1, -1):
        result += words[i]
        if i:
            result += "."
    return result


print(reverse_words("i.like.this.program.very.much"))
