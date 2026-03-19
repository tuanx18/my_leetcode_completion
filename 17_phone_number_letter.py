
def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    phone_dict = {
        "2": ["a", "b", "c"], 
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
        }
    if not digits:
        return None
    limit_key = len(digits)
    res = []
    path = []

    def backtrack(pos):
        if pos == limit_key:
            res.append(''.join(path))
            return

        letters = phone_dict[digits[pos]]
        for ch in letters:
            path.append(ch)       # choose for this position
            backtrack(pos + 1)    # recurse for the next position
            path.pop()            # undo

    backtrack(0)
    return res

digits = "23"
print(letterCombinations(digits))