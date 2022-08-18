# Design a search suggestion system that searches the products array and returns an array for each character in the input string

def search(products, string):
    products.sort()
    res = []
    l, r = 0, len(products) - 1

    for i in range(len(string)):
        c = string[i]

        while l <= r and (len(products[l]) <= i or products[l][i] != c):
            l += 1

        while l <= r and (len(products[r]) <= i or products[r][i] != c):
            r -= 1

        res.append([])
        diff = r - l + 1

        for j in range(min(3, diff)):
            res[-1].append(products[l + j])

    return res 