def bubble_sort(input_list):
    for i in range(len(input_list) - 1):
        for j in range(len(input_list) - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]

    return input_list

# Example usage:

my_list = [5, 3, 1, 2, 4]

sorted_list = bubble_sort(my_list)

print(sorted_list)
