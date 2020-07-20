def insertion_sort_recursive(array: list) -> list:
    if len(array) == 1:
        return array
    else:
        sorted_array = insertion_sort_recursive(array[:-1])
        element_to_insert = array[-1]
        for idx in reversed(range(len(sorted_array) + 1)):
            if sorted_array[idx - 1] <= element_to_insert:
                break
        sorted_array.insert(idx, element_to_insert)
        return sorted_array


def insertion_sort_iterative(array: list) -> list:
    for outer_idx in range(1, len(array)):
        element_to_insert = array[outer_idx]
        idx = outer_idx
        while idx >= 0 and array[idx - 1] > element_to_insert:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = element_to_insert
    return array


def merge_sort(array: list) -> list:
    if len(array) == 1:
        return array
    else:
        mid_point = len(array) // 2
        return merge(merge_sort(array[:mid_point]), merge_sort(array[mid_point:]))


def merge(left: list, right: list) -> list:
    merged_array = []
    left_idx = 0
    right_idx = 0
    left.append(float('inf'))  # Sentinel value to avoid extra code to empty any remaining elements into merged list
    right.append(float('inf'))
    for _ in range(len(left) + len(right) - 2):
        if left[left_idx] < right[right_idx]:
            merged_array.append(left[left_idx])
            left_idx += 1
        else:
            merged_array.append(right[right_idx])
            right_idx += 1
    assert len(merged_array) == len(left) + len(right) - 2
    return merged_array


print(insertion_sort_recursive([10, 9, 9, 9, 8, 8, 8]))
print(insertion_sort_iterative([10, 9, 9, 9, 8, 8, 8]))
print(merge_sort([10, 9, 9, 9, 8, 8, 8]))
