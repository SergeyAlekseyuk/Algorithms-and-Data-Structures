def binary_search(lst, key):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == key:
            return mid
        if lst[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == '__main__':
    list_of_nums = [1, 3, 5, 7, 8, 9, 10]

    first_example = 7
    first_example_index = binary_search(list_of_nums, first_example)
    print(first_example_index)  # 3

    second_example = 4
    second_example_index = binary_search(list_of_nums, second_example)
    print(second_example_index)  # -1 / num not found
