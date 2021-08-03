def quicksort(lst, low, high):
    """Hoare partition scheme"""
    if low >= high:
        return

    i, j = low, high
    pivot = lst[(high + low) // 2]

    while i <= j:
        while lst[i] < pivot:
            i += 1
        while lst[j] > pivot:
            j -= 1
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i, j = i + 1, j - 1
    quicksort(lst, low, j)
    quicksort(lst, i, high)


if __name__ == '__main__':
    list_of_nums = [99, 4, 5, 6, 44, 10, 5, 20, -1]
    quicksort(list_of_nums, 0, len(list_of_nums) - 1)
    print(list_of_nums)  # [-1, 4, 5, 5, 6, 10, 20, 44, 99]
