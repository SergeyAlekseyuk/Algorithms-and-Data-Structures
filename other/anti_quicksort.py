def anti_quicksort(n):
    lst = [i + 1 for i in range(n)]
    for i in range(2, n):
        lst[i], lst[i // 2] = lst[i // 2], lst[i]
    return lst


if __name__ == '__main__':
    print(anti_quicksort(5))  # [1, 4, 5, 3, 2]
