def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    char_dict = {}
    for i in range(len(s)):
        if char_dict.get(s[i], 0) == 0:
            if t[i] in char_dict.values():
                return False
            char_dict[s[i]] = t[i]
        else:
            if char_dict[s[i]] != t[i]:
                return False
    return True

s = "badc"
t = "badc"

print(isIsomorphic(s, t))