
def test(s):
    ans = 0

    i, j = 0, 0

    check = set()

    while j < len(s):
        if s[j] not in check:
            check.add(s[j])

        else:

            ans = max(ans, j - i)

    while s[j] in check:

        check.remove(s[i])

    i += 1
    j += 1

    return ans
