def counting_sort(lst, p):
    sorted_lst = [0] * len(lst)

    temp = [0 for _ in range(10)]

    for i in range(len(lst)):
        temp[lst[i] // (10 ** p) % 10] += 1

    for j in range(1, 10):
        temp[j] = temp[j] + temp[j - 1]

    for i in range(len(lst) - 1, -1, -1):
        sorted_lst[temp[lst[i] // (10 ** p) % 10] - 1] = lst[i]
        temp[lst[i] // (10 ** p) % 10] -= 1

    return sorted_lst


def radix_sort(lst, d):
    for i in range(d):
        lst = counting_sort(lst, i)
    return lst


if __name__ == '__main__':
    list_of_nums = [999, 321, 987, 456, 123, 777, 654, 555, 789, 268, 111]
    number_of_digits = len(str(max(list_of_nums)))
    result = radix_sort(list_of_nums, number_of_digits)
    print(result)  # [111, 123, 268, 321, 456, 555, 654, 777, 789, 987, 999]
