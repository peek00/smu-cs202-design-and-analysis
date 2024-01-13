nums1 = [1, 2, 3, 5, 8, 13]
nums2 = [2, 8, 21, 34]

def q5(num1, num2):
    set2 = set(nums2)
    output = []
    for i in num1:
        if i not in set2:
            output.append(i)
    return output

print(q5(nums1,nums2))