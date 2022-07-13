# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# class Paranthesis:
def generateparanthesis(n):
    stack = []
    res = []

    def paranthesishelper(nopen, nclosed):
        if nopen == nclosed == n:
            res.append("".join(stack))
            return
            
        if nopen < n:
            stack.append("(")
            paranthesishelper(nopen + 1, nclosed)
            stack.pop()
            
        if nclosed < nopen:
            stack.append(")")
            paranthesishelper(nopen, nclosed + 1)
            stack.pop()
        
    paranthesishelper(0,0)

    return res

    
print(generateparanthesis(4))