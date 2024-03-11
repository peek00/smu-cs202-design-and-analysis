import sys

def bounded_knapsack(weight, value, quantity, limit):
    """
    Given n = total number of unique items, m = capacity of knapsack, q = total quantity of all items,
    we can consider the complexity to be O(n * log2m * q).
    
    This code loops over all the total unique items, from 1 to the limit (capacity of the knapsack).
    For each possible item at the current limit, it loops through whichever number is smaller: 
    the total quantity of the specific item or the total number of the specific number that 
    can fit in the backpack.

    At the worst case, the last loop will go on for the the entire available quantity of the item. 
    I believe we can simplify this last part to be the total quantity of ALL items available. 

    So in a way, the complexity of this can be considered as 
    O(total number of items * capacity of the knapsack * total quantity of all items available),
    where since the capacity of the knapsack is an integer input, we can take the binary representation
    of the number which is log2{capacity of the knapsack}.

    Given n = total number of unique items, m = capacity of knapsack, q = total quantity of all items,
    we can consider the complexity to be O(n * log2m * q).
    """
    ### Sample code ###
    # n = len(weight)
    # return sum([value[i] * quantity[i] for i in range(n)])
    ### Sample code ###

    # Indicated 0, 1,2, 3, 4 ... limit for number of columns
    # Indicate item 1,2,3... for number of rows
    dp = [[0] * (limit + 1) for _ in range(len(weight))] 
    no_of_unique_items = len(weight)

    # Initialize the first col to be 0 for all, since 0 capacity means cannot have items
    for i in range(no_of_unique_items):
        dp[i][0] = 0

    # Loops through the current item, only considering to add or exclude this item

    for item in range(no_of_unique_items): # O(weight * limit * quantity)
        # Loop through the current capacity that goes from 0 to limit, skip 0
        for current_capacity in range(1, limit + 1): 
            # If we do not pick this item up, means we take the current capacity from previous item
            dp[item][current_capacity] = dp[item - 1][current_capacity]
            # Check if at least one of current item can be included
            if weight[item] <= current_capacity:
                # Consider each possible quantity of the current item
                # Start from at least 1 item 
                for no_of_item in range(1, min(quantity[item] + 1, current_capacity // weight[item] + 1)):
                    # Update the dp table with the maximum value
                    dp[item][current_capacity] = max(
                        dp[item][current_capacity],
                        dp[item - 1][current_capacity - no_of_item * weight[item]] + no_of_item * value[item]
                    )
    return dp[-1][-1]

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [[int(t) for t in s.split(':')] for s in sys.stdin.readline().split()]
    print(bounded_knapsack([i[0] for i in a[:-1]], [i[1] for i in a[:-1]], [i[2] for i in a[:-1]], a[-1][0]))
