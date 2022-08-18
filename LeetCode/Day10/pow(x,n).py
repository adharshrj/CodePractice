# Create a function that takes two inputs x and n and returns x^n

def powf(x, n):
    def helper(x, n):
        if x == 0: return 0
        if n == 0: return 1
        
        res = helper(x*x, n//2)
        return x * res if n%2 else res
    
    result = helper(x,abs(n))
    return result if n >= 0 else 1 / result

print(powf(2, -3))