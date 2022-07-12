# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.

def validparanthesis(s):
    stack = []
    testmap = {')':'(', '}':'{', ']':'['}

    for ch in s:
        if ch in testmap:
            if stack and stack[-1] == testmap[ch]:
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)
    
    # Hint: return True if not stack else False
    return not stack
        