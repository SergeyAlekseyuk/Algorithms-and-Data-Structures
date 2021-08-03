def count_inversions(lst):
    list_length = len(lst)
    if list_length == 1:
        return lst, 0
    else:
        left_lst = lst[:list_length//2]
        right_lst = lst[list_length//2:]
        left_lst, left_counter = count_inversions(left_lst)
        right_lst, right_counter = count_inversions(right_lst)
        merged_lst = []
        i = 0
        j = 0
        counter = left_counter + right_counter
        while i < len(left_lst) or j < len(right_lst):
            if j == len(right_lst) or (i < len(left_lst) and left_lst[i] <= right_lst[j]):
                merged_lst.append(left_lst[i])
                i = i + 1
            else:
                merged_lst.append(right_lst[j])
                counter += len(left_lst) - i
                j = j + 1
        merged_lst += left_lst[i:]
        merged_lst += right_lst[j:]
        return merged_lst, counter


if __name__ == '__main__':
    list_of_nums = [5, 4, 3, 2, 1]
    sorted_list, inversions = count_inversions(list_of_nums)
    print(sorted_list)  # [1, 2, 3, 4, 5]
    print(inversions)  # 10

