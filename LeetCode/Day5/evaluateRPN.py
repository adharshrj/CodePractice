# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

# Note that division between two integers should truncate toward zero.

# It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

class ReversePolishNotation:
    def evaluaterpn(self, tokens):
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":  
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)             
            elif t == "*": 
                stack.append(stack.pop() * stack.pop())
            elif t == "/":               
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))   
            else:
                stack.append(int(t))

        return stack[-1]