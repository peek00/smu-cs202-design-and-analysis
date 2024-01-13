strs1 = ["flower","power","chowder"]
strs2 = ["flower","flow","flight"]

def q3(input):
    """
    Sort the list first, cause prefix max is the smallest.
    """ 
    sorted_list = sorted(input, key=len)
    prefix = sorted_list[0]
    curr = -1
    for s in sorted_list[1:][::-1]:
        prefix = getPrefix(prefix, s)
    if prefix:
        print(prefix)
    else:
        print("")

def getPrefix(prefix, word):
    assert len(word) > len(prefix), "Word must be longer!"
    idx = len(prefix) - 1
    common_idx = len(prefix)
    while idx >= 0:
        if word[idx] == prefix[idx]:
            pass
        else:
            common_idx -= 1
        idx -= 1
    return prefix[:common_idx]


print(q3(strs1))
print(q3(strs2))

