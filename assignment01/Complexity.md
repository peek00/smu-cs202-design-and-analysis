# Complexity if A1Q2

I will be attempting to derive the complexity of the algorithm used. The function is made up for the following sub functions

1. math.comb
2. get_largest_choice(a, b, x)
3. get_element(n, m, target)
4. get_combination_recursive(a, b, x, m, combination)

> math.comb is assumed to be O(m).

### get_largest_choice(a, b, x)

This simply loops through and performs `math.comb` for valuyes of `a` and `b`. The lower bound of `X` is 1, which occurs when `a` and `b` are the same because there is only one way to choose `b` items from `b` items. 
1. Loops through from a to b,
2. Performs `math.comb(a,b)` which is assumed to take O(b) time. 

Hence, the worst case time complexity of this function can be assumed to be **O(a * b)**.

### get_combination_recursive(a, b, x, m, combination)

This is a recursive function where the base case is when `m == 0`. 
The recursive term is `T(m) + O(ab)`. Since `a,b` is also `n,m`, the recursive term is `T(m) + O(nm)`. I am unsure how to analyze this using Master theorem due to the presence of both `m` and `nm`...

### get_element(n, m, target)

This function complexity is dominated by `get_combination_recursive` which is `T(m) + O(nm)`.

### A1Q2(n, m, results)
This function loops through the length of the number of combinations (n,m) and calls `get_element`. The complexity of the for loop can be thought of as `log base 10 of the number of ways to choose n items from m items`.

Therefore, the complexity of this algorithm can be expressed as 
` O(log base 10 of X * T(M) * O(nm))` where `x` is `nCm`.
