def get_sizes(n:int ,m:int):
    # Find number of major sets
    # Starting digit is the index
    major_sets = n - m + 1
    size_list = []

    curr_size = 0
    for i in range(major_sets):
        # i refers to the starting digit
        last_digit = i + m - 1
        number_of_digits = n - last_digit
        print(f"Last digit: {last_digit} for starting digit: {i}, number of digits: {number_of_digits}")
        # while number_of_digits > 0:
        for j in range(number_of_digits): 
            print(number_of_digits- j)
            curr_size += number_of_digits - j
        number_of_digits -= 1
        size_list.append(curr_size)
        curr_size = 0
    return size_list

def get_starting_indexes(size_list):
    for i in range(len(size_list) - 1):
        size_list[i] += size_list[i-1]
    size_list.insert(0,0)
    return size_list[:-1]

if __name__ == "__main__":
    size_list = get_sizes(7,4)
    print(size_list)
    # indexes = get_starting_indexes(size_list)
    # print(indexes)
