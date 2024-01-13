nums = [4,1,2,1,2]

def q4(input):
    map = {}
    for i in input:
        if i in map:
            return True
        map[i] = True
    return False

print(q4(nums))