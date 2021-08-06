def counting_sort(lst, sorted_lst, num):

    temp = [0 for _ in range(num)]

    for i in range(len(lst)):
        temp[lst[i]] += 1

    for j in range(1, num):
        temp[j] = temp[j] + temp[j - 1]

    for i in range(len(lst) - 1, -1, -1):
        sorted_lst[temp[lst[i]] - 1] = lst[i]
        temp[lst[i]] -= 1

    return sorted_lst


if __name__ == '__main__':
    list_of_nums = [6, 0, 2, 1, 0, 3, 4, 6, 1, 3, 2]
    sorted_list = [0] * len(list_of_nums)
    result = counting_sort(list_of_nums, sorted_list, max(list_of_nums) + 1)
    print(result)  # [0, 0, 1, 1, 2, 2, 3, 3, 4, 6, 6]
