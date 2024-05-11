"""Prompt is as follows:
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

 

"""

#Solution is below:

class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []

        for operation in operations:
            try:
                score = int(operation)
                stack.append(score)
            except ValueError:

                if operation == '+':
                    if len(stack) >= 2:
                        new_score = stack[-1] + stack[-2]
                        stack.append(new_score)
                
                elif operation == 'D':
                    if stack:
                        stack.append(2 * stack[-1])

                elif operation == 'C':
                    if stack:
                        stack.pop()
        return sum(stack)