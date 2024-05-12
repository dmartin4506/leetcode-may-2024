"""Prompt is as follows:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
"""

#Solution code is below:

class Solution:
    def isValid(self, s: str) -> bool:

        newStack = []
        ourDict = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in ourDict.values():
                newStack.append(char)
            elif char in ourDict:
                if not newStack or newStack.pop() != ourDict[char]:
                    return False
        return not newStack
