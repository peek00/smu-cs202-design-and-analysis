def get_sizes(n:int ,m:int):
    # Find number of major sets
    major_sets = n - m + 1
    last_digit = n - m
    number_of_digits = n - last_digit # 4
    _ = number_of_digits
    size_list = []

    curr_size = 0
    for i in range(major_sets):
        # i refers to the starting digit
        number_of_digits = _ - i
        while number_of_digits > 0:
            for j in range(number_of_digits): 
                curr_size += number_of_digits - j
            number_of_digits -= 1
        size_list.append(curr_size)
        curr_size = 0
    return size_list
if __name__ == "__main__":
    print(get_sizes(20, 10))
