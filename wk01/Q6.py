a = '610'
b = a # Referencing same string
for i in range(len(a)): # 0,1,2
    b += str(i**2 + int(a[i:])) # This creates a new string object for b, hence they are no longer linked
    # str(0 + 610) = 610
    # str (1 + 10) = 11
    # sr (4 + 0) = 4
    # 610114
print(b)