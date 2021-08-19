def bucket_sort(lst):
    bucket = []

    # Create empty buckets
    for i in range(len(lst)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in lst:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(lst)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(lst)):
        for j in range(len(bucket[i])):
            lst[k] = bucket[i][j]
            k += 1
    return lst


if __name__ == '__main__':
    list_of_nums = [.52, .51, .47, .42, .37, .33, .32]
    result = bucket_sort(list_of_nums)
    print(result)  # [0.32, 0.33, 0.37, 0.42, 0.47, 0.51, 0.52]
